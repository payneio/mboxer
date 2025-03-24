import email
import email.header
import email.utils
import mailbox
import os
import re

from dotenv import load_dotenv

# === Load config ===
load_dotenv()
mbox_path = os.getenv("MBOX_PATH")
output_dir = os.getenv("OUTPUT_DIR", "eml_output")
os.makedirs(output_dir, exist_ok=True)


# === Helpers ===
def sanitize_filename(name):
    return re.sub(r"[^\w\-_.]", "_", name)


def decode_header_field(header_value):
    if header_value is None:
        return ""
    if isinstance(header_value, email.header.Header):
        return str(header_value)
    decoded_fragments = email.header.decode_header(header_value)
    return "".join(
        str(t[0], t[1] or "utf-8") if isinstance(t[0], bytes) else t[0]
        for t in decoded_fragments
    )


def extract_addresses(header_value):
    decoded = decode_header_field(header_value)
    return [
        email.utils.parseaddr(addr)[1].lower()
        for addr in decoded.split(",")
        if addr.strip()
    ]


# === Process MBOX ===
mbox = mailbox.mbox(mbox_path)

for i, msg in enumerate(mbox):
    # Parse date
    date_str = msg.get("date")
    try:
        parsed_date = email.utils.parsedate_to_datetime(date_str)
        timestamp = parsed_date.strftime("%Y-%m-%d_%H-%M-%S")
    except Exception:
        timestamp = f"unknown_date_{i:04}"

    # Extract sender and recipients
    from_addr = email.utils.parseaddr(decode_header_field(msg.get("from")))[1].lower()
    to_addrs = extract_addresses(msg.get("to"))
    safe_sender = sanitize_filename(from_addr or "unknown")

    if not to_addrs:
        safe_recipient = "unknown"
    elif len(to_addrs) == 1:
        safe_recipient = sanitize_filename(to_addrs[0])
    else:
        safe_recipient = sanitize_filename(to_addrs[0]) + "_et_all"

    # Compose filename
    base_name = f"{timestamp}_from_{safe_sender}_to_{safe_recipient}"
    max_len = 100
    filename = (
        (base_name[:max_len] + ".eml")
        if len(base_name) > max_len
        else base_name + ".eml"
    )
    filepath = os.path.join(output_dir, filename)

    # Save .eml file
    try:
        with open(filepath, "wb") as f:
            f.write(bytes(msg))
        print(f"[{i + 1:04}] ✅ Saved: {filename}")
    except Exception as e:
        print(f"[{i + 1:04}] ❌ Error saving {filename}: {e}")
