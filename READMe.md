## 🔊 Real-Time Voice-to-Voice Chatting Using Open-Source Models (Locally)

A fully **offline**, real-time voice assistant pipeline using:

* **Speech-to-Text (STT)**: Whisper v2 tiny via WhisperLive
* **Large Language Model (LLM)**: `Llama-3.2-1B-Instruct-IQ3_M.gguf`
* **Text-to-Speech (TTS)**: Piper with `en_US-lessac-medium` voice

> 🧠 Speak to your local LLM — it transcribes, reasons, and speaks back, all on your machine.

---

## 📦 Components

| Task | Tool Used                                                                                       |
| ---- | ----------------------------------------------------------------------------------------------- |
| STT  | [WhisperLive](http://github.com/collabora/WhisperLive/) (Whisper v2 tiny)                       |
| LLM  | [Llama 3.2 1B Instruct](https://huggingface.co/bartowski/Llama-3.2-1B-Instruct-GGUF)            |
| TTS  | [Piper (GPL edition)](https://github.com/OHF-Voice/piper1-gpl) with `en_US-lessac-medium` voice |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/voice2voice-assistant.git
cd voice2voice-assistant
```

---

### 2️⃣ Download LLM (GGUF) Model

```bash
wget https://huggingface.co/bartowski/Llama-3.2-1B-Instruct-GGUF/resolve/main/Llama-3.2-1B-Instruct-IQ3_M.gguf
```

Move it to the correct directory:

```bash
mv Llama-3.2-1B-Instruct-IQ3_M.gguf src/stt/WhisperLive/models/
```

---

### 3️⃣ Download STT (Whisper v2 tiny) Model Files

Create a directory and download the model files:

```bash
mkdir -p src/stt/WhisperLive/models/faster_whisper_tiny
```

Go to [https://huggingface.co/Systran/faster-whisper-tiny/tree/main](https://huggingface.co/Systran/faster-whisper-tiny/tree/main)
Download **all model files** (like `config.json`, `model.bin`, etc.), and place them inside:

```bash
src/stt/WhisperLive/models/faster_whisper_tiny/
```

---

### 4️⃣ Download TTS (Piper) Voice Model

```bash
python3 -m piper.download_voices en_US-lessac-medium
```

Move the downloaded voice folder to the following directory:

```bash
mv voices/en_US-lessac-medium src/tts/piper_/model/
```

---

### 5️⃣ Start Whisper STT Server (in Docker)

Navigate to the Whisper server directory:

```bash
cd src/stt/WhisperLive/
```

#### ✅ Build Docker Image

Choose based on your hardware:

**For CPU:**

```bash
docker build -t whisper-stt:cpu -f docker/Dockerfile.cpu .
```

**(Optional) For GPU:**

```bash
docker build -t whisper-stt:gpu -f docker/Dockerfile.gpu .
```

#### ▶️ Run Docker Container

```bash
docker run -d -p 9090:9090 -v "$(pwd):/app" --name whisper-stt-app whisper-stt:cpu
```

---

### 6️⃣ Create Conda Environment

Tested with Python 3.11.13:

```bash
conda create -n voice_env python=3.11.13 -y
conda activate voice_env
```

---

### 7️⃣ Install Python + System Dependencies

Run the setup script:

```bash
bash setup_env.sh
```

> Example contents of `setup_env.sh`:

```bash
#!/bin/bash

pip install -r requirements.txt
pip install https://github.com/abetlen/llama-cpp-python/releases/download/v0.3.2/llama_cpp_python-0.3.2-cp311-cp311-linux_x86_64.whl
sudo apt install -y musl-dev
sudo ln -sf /usr/lib/x86_64-linux-musl/libc.so /lib/libc.musl-x86_64.so.1
```

---

## 🚀 Run the Assistant

```bash
python main.py
```

> 🎤 Speak → 🤖 WhisperLive transcribes → 🧠 LLM reasons → 🔊 Piper speaks

---

## ✅ Tested On

* OS: Ubuntu 24
* Python: 3.11.13
* Hardware: CPU-only (GPU support optional via Docker)

---

## 📚 References

| Component         | Source                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| WhisperLive (STT) | [github.com/collabora/WhisperLive](http://github.com/collabora/WhisperLive/)                                       |
| Whisper Model     | [huggingface.co/Systran/faster-whisper-tiny](https://huggingface.co/Systran/faster-whisper-tiny)                   |
| Piper (TTS)       | [github.com/OHF-Voice/piper1-gpl](https://github.com/OHF-Voice/piper1-gpl)                                         |
| Llama GGUF Model  | [huggingface.co/bartowski/Llama-3.2-1B-Instruct-GGUF](https://huggingface.co/bartowski/Llama-3.2-1B-Instruct-GGUF) |

---