# 📤 MBOX Exporter

A Python utility to convert `.mbox` files into individual `.eml` files with readable, timestamped filenames like:

```txt
2025-03-23_15-09-42_from_alice_example_com_to_bob_example_com.eml
```

Supports `.env` config, intelligent filename generation, and works with long-running mail archives.

---

## 🔧 Features

- Converts `.mbox` files to `.eml`
- Filenames include timestamp, sender, and recipient
- Handles multiple recipients (`et_all`)
- Loads configuration from `.env`
- Linting and formatting via [`ruff`](https://docs.astral.sh/ruff/)
- Compatible with VS Code + `uv`

---

## 📦 Setup

### 1. Clone the repo & install dependencies

```bash
git clone https://github.com/yourname/mbox-exporter.git
cd mbox-exporter
uv venv .venv
. .venv/Scripts/activate   # or 'source .venv/bin/activate' on macOS/Linux
uv sync
```

### 2. Configure `.env`

An example can be found in `.env.example`

```env
MBOX_PATH=your_file.mbox
OUTPUT_DIR=eml_output
```

---

## 🚀 Usage

Run the exporter:

```bash
python convert.py
```

Each email will be saved in the output folder with a filename like:

```txt
2025-03-23_10-45-12_from_alice_to_bob_et_all.eml
```

---

## 🧪 Development

- Lint & format:

  ```bash
  ruff check . --fix
  ```

- VS Code users can use `.vscode/launch.json` to run with environment variables loaded.

---

## 📚 What Can I Do With .eml Files?

- Open in email clients (Thunderbird, Outlook, etc.)
- Parse & analyze with Python or CLI tools
- Extract metadata, body, or attachments
- Archive and search with `grep`, `ripgrep`, etc.
- Convert to `.pdf`, `.txt`, or re-send via SMTP

---

## 🛠️ TODO (Feel free to contribute!)

- [ ] Add subject to filenames
- [ ] Export metadata CSV
- [ ] Extract attachments
- [ ] CLI interface with `argparse` or `typer`
- [ ] Batch `.mbox` directory support

---

## 📄 License

MIT — free to use, improve, and adapt.
