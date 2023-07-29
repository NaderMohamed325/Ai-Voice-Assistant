#####################################################################
# @file    : define.py
# @author  : Ahmed Basem - Nader Mohamed - Mohamed Wesam - Alaa Yasser
# @version : 0.0.1
# @brief   : Ai voice assistant
#####################################################################

"""####################### Library Files Start ######################"""
import datetime  # Module to work with dates and times
import os  # Module for interacting with the operating system
import smtplib  # Simple Mail Transfer Protocol (SMTP) library for sending emails
import tkinter as tk  # GUI library for creating graphical interfaces
from email.mime.text import MIMEText
from tempfile import NamedTemporaryFile  # Library for temporary file operations

import google.generativeai as palm  # Google generative AI API
import gtts  # Google Text-to-Speech library
import openai  # OpenAI GPT-3 language model API
import pygame  # Library for game development
# Importing necessary libraries and modules
import pyttsx3  # Text-to-speech library
import speech_recognition as spRe  # Library for speech recognition

root = tk.Tk()  # Creating a Tkinter root window
root.title('ChatGPT AI Voice Assistant')  # Setting the title for the GUI window
input_box = tk.Entry(root, width=70, )  # Creating an input box for user input
input_box.pack(pady=10)  # Packing the input box in the GUI window with some padding
output_box = tk.Text(root, width=80, height=25, state='normal',
                     font=('Arial', 15))  # Creating a text box for displaying output
output_box.configure(background='#212122')  # Configuring the background color of the text box
output_box.configure(foreground='white')  # Configuring the text color of the text box
output_box.pack(pady=10)  # Packing the text box in the GUI window with some padding
refresh_button = tk.Button(root, text='Start', command="", width=20, height=2,
                           font=('Arial', 15))  # Creating a button widget
refresh_button.configure(background='#212122')  # Configuring the background color of the button
refresh_button.configure(foreground='white')  # Configuring the text color of the button
refresh_button.pack(pady=10)  # Packing the button in the GUI window with some padding
ask_button = tk.Button(root, text='Ask me a question...', command="", width=20, height=2,
                       font=('Arial', 13))  # Creating another button widget
ask_button.configure(background='#212122')  # Configuring the background color of the button
ask_button.configure(foreground='white')  # Configuring the text color of the button
"""######################## Library Files End ######################"""

"""###################### Global variable start ####################"""
# Initializing text-to-speech engine
engine = pyttsx3.init('sapi5')
# Getting available voices for the text-to-speech engine
voices = engine.getProperty('voices')
# Setting the voice for the text-to-speech engine (in this case, the second voice is selected)
engine.setProperty('voice', voices[1].id)
# Setting the speed rate for the text-to-speech engine
engine.setProperty('rate', 150)
# Setting OpenAI GPT-3 API key
openai.api_key = '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'
# Configuring Google generative AI API key
palm.configure(api_key='YOUR_API_KEY')  # Replace 'YOUR_API_KEY' with an actual API key
"""####################### Global variable end #####################"""

"""##################### Function Define Start #####################"""


# Function for converting text to voice and displaying it
def speakEn(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    # Enabling the output text box and inserting the response
    output_box.configure(state='normal')
    output_box.insert('end', f"Bot : {text} \n")
    output_box.configure(state='disabled')


# Function for listening to user's speech and converting it to text
def listenEn():
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
    # Enabling the output text box and inserting the user's speech
    output_box.configure(state='normal')
    output_box.insert('end', f"User : {query} \n")
    output_box.configure(state='disabled')
    return query


# Function to greet the user based on the time of day
def welcome():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speakEn("Good Morning, My Brother")
        print(" Good Morning , My Brother ".center(110, "="))
    elif hour >= 12 and hour < 18:
        speakEn("Good Afternoon, My Brother")
        print(" Good Afternoon , My Brother ".center(110, "="))
    else:
        speakEn("A Hot Night is Here, My Brother")
        print(" A Hot Night is Here , My Brother ".center(110, "="))
    speakEn("I am Here ")


# Function to start the voice assistant
progLang = 'ar'


def start():
    print("=" * 110)
    ask_button.pack(pady=10)
    refresh_button.pack_forget()
    speakEn("Hello my Friend, I am basem")
    speakEn("Before starting with You Please Choose which language you Want me to continue")
    print(" Before starting with You Please Choose which language you Want me to continue ".center(110, "="))
    print(" For Arabic say arabic -- For English say english ".center(110, "="))
    progLang1 = str(listenEn()).lower()
    global progLang
    if "english" in progLang1:
        progLang = "en"
    elif "arabic" in progLang1:
        progLang = "ar"
    welcome()


# Command for the 'Start' button to call the start() function
refresh_button.configure(command=start)


# Function to convert text to speech with speed adjustment
def speak(text, lang=progLang, speed=2.0):
    output_folder = os.path.expanduser("~/JarvisOutput")
    os.makedirs(output_folder, exist_ok=True)

    with NamedTemporaryFile(delete=False) as output_file:
        tts = gtts.gTTS(text, lang=lang, slow=False)
        tts.save(output_file.name)
        output_file.seek(0)
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(output_file.name)
    sound.set_volume(2.0)
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
    pygame.mixer.quit()
    pygame.time.wait(500)
    os.remove(output_file.name)
    output_box.configure(state='normal')
    output_box.insert('end', f"Bot : {text} \n")
    output_box.configure(state='disabled')


# Function to listen to user's speech with speed adjustment
def listen():
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
        print(" Say that again please... ".center(110, "="))
        listen()
    output_box.configure(state='normal')
    output_box.insert('end', f"User : {query} \n")
    output_box.configure(state='disabled')
    return query


# Function to have a conversation with the GPT-3.5 language model
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


# Function to count the number of files in a directory
def coun():
    dir_path = r'C:\Users\ahmed\Downloads\Music'
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    return count - 1


# Function to send an email using the SMTP protocol
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    speakEn("Message sent!")
    print("Message sent!".center("=", 110))


"""##################### Function Define End #######################"""
