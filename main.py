import os
import keyboard
from datetime import date

# Prints the OS currently being used
#print (platform.system())
fileName = "test.txt"
state = True
while state == True:
    if  os.path.exists(fileName):
        print("File already exists")
    else:
        print("Creating new file... ")
        file = open("test.txt","w")
        file.write("We just created a new file!\n")
        file.close()
    
    if keyboard.is_pressed('esc'):
        print('STOPING PROGRAM')
        today = date.today()
        print(today)
        file = open("test.txt","a")
        file.write("--- LAST EDIT MADE ON --- : ")
        file.write(today.strftime("%m/%d/%Y %H:%M:%S"))
        file.write("\n")
        keyboard.send("ctrl+alt+t")
        file.close()
        state = False