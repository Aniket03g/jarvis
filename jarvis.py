import pyttsx3
import speech_recognition as sr
import datetime
import os
import cs2
import random
from requests import get
import wikipedia
import  webbrowser
import pywhatkit as kit
import smtplib
import sys

engine = pyttsx3.init('sap15')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voies', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Recognizer() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#To wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir, please tell me how can i help you.")

#To send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('absol9506@gmail.com','Absoabso@0303')
    server.sendmail('absol9506@gmail.com', to, content)
    server.close()


if --name-- == "==main--":
    wish()
    while True:
    #if 1:

        query = takecommand().lower()

        #Logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open command promt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "directory de"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                     os.startfile(os.path.join(music_dir, song))



        elif "ip address" in query:
            ip = get('https://api.ipfy.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f{cm})

        elif "send message" in query:
            kit.sendwhatmsg("+917744872443", "this is testing protocol"time?)


        elif "play song on youtube" in query:
            kit.playonyt("see you again")

        elif "email to aniket" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to ="absol9506@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to aniket")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send the email")


        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()