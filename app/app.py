import datetime as datetime
from datetime import *
import time as time
# import calendar as calendar
import requests as requests
import json



#Połaczenie z API
payload = {'lat' : '50.5289' , 'lng' : '18.75127' , 'formatted' : '0'}
url = 'https://api.sunrise-sunset.org/json'

#Zapytanie API
response = requests.get(url, params = payload)
json_object = response.json()

responce_sunrise = str(json_object['results']['sunrise'])
responce_sunset = str(json_object['results']['sunset'])



#Formatowanie ver 2
formatfrom="%Y-%m-%dT%H:%M:%S+00:00"
formatto="%H:%M:%S"
formatted = (datetime.strptime(responce_sunrise,formatfrom).strftime(formatto))
formatted = formatted.split(':')
formatted[0] = (int(formatted[0])) + 1
print(formatted)



#Formatowanie ver 1
sunrise = responce_sunrise.split('T')
sunset = responce_sunset.split('T')
sunrise = sunrise[1].partition('+')
sunset = sunset[1].partition('+')
sunrise = sunrise[0]
sunset = sunset[0]

print(sunrise,sunset)

#Sprawdzanie godziny
while True:
    now = datetime.now()
    hour = str(now.hour)
    minute = str(now.minute)
    seconds = str(now.second)
    CURRENT_TIME_str = (hour+":"+minute+":"+seconds)
    print(f'{CURRENT_TIME_str} = {sunrise}')
    if CURRENT_TIME_str == sunrise:
        print("Otwieranie rolety") #Tutaj odniesienie do wykonania pliku otwierajacego rolety 
        time.sleep(3600)
    else: 
        print("Nie ma jeszcze określonej godziny.")
    time.sleep(1)
