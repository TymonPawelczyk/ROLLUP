import datetime as datetime
import time as time
# import calendar as calendar
import requests as requests
import json
import gpiozero



#Połaczenie z API
payload = {'lat' : '50.3657432' , 'lng' : '18.87153251609449' , 'formatted' : '1'}
url = 'https://api.sunrise-sunset.org/json'

#Zapytanie API
response = requests.get(url, params = payload)
json_object = response.json()

sunrise = str(json_object['results']['sunrise'])
sunset = str(json_object['results']['sunset'])

# print(json_object)
print(sunrise,sunset)


#Sprawdzanie godziny
# while True:
#     now = datetime.datetime.now()
#     hour = now.hour
#     print(now.hour)
#     if hour == 14:
#         print("Otwieranie rolety")
#         time.sleep(3600)
#     else: 
#         print("Nie ma jeszcze określonej godziny.")
#     time.sleep(1)