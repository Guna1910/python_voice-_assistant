

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyowm
import sys
from googletrans import Translator
translator=Translator()

master="goutham"

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
#speaks what you passed
def speak(text):
	engine.say(text)
	engine.runAndWait()

def wish():
        hour=int(datetime.datetime.now().hour)
        print(hour)

        if hour>0 and hour<12:
                speak(" good Morning" + master)
        elif hour>=12 and hour<18:
                speak(" good Afternoon" + master)
        else:
                speak(" good Evening" + master)

        speak(" How may i help you")  

def takeCommand():
        r=sr.Recognizer()
        with sr.Microphone() as source:
                #print(" Listening...")
               # audio=r.listen(source)
                print("Say something!")
                audio = r.listen(source,timeout=1,phrase_time_limit=5)
        try :
                print(" taking input")
                query=r.recognize_google(audio,language="en-in")
                print("user said {} ".format(query))
        except Exception as e:
                print(" I did not get you please speak again")
                query="None"
                
                
        return query


def weather():
        owm = pyowm.OWM('2cc80bfc1e12ce8b99cb8e33a5341148')
        city = 'Vijayawada'
        loc = owm.weather_manager().weather_at_place(city)
        weather = loc.weather
        # temperature
        temp = weather.temperature(unit='celsius')
        speak("The Temperature outside is")
        speak(temp["temp"])

def translated(text):
        if(text=="none"):
                speak(" Say Something")
                
                
        translated_sentence=translator.translate(text,src='en',dest='te')
        speak(translated_sentence.text)
        print(translated_sentence.text)
        
#speak("Say Something")
wish()
while True:
        query=takeCommand()
        if  "wikipedia" in query.lower():
                speak("searching in wikipedia")
                query=query.replace("wikipedia"," ")
                results=wikipedia.summary(query,sentences=2)
                speak(results)
        elif  "open youtube" in query.lower():
                url="youtube.com"
                chrome_path= "c:/Users/Lenovo/AppData/Local/Google/Chrome/Application/chrome.exe %s"
                speak("Opening Youtube")
                webbrowser.get(chrome_path).open(url)  
                
        elif  "amazon music" in query.lower():
                url="music.amazon.in/home"
                chrome_path= "c:/Users/Lenovo/AppData/Local/Google/Chrome/Application/chrome.exe %s"
                speak("Opening Amazon Music")
                webbrowser.get(chrome_path).open(url)
                
        elif  "meeting"  in query.lower():
                url="meet.google.com/zhm-aiss-hay"
                chrome_path= "c:/Users/Lenovo/AppData/Local/Google/Chrome/Application/chrome.exe %s"
                speak("opening Cse meeting Get ready")
                webbrowser.get(chrome_path).open(url)
        elif  "google meet" in query.lower():
                url="meet.google.com"
                chrome_path= "c:/Users/Lenovo/AppData/Local/Google/Chrome/Application/chrome.exe %s"
                speak("Opening Google meet")
                webbrowser.get(chrome_path).open(url)
        elif  "time" in query.lower():
                time=datetime.datetime.now().strftime(" %H:%M")
                speak(f"{master} the time is {time}")
        elif  "mail" in query.lower():
                url="mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"
                chrome_path= "c:/Users/Lenovo/AppData/Local/Google/Chrome/Application/chrome.exe %s"
                speak("Opening  Gmail")
                webbrowser.get(chrome_path).open(url)
        elif "whatsapp" in query.lower():
                url="web.whatsapp.com"
                chrome_path= "c:/Users/Lenovo/AppData/Local/Google/Chrome/Application/chrome.exe %s"
                speak("Opening  Whatsapp")
                webbrowser.get(chrome_path).open(url)
        elif  "weather" in query.lower():
                weather()
        elif  "search" in query.lower():
                speak("searching in google")
                query=query.replace("google"," ")
                url="google.com/?#q="+query
                chrome_path= "c:/Users/Lenovo/AppData/Local/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open(url)
        elif "translate" or "convert" in query.lower():
                query=query.replace("translate","")
                query=query.replace("convert","")
                translated(query)
        elif  "bye" or "exit" in query.lower():
                speak("Bye ....!")
                sys.exit()
                

        
                
                
        
                



        



        



