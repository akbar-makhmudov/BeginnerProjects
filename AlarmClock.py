import datetime
from playsound import playsound

print("It is currently: "+datetime.datetime.today().strftime("%H") + ":"+datetime.datetime.today().strftime("%M"))
hour = int(input("What hour should the alarm be set for? [00:00 format]"))
minute = int(input("What minute should the alarm be set for? [00:00]"))
print ("Alarm Set")
x = False
while x == False:
    if hour == int(datetime.datetime.today().strftime("%H")) and minute == int(datetime.datetime.today().strftime("%M")):
        
        print ("Alarm raised!")
        playsound(r"C:\Users\makhakba\Downloads\Ding-dong-sound-effect.mp3")
        x = True
    