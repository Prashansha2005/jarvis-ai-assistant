import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclibrary
import requests
import google.generativeai as genai
import pygame
from gtts import gTTS
import os
import datetime
from time import sleep


newsapi = "2486c441f36a44df86c11827c46e38a6"

def speak_old(text):
    print("Speaking:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speak(text):
    

    from gtts import gTTS 

def speak(text):
    print("Speaking:", text)
    
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit() 

def tell_time():
    now = datetime.datetime.now().strftime("%H:%M")
    return now


def aiprocess(command):
    genai.configure(api_key="AIzaSyClmugZy06i0WS4PIpzw_P2NzIupFu53_s")
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # or "gemini-pro"

# Generate content
    response = model.generate_content(command)

# Print the response
    return response.text

TASK_FILE = "tasks.txt"
def show_tasks():
    if not os.path.exists(TASK_FILE):
        speak("No tasks yet.")
        return

    with open(TASK_FILE, "r") as file:
        tasks = file.readlines()
    if tasks:
        speak("Here are your tasks:")
        for line in tasks:
            task, time_str = line.strip().split("|")
            print(f" {task} at {time_str}")
            speak(f"{task} at {time_str}")
    else:
        speak("No tasks found.")

def add_task(task, time_str):
    with open(TASK_FILE, "a") as file:
        file.write(f"{task}|{time_str}\n")
    speak(f"Task added: {task} at {time_str}")

def remind_tasks():
    while True:
        now = datetime.now().strftime("%H:%M")
        if not os.path.exists(TASK_FILE):
            sleep(30)
            continue

        with open(TASK_FILE, "r") as file:
            lines = file.readlines()

        remaining = []
        for line in lines:
            task, time_str = line.strip().split("|")
            if now == time_str:
                speak(f"Reminder: {task}")
            else:
                remaining.append(line)

        # Update task file to keep only pending ones
        with open(TASK_FILE, "w") as file:
            file.writelines(remaining)

        sleep(60)

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split("play", 1)[1].strip()
        if song in musiclibrary.music:
            link = musiclibrary.music[song]
            webbrowser.open(link)
        else:
            speak(f"Sorry, {song} not found in your library.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            if not articles:
                speak("No news found right now.")
            for article in articles[:5]:
                speak(article['title'])
        else:
            speak("Sorry, I couldn't fetch the news.")

    elif "date and time" in c.lower():
        nom=tell_time()
        speak(f"the date and time is {nom}")

    elif "my task are" in c.lower()
    

    else:
        output=aiprocess(c)
        speak(output)

   

 


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    recognizer = sr.Recognizer()

    while True:
        print("Listening for 'Jarvis'...")

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)

            command = recognizer.recognize_google(audio).lower()
            print("Heard:", command)

            if "jarvis" in command:
                print("Jarvis wake word detected")
                speak("Yaa")

                with sr.Microphone() as source:
                    print("Jarvis active, listening for command...")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=5)

                command = recognizer.recognize_google(audio).lower()
                print("Final command:", command)
                processcommand(command)

        except sr.UnknownValueError:
            print("Didn't catch that. Try again.")
        except sr.WaitTimeoutError:
            print("Listening timed out.")
        except Exception as e:
            print(f"Error: {e}")


       
