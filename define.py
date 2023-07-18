"""#####################################################################
# @file    : define.py
# @author  : Ahmed Basem - Nader Mohamed - Mohamed Wesam - Alaa Yasser
# @version : 0.0.1
# @brief   : Ai voice assistant 
#####################################################################"""

"""####################### Library Files Start ######################"""
import pyttsx3 # take a text and convert it to voice
import speech_recognition as spRe
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import math
import numpy
import pandas
import matplotlib
"""######################## Library Files End ######################"""

"""###################### Global variable start ####################"""
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


"""####################### Global variable end #####################"""


"""##################### Function Define Start #####################"""
def speak(text):  #function that take text and convert it to voice
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def welcome():
    hour=int(datetime.datetime.now().hour)
   
    if hour>=0 and hour<12:
        speak("Good Morning , My Brother")
        print("Good Morning , My Brother")
    elif hour>=12 and hour<18:
        speak("Good Afternoon , My Brother")
        print("Good Afternoon , My Brother")
    else:
        speak("A Hot Night is Here , My Brother")
        print("A Hot Night is Here , My Brother")
    speak("I am Here , How Can I help you?")
    print("I am Here , How Can I help you?") 


def listenAr():  #It takes microphone input from the user and returns string output

    r = spRe.Recognizer()
    with spRe.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='ar-AR')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        listenAr()
    return query

def listenEn():  #It takes microphone input from the user and returns string output

    r = spRe.Recognizer()
    with spRe.Microphone() as source:
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
        listenEn()
    return query
"""##################### Function Define End #######################"""







"""
*****************************************************************************************************************
User                         Date                                Brief
*****************************************************************************************************************
Ahmed Basem                  18/7/23                             def fun speak
Ahmed Basem                  18/7/23                             def fun welcome
Ahmed Basem                  18/7/23                             def fun listen





"""
mytext = listenAr()
print(mytext)
