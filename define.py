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
import webbrowser
import os
import smtplib
import math
import numpy
import pandas
import matplotlib
import openai
import google.generativeai as palm
import requests, json
import random
import gtts
from tempfile import NamedTemporaryFile
import pygame
import pprint
"""######################## Library Files End ######################"""
def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))
"""###################### Global variable start ####################"""
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 150) 
openai.api_key = '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'
palm.configure(api_key='YOUR_API_KEY')


"""####################### Global variable end #####################"""

"""##################### Function Define Start #####################"""
def speakEn(text):  #function that take text and convert it to voice
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listenEn():  #It takes microphone input from the user and returns string output

    r = spRe.Recognizer()
    with spRe.Microphone() as source:
        print(" Listening... ".center(110, "="))
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(" Recognizing... ".center(110, "="))    
        query = r.recognize_google(audio, language="en-in")
        print(f" User said: {query}\n ")

    except Exception as e:
        print(" Say that again please... ".center(110, "="))  
        listenEn()
    return query
print("=" * 110)
speakEn("Hello my Friend,I am basem")
speakEn("Before starting with You Please Choose which langauge you Want me to continue")
print(" Before starting with You Please Choose which langauge you Want me to continue ".center(110 , "="))
print(" For Arabic say arabic -- For English say english ".center(110, "="))
progLang1 = str(listenEn()).lower()
progLang = progLang1
if "english" in progLang :
    progLang = "en"
else :
    progLang = "ar"

def speak(text, lang=progLang, speed=2.0):
    output_folder = os.path.expanduser("~/JarvisOutput")
    os.makedirs(output_folder, exist_ok=True)

    with NamedTemporaryFile(delete=False) as output_file:
        tts = gtts.gTTS(text, lang=lang, slow=False)
        tts.save(output_file.name)
        output_file.seek(0)
    pygame.init()
    pygame.mixer.init()
    # Load the sound file into a Sound object
    sound = pygame.mixer.Sound(output_file.name)
    # Set the playback speed
    sound.set_volume(2.0)
    # Play the sound with speed adjustment
    channel = sound.play()
    if channel is not None:
        channel.set_endevent(pygame.USEREVENT)
        is_playing = True
        while is_playing:
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    is_playing = False
                    break
            pygame.time.Clock().tick(10)

        # Unload the music file and give the system a moment to release the file
    pygame.mixer.quit()
    pygame.time.wait(500)

    # Delete the temporary file manually
    os.remove(output_file.name)
def listen():  #It takes microphone input from the user and returns string output

    r = spRe.Recognizer()
    with spRe.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(" Recognizing... ".center(110, "="))    
        query = r.recognize_google(audio, language=progLang)
        print(f"User said: {query}\n")

    except Exception as e:
            # print(e)    
        print(" Say that again please... ".center(110, "="))  
        listen()
    return query

def welcome():
    hour=int(datetime.datetime.now().hour)
    if "ar" == progLang :
        if hour>=0 and hour<12:
            speak("صباح الخير يا قدوة")
        elif hour>=12 and hour<18:
            speak("مساءك ملبن يا ملبن")
        else:
            speak("الجو حر اوي يا اخويا")
        speak("عايز ايه يعم انت , انا مش فايقلك")
    else :
        if hour>=0 and hour<12:
            speak("Good Morning , My Brother")
            print(" Good Morning , My Brother ".center(110, "="))
        elif hour>=12 and hour<18:
            speak("Good Afternoon , My Brother")
            print(" Good Afternoon , My Brother ".center(110, "="))
        else:
            speak("A Hot Night is Here , My Brother")
            print(" A Hot Night is Here , My Brother ".center(110, "="))
        speak("I am Here , How Can I help you?")
        print(" I am Here , How Can I help you? ".center(110, "="))

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    reply = response.choices[0].text.strip()
    return reply
def coun():
    # folder path
    dir_path = r'C:\Users\ahmed\Downloads\Music'
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1

    return count-1
"""##################### Function Define End #######################"""
