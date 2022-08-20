
from datetime import datetime
import psutil
import speech_recognition as sr
import pyttsx3
import subprocess

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 165)

def spk(text):
    print(f"Edith :{text}")
    engine.say(text=text)
    engine.runAndWait()

def lisn():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening....")
        audio = r.listen(source, 0, 2)

        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language="en-in")
            print (query)
           
        except Exception as e:
            return ""

            
        query = str(query)
        return query.lower()

def battery ():
    def batterycharge(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)

    battery = psutil.sensors_battery()

    print("Battery left : ", batterycharge(battery.secsleft))
    spk( f"{str( battery.percent)}%")
    if battery.power_plugged == True :       
        spk ("Battery in charging")
                    
    else :
        pass
 
def wishMe():

    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        spk("Good Morning")
        return "morning"
         

    elif hour>=12 and hour<18:
        spk("Good Afternoon")
        return "aftternoon"


    else:
        spk("Good Evening ")
        return "evening"

def avilablenetwork():
   
    devices = subprocess.check_output(['netsh','wlan','show','network'])
    devices = devices.decode('ascii')
    devices= (devices.replace("\r","" )
                .replace("Network type","")
                .replace("SSID","")
                .replace("Infrastructure","")
                .replace("Open","")
                .replace("Authentication","")
                .replace(":","")
                )
    print(devices)
    spk(devices)