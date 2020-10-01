#A code which reminds the programmer to drink water,
# exercise his eyes do little physical activity to reduce fatiguness

import time
from pygame import mixer
from datetime import datetime

while True:

    print("**Welcome to Healthy Life System**")
    print("We will take care of your eyes,heart and body hydration\n")
    
    time.sleep(15)
    mixer.init()
    mixer.music.load("water.mp3")
    print("Reminder!! Please Drink Water")
    mixer.music.set_volume(20)
    mixer.music.play()
    time.sleep(15)
    mixer.music.stop()
    value = input("Please update your done task\n")
    with open("Water_Intake.txt", "a") as op:
        op.write(f"{datetime.now()}" + ":" + value + "\n")
    print("Successfully updated")
    time.sleep(10)
    mixer.init()
    mixer.music.load("eyesexercise.mp3")
    print("Reminder!! Eyes Exercise Time")
    mixer.music.set_volume(20)
    mixer.music.play()
    time.sleep(10)
    mixer.music.stop()
    value2 = input("Please update your done tasks\n")
    with open("Eyes_Exercise.txt", "a") as op:
        op.write(str([str(time.ctime())]) + ":" + value2 + "\n")
    print("successfully updated")
    time.sleep(15)
    mixer.init()
    mixer.music.load("physicalexercise.mp3")
    print("Reminder!! Physical Exercise Time")
    mixer.music.set_volume(20)
    mixer.music.play()
    time.sleep(10)
    mixer.music.stop()
    
    print("Its time for little pysical exercise")
    value3 = input("Please write your done task\n")
    with open("Physical_Exercise.txt", "a") as op:
        op.write(str([str(time.ctime())]) + ":" + value3 + "\n")
    print("successfully updated")
    
    a=int(input(" Press 1 for continuation and 0 to exit"))
    
    if a==0:
        exit()
    else:
        continue




