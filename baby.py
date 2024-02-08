from googletrans import Translated
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import googletrans
import sys
import smtplib
import requests
import pywhatkit as kit
import pyjokes
import playsound
import datetime
import pyowm
import pyautogui as pg 
import time
#addd of modules not done importpacakgeas ""
import PyPDF2
#import subprocess
import clipboard
import pyperclip
import random
import psutil
import urllib.request
import cv2
import numpy as np #pip install numpy
#from speedtest import Speedtest
from pytube import YouTube
from bs4 import BeautifulSoup
import pywikihow

import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from time import sleep


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)


city="pune"


MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october", "november", "december"]
DAYS =["sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]





def speak(audio):
    engine.say(audio)
    engine.runAndWait()







def wishMe():
   # play()
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("hello i'm baby, how can i help u ?")       

def takeCommand():
    #It takes microphone input from the user and returns string output
    if 1:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...") 
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            
            

        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            return "None"
        return query

def get_date(query):
    query = query.lower()
    today = datetime.date.today()

    if query.count("today") > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in query.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    if month < today.month and month != -1:  
        year = year+1

    if month == -1 and day != -1:  
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if query.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    if day != -1:  
        return datetime.date(month=month, day=day, year=year)


def pdf():
    speak("sir! please type extension of exe location")
    aaa = input("")
    book = open('aaa', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book) #pip install PyPDF2
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages} ")
    speak("sir please enter the page number i have to read")
    speak("Please tell me  the page number: ")
    pg= int(takeCommand())
    speaker = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
      # print(voices[1].id)
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 160-170)
    for num in range(pg, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()


def locate(query):
    query=query.split("locate")
    place=query[1]
    speak(f"according to my data base {place} lies here")
    webbrowser.open_new_tab("https://www.google.com/maps?q=maps+"+place)

def note(query):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(query)

    subprocess.Popen(["notepad.exe", file_name])

def news():
    main_url= 'http://news.api.org/v2/top-headlines?sources-techcrunch&apiKey=83263a48521a48a797182dbc3926e513'
    main_page= requests.get(main_url).json()
        #print (main_page)
    articles = main_page["articls"];
    print (articles)
    head = []
    day=["first", "second", "third", "fourth", "fifth", "sixth","seventh", "eighth", "ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)): 
        #print("today's (day[$]) news is: head[$]) 
        speak(f"today's {day[1]} news is: {head[i]}")

    
def weather_info():
    global city
    owm=pyowm.OWM('enter your api key')
    location=owm.weather_at_place(f'{city}')
    weather=location.get_weather()
    temp=weather.get_temperature('celsius')
    humidity=weather.get_humidity()
    date=datetime.datetime.now().strftime("%A:%d:%B:%Y")
    current_temp=temp['temp']
    maximum_temp=temp['temp_max']
    min_temp=temp['temp_min']
    speak(f'The current temperature on {city} is {current_temp} degree celsius ')
    speak(f'The estimated maximum temperature for today {date} on {city} is {maximum_temp} degree celcius')
    speak(f'The estimated minimum temperature for today {date} on {city} is {min_temp} degree celcius')
    speak(f'The air is {humidity}% humid today')

def weather_at_place(city):
    owm=pyowm.OWM('enter your api key')
    location=owm.weather_at_place(f'{city}')
    weather=location.get_weather()
    temp=weather.get_temperature('celsius')
    humidity=weather.get_humidity()
    date=datetime.datetime.now().strftime("%A:%d:%B:%Y")
    current_temp=temp['temp']
    maximum_temp=temp['temp_max']
    min_temp=temp['temp_min']
    speak(f'The current temperature on {city} is {current_temp} degree celsius ')
    speak(f'The estimated maximum temperature for today {date} on {city} is {maximum_temp} degree celcius')
    speak(f'The estimated minimum temperature for today {date} on {city} is {min_temp} degree celcius')
    speak(f'The air is {humidity}% humid today on {city}')



def read():
    pg.hotkey("ctrl",'c')
    tobespoken=pyperclip.paste()
    speak(tobespoken)

def openafile(query):
    query=query.split("play")
    speak(f"searching for {query[1]} in my database")
    dir_path = os.path.dirname(os.path.realpath(__file__)) 
            
    try:
        for root,dirs,files in os.walk("D:\\movie\\song"):
             for file in files:
                file_name=query[1]
                if file.startswith(file_name):
                    path= "C:"+'\\'+str(file) 
                    speak(f"opening {file_name}")
                    os.startfile(path)
    except:
        speak(f"no music named: {file_name}")


def trans():
    speak("Give input language ")
    hq = takeCommand().lower()
    speak(" give output_lang")
    ha = takeCommand().lower()
    input_lang = hq
    output_lang = ha
    translator = googletrans.Translator()
    try:
        r = sr.Recognizer
        with sr.Microphone() as source:
            print('Speak Now')
            voice = r.listen(source)
            text = r.recognize_google(voice, language=input_lang)
            print(text)
    except :
        pass  

    translated = translator.translate(text, dest=output_lang )
    print(translated.text)
    speak(translated.text)




        

#def hero():
#    r = sr.Recognizer()
#    with sr.Microphone() as source:
#        print("Listening...")
#        r.pause_threshold = 1
#        audio = r.listen(source)
#
#    try:
#        print("Recognizing...")    
#        query = r.recognize_google(audio, language='en-in')
#        print(f"User said: {query}\n")
#
#    except Exception as e:
#        # print(e)    
#        print("Say that again please...")  
#        return "None"
#    return query

from playsound import playsound

def play():
    playsound('C:\\New folder\\baby\\Up.wav') 


def window():
    app = QtWidgets.QApplication (sys.argv)
    Form = QtWidgets.QWidget() 
    Form.resize(540,600)
    Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    label = QtWidgets.QLabel(Form)
    label.setGeometry(QtCore.QRect(10, 15, 840, 550))
    movie1 = QtGui.QMovie('abcd.gif')
    label.setMovie(movie1) 
    movie1.start()
    Form.show()
    sys.exit(app.exec_())



def main():
    start = takeCommand().lower()
    if 'hi baby' in start or 'hey baby' in start:
        
        #playsound("c")
      #  os.startfile("C:\\New folder\\rainmeter\\Rainmeter.exe")  
        wishMe()
        while True:
            query = takeCommand().lower()
            
            
            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'baby kaisa hai'in query:
                pass

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open chrome' in query:
                cc = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(cc)
                sleep(4)
                while 1:
                    s = takeCommand()
                    if 'search' in s:
                        pg.press('ctrl','l')
                        sleep(1)
                        pg.typewrite(takeCommand())

            

            elif 'search on google' in query:
                query = query.replace('search on google','')
                webbrowser.open("https://www.google.co.in/search?q=" +query)

            elif 'website' in query:
                speak("ok sir, launching....")
                query = query.replace('baby','')
                hhh= query.replace('website','')
                query = hhh.replace('open','')
                webbrowser.open(f"https://www.{query}.com")

            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")  
              
            elif 'whatsapp web' in query:
                webbrowser.open("web.whatsapp.com") 
             
            elif 'open amazon' in query:
                webbrowser.open("amazon.in")  
         
            elif 'open flipkart' in query:
                webbrowser.open("flipkart.com")  
             
            elif 'amazon' in query:
                webbrowser.open("amazon.in")  
            
            
            elif 'play music' in query:
                from music import music1
                music1()

 
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codePath = "C:\\New Folder\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'close code' in query:
                speak("ok sir closing notepad")
                ab = "Microsoft VS Code\\Code.exe"
                os.system("taskkill /f /im" + ab)
                
            elif 'read pfd' in query:
                import pdfread
                pdfread.read()
                # read()
            elif 'close' in query:
                pg.press('ctrl','f4')

            elif 'open settings' in query or 'setting' in query:
                pg.press('wi','i')

            elif 'minimize' in query:
                pg.press('wi','m')

            elif 'lock' in query:
                pg.pres('wi','l')

            elif 'open search' in query:
                pg.press('wi',s)


            elif 'email to me' in query:
                from mmail import mail
                mail() 
                
            elif 'translate' in query:
                speak("yes,sir!")
                translator = googletrans.Translator()
                trans()

            elif 'download' in query:
                #from pytube import youtube AND PYTUBE3
                from you import dow
                dow()
                

            elif "open camera" in query:
                import cam
                cam.open()
          
            elif "close camera" in query:
                pg.press('esc')


            elif 'send WhatsApp message' in query:
                from whatappp import send
                send()
               

            elif  "search on youtube" in query : 
                query = query.replace('search on youtube',"")
                #query = query.replace('play',"")
                kit.playonyt(query)

            elif "play" in query and "on youtube" in query:
                from you import play
                play(query)

            elif 'stop playing' in query:
                pg.press('space')

            elif 'pause' in query:
                pg.press('pause')

            elif 'enter' in query:
                pg.press('enter')
                    
            elif 'full screen' in query:
                pg.press('f')
                
            elif 'back' in query:
                pg.press('j')
                    
            elif 'minimise' in query:
                pg.hotkey('win','d')
                
            elif 'open new tab' in query:
                pg.hotkey('ctrl','t')
            
            elif 'news' in query:
                news()

            elif 'exit' in query:
                sys.exit()
                break

            elif 'temperatue' in query:
                import temp
                temp.temperature(query)      
            
            elif 'chatbot mode' in query:
                from bootmode import boot
                boot()

            elif 'find my location' in query or 'where am i' in query:
                from location import find
                find()

            elif 'open notepad' in query:
                speak("opening notepad")
                os.system("start notepad")
            

            elif 'close notepad' in query:
                speak("ok sir closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif 'set alarm' in query:
                from set import alarm
                alarm()

            elif 'tell me a joke' in query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif 'tell me some more jokes' in query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif 'close all tabs' in query:
                speak("ok sir closing notepad")
                os.system("taskkill /f /im ")

            
            elif 'close browser' in query or 'close chrome' in query:
                speak("ok sir closing notepad")
                os.system("taskkill /f /im chrome.exe")
            elif 'kill browser' in query or 'close edge' in query:
                speak("ok sir closing notepad")
                os.system("taskkill /f /im Microsoft edge.exe")


            elif 'open the book' in query or 'open pdf' in query:
                pdf()

            elif 'internet speed' in query:
                from speed import test
                test()
            
            elif "how much power left" in query or "how much power we have" in query or "battery" in query:
                from bettery import per
                per()

            elif "how are you" in query or "how are you felling" in query:
                from bettery import feel
                feel()
            
            elif "do some calculations" in query or "can you calculate" in query:
                from claculation import cal
                cal()

            elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
                from hide import file
                file()

            elif "good morning" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                speak(f"Good morning master it is {strTime} now,Hope you had a good day.")

            elif "good night" in query:
                strTime = datetime.datetime.now().strftime("%X").replace(":"," ") 
                gtime=strTime.replace(":"," ") 
                speak(f"Good night master it is {gtime} sleep tight..")

            elif "open my inbox" in query:
                webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")

            elif "open my sent mail" in query:
                webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#sent")

            elif "Thank you" in query or "thank you" in query or "thanks" in query:
                
                rep= ['Welcome','Well you know Aaryan im cool','Dont mention','By the way I should thank you for creating me']
                speak(random.choice(rep))

            elif"say something" in query:
                speak("what's your name?")

            elif "who created you" in query:
                speak("Abhishek vishwakarma is creater ....")

            elif "who made you" in query:
                speak("I was created by Abhishek Vishwakarma")  
      
            elif "how were you developed" in query:
                speak("Sorry boss  I am not allowed to reveval all my secrets  ")

            elif "which language " in query:
                speak("i have been created under python language only ")

            elif "show me your code" in query:
                speak("Sorry boss  I am not allowed to reveval all of my secrets  ")

            elif "tell me a joke" in query or "Crack a joke" in query or "crack a joke" in query:
                jokes =["A Doctor said to a patient , I'm sorry but you suffer from a terminal illness and have only 10 to live , then the Patient said What do you mean, 10, 10 what, Months, Weeks, and the Doctor said Nine.","Once my Brother who never used to drink was arrested for over drinking,When I lates had gone and asked him why were you arressted, He replied he had not brushed since a week","A Teacher said Kids, what does the chicken give you? The Student replied Meat Teacher said  Very good Now what does the pig give you? Student said BaconTeacher said  Great  And what does the fat cow give you? Student said Homework!","A child asked his father, How were people born? So his father said, Adam and Eve made babies, then their babies became adults and made babies, and so on  The child then went to his mother, asked her the same question and she told him, We were monkeys then we evolved to become like we are now  The child ran back to his father and said, You lied to me  His father replied, No, your mom was talking about her side of the family."]
                speak(random.choice(jokes))
                speak("Do you want more?")
                ans=takeCommand().lower()
                if "yes" in ans:
                    speak(random.choice(jokes))
                else:
                    return None
            
            elif "what is today's date" in query:
                date=datetime.datetime.now().strftime("%A:%d:%B:%Y")
                speak(f"Today is {date} ")        
        
            elif "weather out" in query or 'weather in pune' in query:
                weather_info()

            elif "weather in" in query:
                qy=query.split("weather in")
                city=qy[1]
                weather_at_place(city)  

            elif 'screenshot' in query:
                from cam import screenshot
                screenshot()
                
            elif "locate" in query:
                locate(query)
            
            elif "make a note" in query or "write this down"  in query or "remember this" in query:
                NOTE_STRS = ["make a note", "write this down", "remember this"]
                for phrase in NOTE_STRS:
                    if phrase in query:
                        speak("What would you like me to write down? ")
                        write_down = takeCommand()
                        note(write_down)
                        speak("I've made a note of that.")
                        #supprocess is stilll not install
                

            elif "introduce yourself" in query or "give your info" in query:
                speak("Okay,Let me start by The time I was born,,")
                speak("I was a dream of a boy dreaming to make a perfect virtual assistant")
                speak("He soon established the company named with my name")
                speak("Slowly,I came to life")
                speak("I started learning various things like calculations,General knowldge etc etc")
                speak("Now I am capable of doing various things like Beatboxing,opening applications,Cracking jokes,Playing music etc.")
                speak("Okay,thats a wrap I wont say more ")
                    
            elif "type" in query:
                speak("okay i am listening speak")
                pg.typewrite(takeCommand())

            elif "select all" in query:
                pg.hotkey('ctrl','a')

            elif "close this window" in query:
                pg.hotkey('alt','f4')

            elif "open a new tab" in query:
                pg.hotkey('ctrl','n')
 
            elif "open a new window" in query:
                pg.hotkey('ctrl','shift','n')

            elif "copy" in query:
                pg.hotkey('ctrl','c')
                speak('text copied to clipboard')

            elif "paste" in query:
                pg.hotkey('ctrl','v')

            elif "undo" in query:
                pg.hotkey('ctrl','z')

            elif "redo" in query:
                pg.hotkey('ctrl','x')

            elif "save" in query:
                pg.hotkey('ctrl','s')

            elif "back" in query:
                pg.hotkey('browserback')

            elif "go up" in query:
                pg.hotkey('pageup') 

            elif "go to top" in query:
                pg.hotkey('home')
            
            elif "volume mute" in query: 
                pg.press("volumemute")
            
            elif "volume down" in query:  
                pg.press("volumedown")

            elif "volume up" in query:  
                pg.press("volumeup")


            elif "delete" in query:
                final=query.split("delete")
                os.system("del "+final[1])

            elif "shutdown" in query:
                speak("okay,shutting down your pc")
                os.system('shutdown / s / t /5')

            elif "restart my pc" in query:
                speak("okay, restarting your pc")
                os.system('shutdown /r /t 5')

            elif "sleep the system" in query:
                os.system("rundll32.exe powrprof.dill,SetSuspendedState 0,1,0")

            elif "where is" in query:
                query=query.split("where is")
                locate(query)
                
            elif "read" in query:
                try:
                    read()
                except:
                    speak("no text selected plz select a text")

            elif "I know that" in query:
                speak("Ya, ure right")
                        
            elif "play song" in query:
  
                a = os.listdir("D:\\movie\\song")
                d = random.choise(a)
                o.startfile(d)
                from playsound import playsound

               # openafile(query)

            elif "type" in query:
                speak(f"okay i am listening speak")
                pg.typewrite(takeCommand())
                
            elif "open mobile camera" in query:
                from cam import mobile
                mobile()
                












          

            elif "date" in query:
                get_date(query)                                           
                                     
            elif 'who' in query or 'which' in query:
                from how import who
                who(query)

            elif 'what is' in query:
                from how import what
                what(query)

            elif "how to" in query:
                from how import to
                to(query)
        
        

        




if __name__ == "__main__":
    while True:
        #putting jarvis in infinite loop
        main()