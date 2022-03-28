from tkinter import *
from datetime import datetime, time
import time as t

class Gui:

    def __init__(self):
        self.__root = Tk()
        self.__greetingLabel = Label(font=('Times', 24))
        self.__greetingLabel.place(x=10,y=10)
        self.__root.wm_attributes("-topmost", True)
        self.__root.wm_attributes("-fullscreen", True)

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
        self.__greeting.action(self.__ui,0)
        # self.__ui.stop();



class GenericGreeting:

    def action(self, gui, messageposition):
        message = "Hi, Sam!"
        gui.greeting(message[0:messageposition])
        if(messageposition - 1 != len(message)):
            gui.after(500, self.action, gui, messageposition+1)


class MorningGreeting:

    def action(self, setLabel):
        setLabel("Good morning, Sam")
        

    