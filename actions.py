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
import wikipedia
import webbrowser
import os
import smtplib
import math
import numpy
import pandas
import matplotlib
from define import *
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
    pass

def date_now():
    pass

def ece_drive():
    speak("ohhh yaa , you are from e c e 2026 , you are lucky , however , drive is open")
    print("ohhhhhh ya , you are from ece 2026 , you are lucky , however , drive is open")
    url = "https://drive.google.com/drive/folders/13NMDUoI4rid0KJYlIfAeeC-RExtsFJFR"
    webbrowser.open_new_tab(url)

def developers():
    pass

def ece_channel():
    speak("You seem to be a fan of abdelrahman Asem records, however, channel is open")
    print("You seem to be a fan of abdelrahman Asem records, however, channel is open")
    url = "https://www.youtube.com/@ECE-2026"
    webbrowser.open_new(url)

def discord():
    speak("Discord ? hmmmm , You look like a Gamer")
    print("Discord ? hmmmm , You look like a Gamer")
    speak("Ypu need Application Or Website")
    print("Ypu need Application Or Website")
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

def searchInChatGpt():
    pass

def whatsapp() : 
    speak("Whatsapp ? hmmmm , You will talk to the crush ? , You seem naughty")
    print("Whatsapp ? hmmmm , You will talk to the crush ? , You seem naughty")
    speak("Ypu need Application Or Website")
    print("Ypu need Application Or Website")
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

"""##################### Function Define End #######################"""



"""
*****************************************************************************************************************
User                         Date                                Brief
*****************************************************************************************************************



"""

