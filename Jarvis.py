import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):

    # This function will allow Jarvis to speak
    engine.say(audio)
    engine.runAndWait()

def wishMe():

    # This function wishes the user as soon as the program runs
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello! I am Jarvis! Please tell me how may I help you?")

def takeCommand():

    # This function takes input from the microphone of the user and returns the string output 

    # Here the sound is in variable audio and it is converted to the string after recognizing it and stored in the string query 
    r = sr.Recognizer()

    # Listen to the input audio
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        # r.energy_threshold = 400
        audio = r.listen(source)

    # Recognise the input audio
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please....")
        return "None"

    return query

def sendEmail (to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login ( 'email id of sender', 'password of the sender')
    server.sendmail('email id of sender', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        # Logic for executing taskes based on query

        if 'wikipedia' in query:
        
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'gmail' in query:
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Devearsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'please send an email' in query:
            try:  
                speak("What should I say?")
                content = takeCommand()
                to = "email id of reciever"
                sendEmail (to, content)
                speak('The Email has been sent succesfully!')

            except Exception as e:
                print(e)
                speak('Sorry! The email has not been sent..')

        elif 'quit' in query:
            speak("Thank you! Have a great day!")
            exit()