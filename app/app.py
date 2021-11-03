import datetime as datetime
import time as time
import calendar as calendar
import requests as requests

# datetime.datetime.now().time()

payload = {'formatted':'0'}

response = requests.get("https://api.sunrise-sunset.org/json?lat=50.3657432&lng=18.87153251609449", params = payload)

print(response.json())

# while True:
#     now = datetime.datetime.now()
#     hour = now.minute
#     print(now.minute)
#     if hour == 48:
#         now = datetime.datetime.now()
#         hour = now.minute
#         print("Otwieranie rolety")
#         time.sleep(1)
#     else:
#         print("Nie ma jeszcze określonej godziny.")
#         time.sleep(1)
# time.sleep(1)