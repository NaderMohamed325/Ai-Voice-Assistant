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
import smtplib
from email.mime.text import MIMEText
import tkinter as tk
root = tk.Tk()
root.title('ChatGPT AI Voice Assistant')
input_box = tk.Entry(root, width=70,)
input_box.pack(pady=10)
output_box = tk.Text(root, width=80, height=25, state='normal',font=('Arial', 15))
output_box.configure(background='#212122')
output_box.configure(foreground='white')
output_box.pack(pady=10)
refresh_button = tk.Button(root, text='Start', command="",width=20 ,height=2,font=('Arial', 15))
refresh_button.configure(background='#212122')
refresh_button.configure(foreground='white')
refresh_button.pack(pady=10)
ask_button = tk.Button(root, text='Ask me a question...', command="",width=20 ,height=2,font=('Arial', 13))
ask_button.configure(background='#212122')
ask_button.configure(foreground='white')
"""######################## Library Files End ######################"""

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
    output_box.configure(state='normal')
    output_box.insert('end', f"Bot : {text} \n")
    output_box.configure(state='disabled')

def listenEn():  #It takes microphone input from the user and returns string output

    r = spRe.Recognizer()
    with spRe.Microphone() as source:
        print(" Listening... ".center(110, "="))
        output_box.configure(state='normal')
        output_box.insert('end', f"Bot : Listening... \n")
        output_box.configure(state='disabled')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(" Recognizing... ".center(110, "="))
        output_box.configure(state='normal')
        output_box.insert('end', f"Bot : Recognizing... \n")
        output_box.configure(state='disabled')    
        query = r.recognize_google(audio, language="en-in")
        print(f" User said: {query}\n ")

    except Exception as e:
        print(" Say that again please... ".center(110, "="))  
        listenEn()
    output_box.configure(state='normal')
    output_box.insert('end', f"User : {query} \n")
    output_box.configure(state='disabled')
    return query

def welcome():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speakEn("Good Morning , My Brother")
        print(" Good Morning , My Brother ".center(110, "="))
    elif hour>=12 and hour<18:
        speakEn("Good Afternoon , My Brother")
        print(" Good Afternoon , My Brother ".center(110, "="))
    else:
        speakEn("A Hot Night is Here , My Brother")
        print(" A Hot Night is Here , My Brother ".center(110, "="))
    speakEn("I am Here ")

progLang = 'ar'
def start():
    print("=" * 110)
    ask_button.pack(pady=10)
    refresh_button.pack_forget()
    speakEn("Hello my Friend,I am basem")
    speakEn("Before starting with You Please Choose which langauge you Want me to continue")
    print(" Before starting with You Please Choose which langauge you Want me to continue ".center(110 , "="))
    print(" For Arabic say arabic -- For English say english ".center(110, "="))
    progLang1 = str(listenEn()).lower()
    global progLang
    if "english" in progLang1 :
        progLang = "en"
    elif "arabic" in progLang1 :
        progLang = "ar"
    welcome()
refresh_button.configure(command= start)
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
    output_box.configure(state='normal')
    output_box.insert('end', f"Bot : {text} \n")
    output_box.configure(state='disabled')

def listen():  #It takes microphone input from the user and returns string output

    r = spRe.Recognizer()
    with spRe.Microphone() as source:
        print("Listening...")
        output_box.configure(state='normal')
        output_box.insert('end', f"Bot : Listening... \n")
        output_box.configure(state='disabled')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(" Recognizing... ".center(110, "="))    
        output_box.configure(state='normal')
        output_box.insert('end', f"Bot : Recognizing... \n")
        output_box.configure(state='disabled')  
        query = r.recognize_google(audio, language=progLang)
        print(f"User said: {query}\n")

    except Exception as e:
            # print(e)    
        print(" Say that again please... ".center(110, "="))  
        listen()
    output_box.configure(state='normal')
    output_box.insert('end', f"User : {query} \n")
    output_box.configure(state='disabled')
    return query

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
    output_box.configure(state='normal')
    output_box.insert('end', f"Bot : {text} \n")
    output_box.configure(state='disabled')

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

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    speakEn("Message sent!")
    print("Message sent!".center("=",110))
"""##################### Function Define End #######################"""
