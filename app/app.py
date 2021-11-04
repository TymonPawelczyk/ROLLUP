import datetime as datetime
import time as time
# import calendar as calendar
import requests as requests
import json
import gpiozero



#Połaczenie z API
payload = {'lat' : '50.3657432' , 'lng' : '18.87153251609449' , 'formatted' : '0'}
url = 'https://api.sunrise-sunset.org/json'

#Zapytanie API
response = requests.get(url, params = payload)
json_object = response.json()

responce_sunrise = str(json_object['results']['sunrise'])
responce_sunset = str(json_object['results']['sunset'])

#Formatowanie 
sunrise = responce_sunrise.split('T')
sunset = responce_sunset.split('T')
sunrise = (sunrise[1].partition('+'))
sunset = sunset[1].partition('+')
sunrise = sunrise[0]
sunset = sunset[0]

print(sunrise,sunset)

#Sprawdzanie godziny
while True:
    now = datetime.datetime.now()
    hour = str(now.hour)
    minute = str(now.minute)
    seconds = str(now.second)
    CURRENT_TIME_str = (hour+":"+minute+":"+seconds)
    print(CURRENT_TIME_str)
    if CURRENT_TIME_str == "20:22:40":
        print("Otwieranie rolety")
        time.sleep(3600)
    else: 
        print("Nie ma jeszcze określonej godziny.")
    time.sleep(1)