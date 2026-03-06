
# AI Girlfriend Assistant (Offline)

Local AI assistant running completely offline using **Ollama + Python**

No API key required. Runs on your own computer.

---

## Features
- Chat conversation
- Memory saving
- Personality behavior
- Runs locally (privacy safe)
- Works without internet after model download

---

## Requirements
- Python 3.10+
- Ollama installed
- 8GB RAM recommended (4GB minimum with small model)

Install model:
```bash
ollama run llama3
```

---

## Installation

Clone repo:
```bash
git clone https://github.com/YOUR_USERNAME/ai-girlfriend-assistant.git
cd ai-girlfriend-assistant
```

Install dependencies:
```bash
pip install requests
```

---

## Run Assistant

Start Ollama server:
```bash
ollama serve
```

Run python:
```bash
python main.py
```

---

## Project Structure
```
ai_gf/
 ├─ main.py
 ├─ brain.py
 ├─ memory.py
 ├─ personality.txt
```

---

## Notes
First run downloads AI model (~4GB)

---

Made for learning AI locally without paid APIs
