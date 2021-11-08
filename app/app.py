import datetime as datetime
from datetime import *
import time as time
import sched
# import calendar as calendar
import requests as requests
import json



#Aktualizowanie się czasu wschodu i zachodu

#Połaczenie z API
payload = {'lat' : '50.5289' , 'lng' : '18.75127' , 'formatted' : '0'}
url = 'https://api.sunrise-sunset.org/json'

#Zapytanie API
response = requests.get(url, params = payload)
json_object = response.json()

responce_sunrise = str(json_object['results']['sunrise'])
responce_sunset = str(json_object['results']['sunset'])



#Formatowanie ver 2
formatfrom="%Y-%m-%dT%H:%M:%S%z"
formatto="%H:%M:%S"
formatted_sunrise_winter = (datetime.strptime(responce_sunrise,formatfrom)+ timedelta(hours=1)).strftime(formatto)
formatted_sunset_winter = (datetime.strptime(responce_sunset,formatfrom)+ timedelta(hours=1)).strftime(formatto)

print((formatted_sunrise_winter),formatted_sunset_winter)


# #Sprawdzanie godziny zachodu słońca
while True:
    now = datetime.now()
    CURRENT_TIME_str = now.strftime(formatto)
    print(f'{CURRENT_TIME_str} = {formatted_sunset_winter}')
    if CURRENT_TIME_str == formatted_sunset_winter:
        print("Otwieranie rolety") #Tutaj odniesienie do wykonania pliku otwierajacego rolety 
        time.sleep(3600)
    else: 
        print("Nie ma jeszcze określonej godziny.")
    time.sleep(1)
