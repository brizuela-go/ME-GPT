# ME GPT with OPEN AI API AND ELEVENLABS API

## 🔳 Introduction

This is a simple example of how to use the Open AI API and the ElevenLabs API to generate speech to speech/text with the text-davinci-003 model. The UI/UX was bulit with [Gradio](https://gradio.app/).

## 📄 Requirements

- Python 3.6 or higher
- pip3
- virtualenv

## 📦 Installation

### 🐍 Python

```bash
$ virtualenv -p python venv
$ source venv/bin/activate
```

### 📚 Libraries

```bash
$ pip install -r requirements.txt
```

## 🚀 Usage

```bash
$ python app.py
```

## 🔑 Get your Open AI and ElevenLabs API keys here and start clonig your voice!

- [Open AI](https://platform.openai.com/)
- [ElevenLabs](https://beta.elevenlabs.io/)

## ℹ️ Note

In order to clone your voice, you'll need to upgrade to at least the Starter plan on ElevenLabs. The free plan only allows you to use default voices. You can find more information about the pricing [here](https://beta.elevenlabs.io/pricing).

Also, replace winsound with pydub playback if you're on a non-Windows machine.

```python
play(AudioSegment.from_wav("output.wav"))
```

## 🐳 Docker

```bash
$ docker build -t me-gpt .
$ docker run --rm -it -p 7860:7860 me-gpt:latest
```
