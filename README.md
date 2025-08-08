# jarvis-ai-assistant
this is my first ai assistant named jarvis
# 🧠 Jarvis AI Voice Assistant

**Jarvis** is a Python-based voice assistant that can respond to your voice commands using real-time speech recognition and AI-generated responses. Inspired by the Jarvis from Iron Man, this assistant can open websites, play music, fetch news, give reminders, and even talk to you using Gemini AI (Google).

---

#  Features

- 🗣 Voice-activated wake word: Just say **"Jarvis"**
- 🔍 Open popular websites like Google, YouTube, Facebook, etc.
- 🎵 Play music from a predefined library
- 📰 Fetch and read out top news headlines (via NewsAPI)
- 🧠 Get AI-generated answers from Google Gemini (Gemini 1.5 Flash)
- ⏰ Add tasks with time-based reminders (spoken alerts)
- 📅 Ask for current date & time

---

# How It Works

# Workflow:
1. Listens for the word "Jarvis" via microphone
2. Activates voice recognition and processes commands
3. Based on the command:
   - Opens websites
   - Plays music
   - Speaks time/date
   - Uses Gemini AI to generate answers
   - Saves tasks and speaks reminders

---

#Requirements

Install the following libraries in your virtual environment:

bash
pip install SpeechRecognition

pip install pyttsx3

pip install pygame

pip install gTTS

pip install requests

pip install google-generativeai


#FILE STRUCTURE:

jarvis-ai-assistant/

├── main.py            # Main assistant logic

├── client.py          # Gemini or OpenAI 
test script

├── musiclibrary.py    # Dictionary of song names to URLs

├── reminders.py       # (Optional) Separate logic for reminders

├── temp.mp3           # Temp file used for voice output

├── tasks.txt          # Stores reminder tasks


#API Keys Used
News API – for top headlines (newsapi.org)

Google Gemini API Key – for AI response generation

#Credits
Python libraries: speech_recognition, gtts, pygame, pyttsx3, requests

Gemini AI by Google

Inspired by the Iron Man movie AI
