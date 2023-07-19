"""#####################################################################
# @file    : main.py
# @author  : Ahmed Basem - Nader Mohamed - Mohamed Wesam - Alaa Yasser
# @version : 0.0.1
# @brief   : Ai voice assistant 
#####################################################################"""

"""####################### Library Files Start ######################"""
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib
import math
import numpy
import pandas
import matplotlib
import warnings
import wikipedia
import random
from define import *
import requests, json
"""######################## Library Files End ######################"""

"""##################### Function Define Start #####################"""
def google():
    speak("Google Opened")
    print("Google Opened")
    speak("What you need from Google")
    print("What you need from Google")
    googleSearch = listenAr()
    googleSearch = googleSearch.replace(" ","+")
    speak("Operation is Done")
    print("Operation is Done")
    url = "google.com/search?q="
    url = url + googleSearch
    webbrowser.open_new_tab(url)

def youtube():
    speak("Youtube Opened")
    print("Youtube Opened")
    speak("What you need from Youtube")
    print("What you need from Youtube")
    youtubeSearch = listenAr()
    youtubeSearch = youtubeSearch.replace(" ","+")
    speak("Operation is Done")
    print("Operation is Done")
    url = "youtube.com/search?q="
    url = url + youtubeSearch
    webbrowser.open_new_tab(url)

def facebook():
    speak("You seem to be a fan of Mark Zuckerberg, however, Facebook is open")
    print("You seem to be a fan of Mark Zuckerberg, however, Facebook is open")
    url = "www.facebook.com"
    webbrowser.open_new(url)

def vs_code():
    speak("Vs code ? hmmmm , You look like a Programmer")
    print("Vs code ? hmmmm , You look like a Programmer")
    speak("Vs code is open")
    print("Vs code is open")
    codePath = "C:\\Users\\ahmed\\AppData\\Local\\WhatsApp\\app-2.2310.5\\WhatsApp.exe"
    os.startfile(codePath)


def time_now():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak(f"Sir, the time is {strTime}")
    print(f"Sir, the time is {strTime}")

def date_now():
    strTime = datetime.date.today()
    speak(f"Sir, the time is {strTime}")
    print(f"Sir, the time is {strTime}")

def ece_drive():
    speak("ohhh yaa , you are from e c e 2026 , you are lucky , however , drive is open")
    print("ohhhhhh ya , you are from ece 2026 , you are lucky , however , drive is open")
    url = "https://drive.google.com/drive/folders/13NMDUoI4rid0KJYlIfAeeC-RExtsFJFR"
    webbrowser.open_new_tab(url)

def developers():
    speak("This Program is developed By 4 student In Ece department")
    print("This Program is developed By 4 student In Ece department")


def ece_channel():
    speak("You seem to be a fan of abdelrahman Asem records, however, channel is open")
    print("You seem to be a fan of abdelrahman Asem records, however, channel is open")
    url = "https://www.youtube.com/@ECE-2026"
    webbrowser.open_new(url)

def discord():
    speak("Discord ? hmmmm , You look like a Gamer")
    print("Discord ? hmmmm , You look like a Gamer")
    speak("You need Application Or Website")
    print("You need Application Or Website")
    respond = listenEn()
    if "application" in respond.lower() :
        codePath = "C:\\Users\\ahmed\\AppData\\Local\\Discord\\app-1.0.9015\\Discord.exe"
        os.startfile(codePath)
    elif "website" in respond.lower() :
        url = "https://www.discord.com"
        webbrowser.open_new(url)
    else : 
        speak("Unknown choose , sorry about this error")
        print("Unknown choose , sorry about this error")


def whatsapp() : 
    speak("Whatsapp ? hmmmm , You will talk to the crush ? , You seem naughty")
    print("Whatsapp ? hmmmm , You will talk to the crush ? , You seem naughty")
    speak("You need Application Or Website")
    print("You need Application Or Website")
    respond = listenEn()
    if "application" in respond.lower() :
        codePath = "C:\\Users\\ahmed\\AppData\\Local\\WhatsApp\\app-2.2310.5\\WhatsApp.exe"
        os.startfile(codePath)
    elif "website" in respond.lower() :
        url = "https://web.whatsapp.com/"
        webbrowser.open_new(url)
    else : 
        speak("Unknown choose , sorry about this error")
        print("Unknown choose , sorry about this error")

def linkedin():
    speak("linkedin hmmmmmmm ? , you search about A job")
    print("linkedin hmmmmmmm ? , you search about A job")
    speak("operation Done!")
    print("operation Done!")
    url = "https://www.linkedin.com/feed/"
    webbrowser.open_new(url)
    
def wikipedia():
    speak("ًWikipedia Opened")
    print("Wikipedia Opened")
    speak("What you need from Wikipedia")
    print("What you need from Wikipedia")
    value = listenEn()
    value = value.replace(" ","")
    import wikipedia
    import random
    import warnings
    warnings.filterwarnings("ignore")
    try:
        m = wikipedia.search(value, 3)
        speak(wikipedia.summary(m[0], sentences=2))
        print(wikipedia.summary(m[0], sentences=2))
    except wikipedia.exceptions.DisambiguationError as e:
        s = random.choice(e.options)
        p = wikipedia.summary(s, sentences=2)
        print(p) 
def joke():
    speak("I am an artificial intelligence program that is not intended for laughter my Naughty . Nevertheless, I will tell you a joke that will make you laugh for the next year")
    print("I am an artificial intelligence program that is not intended for laughter my Naughty . Nevertheless, I will tell you a joke that will make you laugh for the next year")
    num = int(random.randint(0,8))
    if num == 0 :
        speak("why is six sacred seven ?")
        print("why is six sacred seven ?")
        speak("Because seven eghit nine Hahahahahahahahahahahahahaha")
        print("Because seven eghit nine")
    elif num == 1 :
        speak("Why do we tell actors to “break a leg?”")
        print("Why do we tell actors to “break a leg?”")
        speak("Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor. Hahahahahahahahahahahahahaha")
        print("Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor.")
    elif num == 2 :
        speak("Why don't skeletons fight each other?")
        print("Why don't skeletons fight each other?")
        speak("They don't have the guts! , Hahahahahahahahahahahaha")
        print("They don't have the guts!")
    elif num == 3 :
        speak("Why did the scarecrow win an award?")
        print("Why did the scarecrow win an award?")
        speak("Because he was outstanding in his field! , Hahahahahahahahahahahaha")
        print("Because he was outstanding in his field!")
    elif num == 4 :
        speak("How do you organize a space party?")
        print("How do you organize a space party?")
        speak("You planet! , Hahahahahahahahahahahaha")
        print("You planet!")
    elif num == 5 :
        speak("Why don't eggs tell jokes?")
        print("Why don't eggs tell jokes?")
        speak("Because they might crack up! , Hahahahahahahahahahahaha")
        print("Because they might crack up!")
    elif num == 6 :
        speak("Why did the tomato turn red?")
        print("Why did the tomato turn red?")
        speak("Because it saw the salad dressing! , Hahahahahahahahahahahaha")
        print("Because it saw the salad dressing!")
    elif num == 7 :
        speak("What do you call a snowman with a six-pack?")
        print("What do you call a snowman with a six-pack?")
        speak("An abdominal snowman! , Hahahahahahahahahahahaha")
        print("An abdominal snowman!")
    elif num == 8 :
        speak("What do you Call Someone with No Body and No Nose?")
        print("What do you Call Someone with No Body and No Nose?")
        speak("Nobody Nose! , Hahahahahahahahahahahaha")
        print("Nobody Nose!")

def chatGpt():
    speak("Chat Gpt is open")
    print("Chat Gpt is open")
    speak("What do You Need from Gpt ?")
    print("What do You Need from Gpt ?")
    user_input = listenEn()
    user_input = user_input.strip()
    while True:
        if user_input.lower() == 'bye':
            speak("Goodbye!")
            print("Bot: Goodbye!")
            break
        response = chat_with_gpt(user_input)
        speak(response)
        print("Bot:", response)
        user_input = listenEn()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()     

def playMusic() :
    songs_dir=r"C:\\Users\\ahmed\\Downloads\\Music"
    songs=os.listdir(songs_dir)
    ra = random.randint(0,coun())
    os.startfile(os.path.join(songs_dir,songs[ra]))    

def weather():
    api_key = "2493d2dbe14bd976436c91a8d6757ff3"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = listenEn()
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_temperature = current_temperature - 273
        current_temperature = int(current_temperature)
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak(" Temperature = " +
                        str(current_temperature) + "celsius" +
            "\n atmospheric pressure = " +
                        str(current_pressure) + "Hpa" +
            "\n description = " +
                        str(weather_description))
        print(" Temperature = " +
                        str(current_temperature) + "celsius" +
            "\n atmospheric pressure = " +
                        str(current_pressure) + "Hpa" +
            "\n description = " +
                        str(weather_description))
    else:
        speak(" City Not Found ")
        print(" City Not Found ")



"""##################### Function Define End #######################"""



"""
*****************************************************************************************************************
User                         Date                                Brief
*****************************************************************************************************************

"""

weather()
