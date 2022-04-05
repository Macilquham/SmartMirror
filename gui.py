from tkinter import *
from datetime import datetime, time
import time as t
import requests
import json
import random

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
        self.__greeting = MathQuiz()

    def execute(self):
        current_time = datetime.now().time()
        school_finish = time(15,0,0)
        school_start = time(9,0)

        # if school_start < current_time < school_finish:
        #     self.__greeting  = MorningGreeting()
  
        self.__ui.after(0,self.handle)
        self.__ui.start()

    def handle(self):
        message = self.__greeting.message
        self.action(message, 0, 0)
        

    def action(self, message, messageIndex, messageposition):
            self.__ui.greeting(message[messageIndex][0:messageposition])
            if(messageposition - 1 != len(message[messageIndex])):
                self.__ui.after(350, self.action, message, messageIndex, messageposition+1)
            elif(messageIndex + 1 != len(message)):
                self.__ui.after(1500, self.action,  message, messageIndex+1, 0)
            else:
                 self.__ui.after(1500, self.__ui.stop)
                

class GenericGreeting:

     @property
     def message(self):
         return ["Hi, Sam!"]

class MorningGreeting:
     @property
     def message(self):
         return ["Good morning, Sam"]

class MathQuiz:
     @property
     def message(self):
         first_number = random.randrange(0,5)
         second_number = random.randrange(0,5)
         total = first_number + second_number
         return ["Ready for a math quiz, Sam?","What is {0} + {1}?".format(first_number, second_number), "{0} + {1} = {2}".format(first_number, second_number,total)]

class RandomFact:
     @property
     def message(self):
        api_url = 'https://api.api-ninjas.com/v1/country?name=United States'
        response = requests.get(api_url, headers={'X-Api-Key': 'rInxjc8lmjG+C0NLpIQAfg==PbQmi3w6GeiKloEU'})
        if response.status_code == requests.codes.ok:
            text = json.loads(response.text)
            return["The capital of America is "+text[0]["capital"]]
        else:
            return ["The capital of New Zealand is Wellington"]

        

    