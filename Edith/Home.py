from Funtion import *
from Sets import *
from Task import replay
import requests

 

url = "http://www.google.com"
timeout = 5
try:
	request = requests.get(url, timeout=timeout)
	while True :
		query = lisn()
		if query in  wake_up :
			wish = wishMe ()
			replay()
			
except (requests.ConnectionError, requests.Timeout) as exception:
	print("No internet connection.")
	spk ("plese check your internet conection")

