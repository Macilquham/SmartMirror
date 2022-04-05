from tkinter import *
from datetime import datetime, time
import time as t

class Gui:

    def __init__(self):
        self.__root = Tk()
        self.__greetingLabel = Label(font=('Times', 24))
        self.__greetingLabel.place(x=10,y=10)
        self.__root.wm_attributes("-topmost", True)
        self.__root.geometry("500x500")
        # self.__root.wm_attributes("-fullscreen", True)

    def greeting(self, name:str):
        self.__greetingLabel.config(text=name)
    
    def after(self, time, eventToExecute, *args):
        self.__root.after(time, eventToExecute, *args)

    def start(self):
        self.__root.mainloop()

    def stop(self):
        self.__root.destroy()

    def complete(self):
        self.stop()

class SmartMirror:
    def __init__(self):
        self.__ui = Gui()
        self.__greeting = GenericGreeting()

    def execute(self):
        current_time = datetime.now().time()
        school_finish = time(15,0,0)
        school_start = time(9,0)

        if school_start < current_time < school_finish:
            self.__greeting  = MorningGreeting()
  
        self.__ui.after(0,self.handle)
        self.__ui.start()

    def handle(self):
        message = self.__greeting.message
        self.action(message, 0)
        # self.__ui.stop();

    def action(self, message, messageposition):
        self.__ui.greeting(message[0:messageposition])
        if(messageposition - 1 != len(message)):
            self.__ui.after(350, self.action, messageposition+1)

class GenericGreeting:

     @property
     def message(self):
         return "Hi, Sam!"

class MorningGreeting:
     @property
     def message(self):
         return "Good morning, Sam"

        

    