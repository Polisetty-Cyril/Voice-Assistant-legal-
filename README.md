# Legal Voice Assistant

An **AI-powered legal voice assistant** that allows users to ask legal questions using voice and receive spoken answers in real time.  
It utilizes **speech recognition** to capture questions, verifies whether they are law-related, and generates detailed answers using a legal knowledge context and a text generation model.

---

## 🚀 Features

- 🎙 **Voice Input** – Ask your legal questions by speaking naturally.
- 🗣 **Voice Output** – Hear the AI's response through text-to-speech.
- ⚖ **Legal Q&A** – Detects law-related queries and answers with examples.
- 🧠 **Context-Aware** – Uses pre-defined legal context for accurate responses.
- 🛑 **Exit Command** – Stop the assistant anytime by saying "exit" or "stop".

---

## 🛠 Tech Stack

- **Python 3.10+**
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) – Speech-to-text conversion.
- [SAPI.SpVoice](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ms723602(v=vs.85)) – Windows text-to-speech engine.
- [Transformers](https://huggingface.co/transformers/) – For generating detailed answers.
- [Flan-T5](https://huggingface.co/google/flan-t5-base) – Open-source text-to-text generation model.

---
