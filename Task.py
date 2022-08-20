from logging import shutdown
from logging.config import listen
from Funtion import *
from Sets import *
import webbrowser
from datetime import datetime
import random
from requests import get
import  pyjokes
import os
import screen_brightness_control as br
import pyautogui 
import requests

def replay():
    now = datetime.now()

    while True :

        query = lisn()

        if "name" in query:
            spk("my name is Edith")

        elif "who are you" in query:
            spk("iam your personal assistant")

        elif "date" in query:
            d = now.strftime("%B %d, %Y")
            spk(d)

        elif "time" in query:
            t = now.strftime("%I:%M")
            spk(t)

        elif "battery" in query:
            battery()          

        elif "search" in query :
            query = query.removeprefix("search ")
            spk(f"searching {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            break
 
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            spk(f"IP Adress is {ip}")
        
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            spk(joke)

        elif "note" in query:
    
            spk("What should I write down")
            memory =  lisn().lower()
            spk("Noted")
            note = open("Edith_note.txt", "w")
            print (note)
            note.write(memory)
            note.close()

        elif "network" in query:
            avilablenetwork()

        elif "internet" in query:
            url = "http://www.google.com"
            timeout = 5
            try:
                request = requests.get(url, timeout=timeout)
                devices = subprocess.check_output(['netsh','wlan','show','network'])
                devices = devices.decode('ascii')
                devices= (devices.replace("\r","" )
                .replace("Network type","")
                .replace("SSID","")
                .replace("Infrastructure","")
                .replace("Open","")
                .replace("Authentication","")
                .replace(":","")
                .replace("There are 1 networks currently visible.","")
                .replace("Encryption","")
                .replace("None","")
                .replace("1","you are connected in")
                )
                spk(devices)
            except (requests.ConnectionError, requests.Timeout) as exception:
                spk("internet is not working")
                spk ("plese check your internet conection")


        elif "open cmd" in query:
            spk("opening command prompt")
            os.system("start cmd")
            lisn()
                    

        elif 'open' in query:
            query = query.removeprefix("open ")
            spk (f"opening {query}")
            webbrowser.open(f"www.{query}.com")
            break
    
        elif query in change_bright :
            spk ("ok you have to set a value")
            while True :
                val = lisn()
                try :
                    br.set_brightness(val)
                    spk(f"set to {br.get_brightness()}%")
                    break 
                except :
                    spk ("sorry ") 


        elif "brightness" in query:
            print(br.get_brightness())
            spk (f"{br.get_brightness()}%")

        elif "volume up" in query :
            spk ("ok")
            pyautogui.press('volumup') 

        elif "volume down" in query :
            spk("ok")
            pyautogui.press('volumedown')

        elif "mute" in query :
            spk("ok")
            pyautogui.press('volumemute') 

        elif "sleep" in query:
            spk("ok you can me call any time")
            break

        elif query in close :
            spk ("ok iam going ")
            exit()

        elif query in greeting :
            print ("greeting")
            spk(random.choice(responce_greeting))

        elif  query in  closecomputer:
            os.system("shutdown /s /t 5")       

        elif  query in restartcomputer:
            os.system("shutdown /r /t 5")

        

        else:
            print ("same")
            spk(query)
          