import time
from playsound import playsound
"""
t = int(input("Kaç saniye çalışacaksın?"))

while t:
    mins = t // 60
    secs = t % 60
    timer = "{:02d}:{:02d}".format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1
print("Ara ver!")

"""
n = int(input("Kaç pomodoro yapacaksın?\n"))
for i in range(n):
    t = 25*60
    while t:
        mins = t // 60
        secs = t % 60
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    sayi = i + 1
    print(f"{sayi}.Pomodoro bitti.")
    playsound('nralarm.wav')
    print("5 dk ara")
    time.sleep(300)

print("Çalışma bitmiştir.")


    


