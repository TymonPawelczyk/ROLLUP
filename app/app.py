import datetime as datetime
import time as time
import calendar as calendar
import requests as requests
import json



payload = {'formatted':'0'}

#Połaczenie z API
response = requests.post("https://api.sunrise-sunset.org/json?lat=50.3657432&lng=18.87153251609449", params = payload)

print(response.json())

#Sprawdzanie godziny
while True:
    now = datetime.datetime.now()
    hour = now.hour
    print(now.hour)
    if hour == 0:
        now = datetime.datetime.now()
        hour = now.hour
        print("Otwieranie rolety")
        time.sleep(3600)
    else: 
        print("Nie ma jeszcze określonej godziny.")
        time.sleep(1)
    time.sleep(1)