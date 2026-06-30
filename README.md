# jarvis-ai-assistant

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
## Technologies Used

- Python
- SpeechRecognition
- Google Gemini API
- gTTS
- pygame
- requests
- NewsAPI

  
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


## Limitations

- Speech recognition accuracy depends on microphone quality.
- Internet connection is required for Gemini API and News API.
- Currently supports a predefined music library.

  ## Future Improvements

- GUI interface
- Better speech recognition
- Weather integration
- Dynamic music search
- Chat history
  
Inspired by the Iron Man movie AI
