from define import listen,speak,welcome,progLang,chat_with_gpt
from actions import *
##################################################
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
