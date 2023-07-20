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
from define import *
from actions import *
"""######################## Library Files End ######################"""


"""##################### Function Define Start #####################"""

"""##################### Function Define End #######################"""

# speak("Hello my Friend,I am Basem")
# welcome()

UserOrder = listenEn()
UserOrder = UserOrder.lower()

if "youtube" in UserOrder :
    youtube()
elif "google" in UserOrder :
    google()    
elif "facebook" in UserOrder :
    facebook()
elif "discord" in UserOrder :
    discord()
elif "code" in UserOrder :
    vs_code()
elif "time" in UserOrder :
    time_now()
elif "date" in UserOrder :
    date_now()
elif "ece drive" in UserOrder :
    ece_drive()
elif "ece channel" in UserOrder :
    ece_channel()
elif "developers" in UserOrder :
    developers()
elif "linkedin" in UserOrder :
    linkedin()
elif "wikipedia" in UserOrder :
    wikipedia()
elif "joke" in UserOrder :
    joke()
elif ("gbt" or "chat") in UserOrder :
    chatGpt()
elif ("whatsapp" or 'whats') in UserOrder :
    whatsapp()
elif "music" in UserOrder :
    playMusic()
elif ("temperature" or "weather") in UserOrder :
    weather()
else : 
    speak("sorry about that , but this feature is not here now")
    print("sorry about that , but this feature is not here now")




"""
*****************************************************************************************************************
User                         Date                                Brief
*****************************************************************************************************************





"""
