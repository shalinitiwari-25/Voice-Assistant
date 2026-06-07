# Trivya AI - Voice Assistant

## Overview

Trivya AI is a Python-based assistant that supports both voice and web interactions. The project combines speech recognition, text-to-speech technology, and a Streamlit-based interface to provide a simple and interactive user experience.

The assistant can recognize commands, respond with speech, provide useful information such as the current date and time, open websites, and assist users through either voice or text-based interaction.

---

## Features

### Voice Assistant Mode

* Speech recognition using SpeechRecognition
* Text-to-speech responses using pyttsx3
* Current date and time queries
* Greeting and conversational responses
* Joke generation
* Website navigation through voice commands
* Google search support
* Error handling for microphone and network issues

### Web Interface Mode

* Streamlit-based web application
* Text-based interaction with the assistant
* Conversation history display
* Browser-friendly interface for quick testing and demonstrations

---

## Screenshots

### Voice Assistant

![Voice Assistant](assets/voice_assistant.png)

### Streamlit Interface

![Streamlit Interface](assets/streamlit_interface.png)

## Technologies Used

* Python
* Streamlit
* SpeechRecognition
* PyAudio
* pyttsx3
* webbrowser
* datetime

---

## Project Structure

```text
Voice-Assistant/
│
├── main.py              # Terminal-based voice assistant
├── streamlit_app.py     # Streamlit web interface
├── requirements.txt     # Project dependencies
├── README.md
├── .gitignore
└── assets/              # Screenshots and media files
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shalinitiwari-25/Voice-Assistant.git
```

### 2. Navigate to the Project Directory

```bash
cd Voice-Assistant
```

### 3. Create and Activate a Virtual Environment (Optional)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Voice Assistant Mode

Run the terminal-based voice assistant:

```bash
python main.py
```

### Web Interface Mode

Run the Streamlit application:

```bash
streamlit run streamlit_app.py
```

---

## Example Commands

The assistant currently supports commands such as:

* Hello
* How are you
* What is your name
* Who created you
* What is the time
* What is the date
* Tell me a joke
* Open YouTube
* Open Google
* Open GitHub
* Python tutorial
* Exit

---


## Architecture

The project currently provides two user interfaces:

1. **Voice Interface (main.py)**

   * Uses microphone input
   * Converts speech to text
   * Processes commands
   * Responds using text-to-speech

2. **Web Interface (streamlit_app.py)**

   * Uses a browser-based interface
   * Accepts text commands
   * Displays responses on the webpage

Both interfaces provide similar assistant capabilities, allowing users to interact through either voice or text.

---

## Future Enhancements

* Browser microphone integration
* Personalized user memory
* AI-powered conversations
* Dynamic command handling
* External API integration
* Cloud deployment

---

## Author

**Shalini Tiwari**

Aspiring Software Developer | Open Source Contributor | AI Enthusiast

GitHub: https://github.com/shalinitiwari-25

---

## Project Goal

The goal of Trivya AI is to demonstrate how speech recognition, text-to-speech systems, and web interfaces can be combined to build an interactive assistant capable of performing everyday tasks through natural user interaction.
