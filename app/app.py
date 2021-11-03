import datetime as datetime
import time as time

hour = time.localtime()
# datetime.datetime.now().time()
print(hour)

while hour != 22:
    print("Nie ma jeszcze określonej godziny.")
    print(hour)
    time.sleep(5)
else:
    print(hour)