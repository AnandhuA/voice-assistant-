import wikipedia
import smtplib
import pyttsx3
import speech_recognition as sr  
import time
import datetime
import requests
import json
from bs4 import BeautifulSoup
import webbrowser
import re
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer

url='https://rb.gy/bqqq92'
headr={}#"User-Agent" header for your HTTP requests.
page=requests.get(url,headers=headr)
soup=BeautifulSoup(page.content,'html.parser')
temp=soup.find(id="wob_tm").get_text().strip().encode('ascii', 'ignore').decode('ascii')
precipitaion=soup.find(id="wob_pp").get_text().strip().encode('ascii', 'ignore').decode('ascii')
print (temp)
print (precipitaion)