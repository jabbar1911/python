# 🌍 Multi-Language Voice Translator

A Python-based **Voice Translator System** that listens to your speech, converts it into text, translates it into multiple languages, and speaks the translated output using text-to-speech.

This project demonstrates real-time speech recognition, translation, and audio synthesis — similar to how Google Assistant, Siri, and Alexa work.

---

## 📌 About the Project

The Multi-Language Voice Translator allows users to:

- 🎤 Speak into the microphone
- 📝 Convert speech → text
- 🌐 Translate English text into multiple languages
- 🔊 Hear the translated text spoken back
- 🧭 Use a simple, interactive CLI menu

This project is beginner-friendly yet powerful enough to demonstrate how voice assistants work internally.

---

## 🚀 Features

- 🎤 Real-time **Speech Recognition**
- 🌐 **English → Multi-Language Translation**
  - Hindi
  - Telugu
  - Tamil
  - Kannada
  - French
  - Spanish
- 🔊 **Text-to-Speech Output**
- 🎧 Automatic audio playback
- 🧹 Auto deletion of temporary audio files
- 🖥️ Clean CLI menu with Exit option

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| SpeechRecognition | Convert speech to text |
| gTTS | Convert text to speech |
| deep_translator | Translate text between languages |
| playsound | Play audio output |
| PyAudio | Microphone input |
| uuid | Create unique filenames |
| os | File operations |

---

## 📦 Installation

### Step 1: Install Dependencies

Install all required packages using pip:

```bash
pip install SpeechRecognition
pip install gTTS
pip install deep-translator
pip install playsound
pip install pyaudio
```

### Step 2: PyAudio Troubleshooting (Windows)

If PyAudio fails to install, follow these steps:

**1. Download the .whl file**

Visit the official wheels site:
[https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

Download the correct .whl file for your Python version (example: `cp39` = Python 3.9).

**2. Install the downloaded file manually**

```bash
pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl
```

> Note: The filename may differ depending on your Python version.

---

## ▶️ How to Run the Project

1. Open Terminal / Command Prompt
2. Navigate to the project directory
3. Run the script:

```bash
python main.py
```

---

## 📜 Usage Instructions

After running the program, this interactive menu appears:

```
1  English → Hindi
2  English → Telugu
3  English → Tamil
4  English → Kannada
5  English → French
6  English → Spanish
7  Exit
```

### Step-by-Step Workflow

**Step 1: Choose a Language**

Enter a number (1-6) to select your target language. Example: Enter `1` for English → Hindi.

**Step 2: Speak When Prompted**

The program listens to your voice and converts it into text.

**Step 3: Get Translation + Audio Output**

- ✔ The translated text appears on the screen
- 🔊 The system speaks the translated text out loud

---


## 📈 Example Output

```
🎤 Speak now...
🗣️ You said: Hello, how are you?
🌐 Hindi: नमस्ते, आप कैसे हैं?
🔊 Playing translated audio...
```

---

### Translation Errors

- Verify your internet connection (translations require online connectivity)
- Check that your input text is in English
- Restart the program if translation fails

### Audio Playback Issues

- Ensure your speakers/headphones are connected
- Check system volume settings
- Verify playsound library is properly installed
