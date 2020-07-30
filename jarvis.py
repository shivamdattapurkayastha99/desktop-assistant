import pyttsx3

import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour==0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("happy fathers day community hall er   vice president")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold=1
        r.energy_threshold=500
        audio=r.listen(source)
    try:
            print("recognizing..")
            query=r.recognize_google(audio,language='en-in')
            print(f"user said: {query}\n")
    except Exception as e:
            # print(e)
            print("say that again please")
            return "none"
    return query
# def email(to,content):
#     server=smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('dattaprasanta16@gmail.com','password')
#     server.sendemail('dattaprasanta16@gmail.com',to,content)
#     server.close()






if __name__=="__main__":
    wishme()
    while True:
           takeCommand().lower()
           if 'wikipedia' in query:
               speak("searching wikipedia")
               query=query.replace("wikipedia","")
               results=wikipedia.summary(query,sentences=2)
               speak("according to wikipedia")
               speak(results)
           elif 'open youtube' in query:
               webbrowser.open("youtube.com")
           elif 'open google' in query:
               webbrowser.open("google.com")
           elif 'the time' in query:
               strTime=datetime.datetime.now().strftime("%H:%M:%S")
               speak(f"the time is {strTime}")
        #    elif 'mail' in query:
        #        try:
        #            speak("what should i do")
        #            content=takeCommand()
        #            to="shivamdatta465@gmail.com"
        #            sendemail(to,content)
        #            speak("email has been sent")
        #        except Exception as e:
        #            print(e)
        #            print("not able to send email")
            

            
           



