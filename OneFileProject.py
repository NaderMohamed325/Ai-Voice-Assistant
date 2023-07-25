"""####################### Library Files Start ######################"""
import pyttsx3 # take a text and convert it to voice
import ecapture as ec
import pyautogui
import speech_recognition as spRe
import datetime
import webbrowser
import os
import smtplib
from email.mime.text import MIMEText
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
from define import speak,listen,coun,chat_with_gpt,speakEn,listenEn,send_email
import psutil
from deep_translator import GoogleTranslator
"""######################## Library Files End ######################"""

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

def google():
    speakEn("Google Opened")
    print(" Google Opened ".center(110, "="))
    speakEn("What you need from Google")
    print(" What you need from Google ".center(110, "="))
    googleSearch = listen()
    googleSearch = googleSearch.replace(" ","+")
    speakEn("Operation is Done")
    print(" Operation is Done ".center(110, "="))
    url = "google.com/search?q="
    url = url + googleSearch
    webbrowser.open_new_tab(url)

def youtube():
    speakEn("Youtube Opened")
    print(" Youtube Opened ".center(110, "="))
    speakEn("What you need from Youtube")
    print(" What you need from Youtube ".center(110, "="))
    youtubeSearch = listen()
    youtubeSearch = youtubeSearch.replace(" ","+")
    speakEn("Operation is Done")
    print(" Operation is Done ".center(110, "="))
    url = "youtube.com/search?q="
    url = url + youtubeSearch
    webbrowser.open_new_tab(url)

def facebook():
    speakEn("You seem to be a fan of Mark Zuckerberg, however, Facebook is open")
    print(" You seem to be a fan of Mark Zuckerberg, however, Facebook is open ".center(110, "="))
    url = "www.facebook.com"
    webbrowser.open_new(url)

def vs_code():
    speakEn("Vs code ? hmmmm , You look like a Programmer")
    print(" Vs code ? hmmmm , You look like a Programmer ".center(110, "="))
    speakEn("Vs code is open")
    print(" Vs code is open ".center(110, "="))
    codePath = r"C:\Users\ahmed\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    os.startfile(codePath)

def time_now():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speakEn(f"Sir, the time is {strTime}")
    print(f" Sir, the time is {strTime} ".center(110, "="))

def date_now():
    strTime = datetime.date.today()
    speakEn(f"Sir, the time is {strTime}")
    print(f" Sir, the time is {strTime} ".center(110, "="))

def ece_drive():
    speakEn("ohhh yaa , you are from e c e 2026 , you are lucky , however , drive is open")
    print(" ohhhhhh ya , you are from ece 2026 , you are lucky , however , drive is open ".center(110, "="))
    url = "https://drive.google.com/drive/folders/13NMDUoI4rid0KJYlIfAeeC-RExtsFJFR"
    webbrowser.open_new_tab(url)

def developers():
    speakEn("This Program is developed By 4 student In Ece department")
    print(" This Program is developed By 4 student In Ece department ".center(110, "="))

def ece_channel():
    speakEn("You seem to be a fan of abdelrahman Asem records, however, channel is open")
    print(" You seem to be a fan of abdelrahman Asem records, however, channel is open ".center(110, "="))
    url = "https://www.youtube.com/@ECE-2026"
    webbrowser.open_new(url)

def discord():
    speakEn("Discord ? hmmmm , You look like a Gamer")
    print(" Discord ? hmmmm , You look like a Gamer ".center(110, "="))
    speakEn("You need Application Or Website")
    print(" You need Application Or Website ".center(110, "=")) 
    respond = listenEn()
    if "application" in respond.lower() :
        codePath = "C:\\Users\\ahmed\\AppData\\Local\\Discord\\app-1.0.9015\\Discord.exe"
        os.startfile(codePath)
    elif "website" in respond.lower() :
        url = "https://www.discord.com"
        webbrowser.open_new(url)
    else : 
        speakEn("Unknown choose , sorry about this error")
        print(" Unknown choose , sorry about this error ".center(110, "="))

def whatsapp() : 
    speakEn("Whatsapp ? hmmmm , You will talk to the crush ? , You seem naughty")
    print(" Whatsapp ? hmmmm , You will talk to the crush ? , You seem naughty ".center(110, "="))
    speakEn("You need Application Or Website")
    print(" You need Application Or Website ".center(110, "="))
    respond = listenEn()
    if "application" in respond.lower() :
        codePath = "C:\\Users\\ahmed\\AppData\\Local\\WhatsApp\\app-2.2310.5\\WhatsApp.exe"
        os.startfile(codePath)
    elif "website" in respond.lower() :
        url = "https://web.whatsapp.com/"
        webbrowser.open_new(url)
    else : 
        speakEn("Unknown choose , sorry about this error")
        print(" Unknown choose , sorry about this error ".center(110, "="))

def linkedin():
    speakEn("linkedin hmmmmmmm ? , you search about A job")
    print(" linkedin hmmmmmmm ? , you search about A job ".center(110, "="))
    speakEn("operation Done!")
    print(" operation Done! ".center(110, "="))
    url = "https://www.linkedin.com/feed/"
    webbrowser.open_new(url)

def calculation():
    speakEn("operation is done")
    codePath = r"C:\Windows\System32\calc.exe"
    os.startfile(codePath)

def edge():
    speakEn("operation is done")
    codePath = r"C:\Users\ahmed\AppData\Local\Microsoft\WindowsApps\MicrosoftEdge.exe"
    os.startfile(codePath)

def wikipedia():
    speakEn("ًWikipedia Opened")
    print(" Wikipedia Opened ".center(110, "="))
    speakEn("What you need from Wikipedia")
    print(" What you need from Wikipedia ".center(110, "="))
    value = listen()
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
    speakEn("I am an artificial intelligence program that is not intended for laughter my Naughty . Nevertheless, I will tell you a joke that will make you laugh for the next year")
    print(" I am an artificial intelligence program that is not intended for laughter my Naughty . Nevertheless, I will tell you a joke that will make you laugh for the next year ".center(110, "="))
    num = int(random.randint(0,8))
    if num == 0 :
        speakEn("why is six sacred seven ?")
        print(" why is six sacred seven ? ".center(110, "="))
        speakEn("Because seven eghit nine Hahahahahahahahahahahahahaha")
        print(" Because seven eghit nine ".center(110, "="))
    elif num == 1 :
        speakEn("Why do we tell actors to “break a leg?”")
        print(" Why do we tell actors to “break a leg?” ".center(110, "="))
        speakEn("Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor. Hahahahahahahahahahahahahaha")
        print(" Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor. ".center(110, "="))
    elif num == 2 :
        speakEn("Why don't skeletons fight each other?")
        print(" Why don't skeletons fight each other? ".center(110, "="))
        speakEn("They don't have the guts! , Hahahahahahahahahahahaha")
        print(" They don't have the guts! ".center(110, "="))
    elif num == 3 :
        speakEn("Why did the scarecrow win an award?")
        print(" Why did the scarecrow win an award? ".center(110, "="))
        speakEn("Because he was outstanding in his field! , Hahahahahahahahahahahaha")
        print(" Because he was outstanding in his field! ".center(110, "="))
    elif num == 4 :
        speakEn("How do you organize a space party?")
        print(" How do you organize a space party? ".center(110, "="))
        speakEn("You planet! , Hahahahahahahahahahahaha")
        print(" You planet! ".center(110, "="))
    elif num == 5 :
        speakEn("Why don't eggs tell jokes?")
        print(" Why don't eggs tell jokes? ".center(110, "="))
        speakEn("Because they might crack up! , Hahahahahahahahahahahaha")
        print(" Because they might crack up! ".center(110, "="))
    elif num == 6 :
        speakEn("Why did the tomato turn red?")
        print(" Why did the tomato turn red? ".center(110, "="))
        speakEn("Because it saw the salad dressing! , Hahahahahahahahahahahaha")
        print(" Because it saw the salad dressing! ".center(110, "="))
    elif num == 7 :
        speakEn("What do you call a snowman with a six-pack?")
        print(" What do you call a snowman with a six-pack? ".center(110, "="))
        speakEn("An abdominal snowman! , Hahahahahahahahahahahaha")
        print(" An abdominal snowman! ".center(110, "="))
    elif num == 8 :
        speakEn("What do you Call Someone with No Body and No Nose?")
        print(" What do you Call Someone with No Body and No Nose? ".center(110, "="))
        speakEn("Nobody Nose! , Hahahahahahahahahahahaha")
        print(" Nobody Nose! ".center(110, "="))

def chatGpt():
    speakEn("Chat Gpt is open")
    print(" Chat Gpt is open ".center(110, "="))
    speakEn("What do You Need from Gpt ?")
    print(" What do You Need from Gpt ? ".center(110, "="))
    user_input = listen()
    user_input = user_input.strip()
    while True:
        if user_input.lower() == ('shut down' or "bye"):
            speak("Goodbye!")
            print(" Bot: Goodbye! ".center(110, "="))
            break
        response = chat_with_gpt(user_input)
        speak(response)
        print(f" Bot: {response} ".center(110, "="))
        user_input = listen() 

def playMusic() :
    songs_dir=r"C:\\Users\\ahmed\\Downloads\\Music"
    songs=os.listdir(songs_dir)
    ra = random.randint(0,coun())
    os.startfile(os.path.join(songs_dir,songs[ra]))

def weather():
    api_key = "2493d2dbe14bd976436c91a8d6757ff3"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speakEn("in which city you need to weather")
    print("in which city you need to weather")
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
        speakEn(" Temperature = " +
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
        speakEn(" City Not Found ")
        print(" City Not Found ".center(110, "="))

def get_battery_charge():
  """Returns the percentage of battery charge."""
  battery = psutil.sensors_battery()
  if battery is None:
    return None
  else:
    battery_percentage = psutil.sensors_battery().percent
    print(f" your battery status is {battery_percentage}% " .center(110, "="))
    speakEn(f"your battery status is {battery_percentage}%")

    if battery_percentage <=20:
     speak("please connect the charge")
    return battery_percentage

def shutdown():
    return os.system("shutdown /s /t 1")

def restart():
    return os.system("shutdown /r /t 1")

def log_out():
    return os.system("shutdown -l") 

def capture():
    ec.capture(0,"frame", "frame.png")

def video_take():
    ec.vidCapture(0,"frame.avi", 10)

def screenshot():
    myscreen = pyautogui.screenshot()
    myscreen.save('myscreen.jpg')

def notes() :
    speakEn("What you need to note ?")
    print(" What you need to note ? ".center(110, "="))
    myNote = listen()
    f = open("MyNotes.txt")
    f.write(myNote)
    f.write("\n")
    speakEn("That is a Nice Note")
    f.close()

def translation():
    speakEn("From each langauge you need to translate")
    print("From each langauge you need to translate".center(110, "="))
    language = listenEn()
    language = language.split().lower()
    if language == "arabic" :
            speakEn("Say your statement")
            to_translate = listen()
            translated = GoogleTranslator(source='auto', target='en').translate(to_translate)
            speakEn(translated)
            print(translated)
    else :
            speakEn("Say your statement")
            to_translate = listenEn()
            translated = GoogleTranslator(source='auto', target='ar').translate(to_translate)
            speak(translated)
            print(translated)

def emails():
    email_sender = 'ahmedbasem12004@gmail.com'
    speakEn("Enter The Email You Want TO send the Email")
    email_receiver = input("Enter The Email Please : ")
    email_password = "heuxxxajgpgoalds"
    speakEn("Say What is the Subject of Mail")
    print(" Say What is the Subject of Mail ".center("=",110))
    subject = listenEn()
    print(" Say What is the Body of Mail ".center("=",110))
    body = listenEn()
    send_email(subject, body, email_sender, email_receiver, email_password)

"""##################### Function Define End #######################"""
welcome()
UserOrder = listen()
UserOrder = UserOrder.lower()
while True :
    if progLang == "ar" :
        if "سلام" in UserOrder :
            break
        elif "شكرا" in UserOrder :
            break
        elif "الي اللقاء" in UserOrder :
            break
        elif "باي" in UserOrder :
            break
        elif "يوتيوب" in UserOrder :
            youtube()
            break
        elif "جوجل" in UserOrder :
            google()
            break    
        elif "فيسبوك" in UserOrder :
            facebook()
            break
        elif "ديسكورد" in UserOrder :
            discord()
            break
        elif "كود" in UserOrder :
            vs_code()
            break
        elif "في اس" in UserOrder :
            vs_code()
            break
        elif "وقت" in UserOrder :
            time_now()
            break
        elif "الوقت" in UserOrder :
            time_now()
            break
        elif "التاريخ" in UserOrder :
            date_now()
            break
        elif "تاريخ" in UserOrder :
            date_now()
            break
        elif "درايف" in UserOrder :
            ece_drive()
            break
        elif "قناة" in UserOrder :
            ece_channel()
        elif "المطورين" in UserOrder :
            developers()
        elif "المطورين" in UserOrder :
            developers()
        elif "لينكد ان" in UserOrder :
            linkedin()
        elif "لينكدان" in UserOrder :
            linkedin()
        elif "ويكبيديا" in UserOrder :
            wikipedia()
        elif "نكته" in UserOrder :
            joke()
        elif "ضحكني" in UserOrder :
            joke()
        elif "شات" in UserOrder :
            chatGpt()
        elif "جي بي تي" in UserOrder :
            chatGpt()
        elif "واتس" in UserOrder :
            whatsapp()
            break
        elif "واتساب" in UserOrder :
            whatsapp()
            break
        elif "موسيقى" in UserOrder :
            playMusic()
            break
        elif "ترجمه" :
            translation()
            break
        elif "الطقس" in UserOrder :
            weather()
            break
        elif "درجة الحرارة" in UserOrder :
            weather()
            break
        elif "اقفل الجهاز" in UserOrder :
            shutdown()
        elif "اعد تشغيل الجهاز" in UserOrder :
            restart()
        elif "لوج اوت" in UserOrder :
            log_out()
        elif "نسبه شحن البطاريه" in UserOrder :
            get_battery_charge()
        elif "نسبه الشحن" in UserOrder :
            get_battery_charge()
        elif "لقطه شاشه" in UserOrder :
            screenshot()
            break
        elif "صوره" in UserOrder :
            capture()
            break
        elif "فيديو" in UserOrder :
            video_take()
            break
        elif "ملاحظه" in UserOrder :
            notes()
            break
        elif "تسجيل ملاحظه" in UserOrder :
            notes()
            break
        elif "ارسال بريد" :
            emails()
            break
        else : 
            result = chat_with_gpt(UserOrder)
            speak(result)
            break
    else :
        if "bye" in UserOrder :
            break
        elif "goodbye" in UserOrder :
            break
        elif "thanks" in UserOrder :
            break
        elif "youtube" in UserOrder :
            youtube()
            break
        elif "google" in UserOrder :
            google()
            break    
        elif "facebook" in UserOrder :
            facebook()
            break
        elif "discord" in UserOrder :
            discord()
            break
        elif "code" in UserOrder :
            vs_code()
            break
        elif "time" in UserOrder :
            time_now()
        elif "date" in UserOrder :
            date_now()
        elif "our drive" in UserOrder :
            ece_drive()
            break
        elif "our channel" in UserOrder :
            ece_channel()
            break
        elif "developers" in UserOrder :
            developers()
        elif "linkedin" in UserOrder :
            linkedin()
            break
        elif "send email" :
            emails()
            break
        elif "translation" :
            translation()
            break
        elif "wikipedia" in UserOrder :
            wikipedia()
        elif "joke" in UserOrder :
            joke()
        elif "gbt" in UserOrder :
            chatGpt()
        elif "chat" in UserOrder :
            chatGpt()
        elif "gpt" in UserOrder :
            chatGpt()
        elif 'what\'s' in UserOrder :
            whatsapp()
            break
        elif "whatsapp" in UserOrder :
            whatsapp()
            break
        elif ("music") in UserOrder :
            playMusic()
            break
        elif "temperature" in UserOrder :
            weather()
            break
        elif "weather" in UserOrder :
            weather()
        elif ("shut down") in UserOrder :
            shutdown()
        elif ("restart") in UserOrder :
            restart()
        elif ("log out") in UserOrder :
            log_out()
        elif ("battery") in UserOrder :
            get_battery_charge()
        elif ("screenshot") in UserOrder :
            screenshot()
            break
        elif ("image") in UserOrder :
            capture()
            break
        elif ("photo") in UserOrder :
            capture()
            break
        elif ("take a video") in UserOrder :
            video_take()
            break
        elif ("video") in UserOrder :
            video_take()
            break
        elif"note" in UserOrder :
            notes()
            break
        elif"notes" in UserOrder :
            notes()
            break
        else : 
            result = chat_with_gpt(UserOrder)
            speak(result)
            break
    speakEn("Any Thing Other")
    UserOrder = listen()
    UserOrder = UserOrder.lower()
