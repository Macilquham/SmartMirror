from tkinter import *
from datetime import datetime, time
import time as t
from typing import Any
from xmlrpc.client import boolean
import requests
import json
import random
from PIL import ImageTk, Image
import urllib.request
import io

class Gui:

    def __init__(self):
        self.__root = Tk()
        self.__greetingLabel = Label(font=('Times', 36, 'bold'), bg="black", fg="white", anchor="w", justify="left")
        self.__greetingLabel.place(x=650,y=250)
        self.__root.wm_attributes("-topmost", True)
        self.__root.geometry("500x500")
        self.__root.configure(bg="black")
        self.__root.wm_attributes("-fullscreen", True)

    def greeting(self, name:str):
        self.__greetingLabel.config(text=name)

    def greeting_config(self, text,image,compound):
        self.__greetingLabel.config(text=text,image=image,compound=compound)
    
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
        self.__randomGreetings = [Dog]
        #self.__randomGreetings = [CapitalCities,MathQuiz,CurrentTime, Dog]




    def execute(self, correct_user_detected:boolean):

        if not correct_user_detected:
            self.__greeting = AccessDenied()
            self.__ui.after(0,self.handle)
            self.__ui.start()
        else:   
            current_time = datetime.now().time()
            morning_finish = time(9,0)
            morning_start = time(7,0)
            bedtime_start = time(18,15)
            bedtime_end = time(19,30)

            if morning_start < current_time < morning_finish:
                self.__greeting  = MorningGreeting()
            elif bedtime_start < current_time < bedtime_end:
                self.__greeting  = BedTimeGreeting()
            else:
                self.__greeting = random.choice(self.__randomGreetings)()

            if isinstance(self.__greeting, Dog):
                dog = Dog()
                message = dog.message
                image = dog.image
                self.__ui.after(500,self.dog_action,message, image)
                self.__ui.start()
            else:
                self.__ui.after(0,self.handle)
                self.__ui.start()

    def dog_action(self, message, image):

            self.__ui.greeting_config(text=message,image=image,compound='bottom')
            self.__ui.after(4500, self.__ui.stop)

    def handle(self):
        message = random.choice(self.__greeting.message)
        self.action(message, 0, 0)
        

    def action(self, message, messageIndex, messageposition):
            self.__ui.greeting(message[messageIndex][0:messageposition])
            if(messageposition - 1 != len(message[messageIndex])):
                self.__ui.after(350, self.action, message, messageIndex, messageposition+1)
            elif(messageIndex + 1 != len(message)):
                self.__ui.after(1500, self.action,  message, messageIndex+1, 0)
            else:
                 self.__ui.after(2500, self.__ui.stop)
                
class AccessDenied:
     @property
     def message(self):
         return [["You are not Sam!","ACCESS DENIED"]]

class MorningGreeting:
     @property
     def message(self):
         return [["Morena, Sam","Did you have a good sleep?"],["Good morning, Sam", "Have you done your morning chores?","Eaten breakfast?\nBrushed your teeth?\nGone toilet?"]]

class BedTimeGreeting:
    @property
    def message(self):
        return [["Time to get ready for bed, Sam!","And you too Isabella!", "Have you done your night time chores?","Gone for a stinky poo \nGotten your pjs \nGot a nappy"],["Sam!!!","Absolutely!!!", "NO FARTING IN BED TONIGHT!!!"]]

class MathQuiz:
     @property
     def message(self):
         first_number = random.randrange(0,5)
         second_number = random.randrange(0,5)
         total = first_number + second_number
         return [["Ready for a maths quiz, Sam?","What does {0} + {1} equal?".format(first_number, second_number), "{0} + {1} = {2}".format(first_number, second_number,total)]]

class CapitalCities:
     @property
     def message(self):
        country = Countries().get_country()
        api_url = 'https://api.api-ninjas.com/v1/country?name={0}'.format(country)
        response = requests.get(api_url, headers={'X-Api-Key': 'rInxjc8lmjG+C0NLpIQAfg==PbQmi3w6GeiKloEU'})
        if response.status_code == requests.codes.ok:
            text = json.loads(response.text)
            return[["The capital of {0} is {1}".format(country,text[0]["capital"])]]
        else:
            return [["The capital of New Zealand is Wellington"]]

class CurrentTime:
     @property
     def message(self):
         now = datetime.now()
         current_time = now.strftime("%H:%M:%S")
         return[["The time is {0}".format(current_time)]]

class Dog:
     @property
     def image(self):
         return self.__image

     @property
     def message(self):
        dog = DogBreeds().get_breeds()
        api_url = 'https://api.api-ninjas.com/v1/dogs?name={0}'.format(dog)
        response = requests.get(api_url, headers={'X-Api-Key': 'rInxjc8lmjG+C0NLpIQAfg==PbQmi3w6GeiKloEU'})
        
        if response.status_code == requests.codes.ok:
            text =  json.loads(response.text)
            with urllib.request.urlopen("{0}".format(text[0]["image_link"])) as u:
                raw_data = u.read()
            image = Image.open(io.BytesIO(raw_data))
            self.__image = ImageTk.PhotoImage(image)
            return "This is a {0}".format(text[0]["name"])
        else:
            with urllib.request.urlopen('https://api-ninjas.com/images/dogs/golden_retriever.jpg') as u:
                raw_data = u.read()
            image = Image.open(io.BytesIO(raw_data))
            self.__image = ImageTk.PhotoImage(image)
            return "This is a {0}".format("Golden Retriever")

class DogBreeds:
    def __init__(self):
        self.__breeds = ["Cocker Spaniel","Labrador Retriever","Springer Spaniel","German Shepherd","Bull Terrier","Cavalier King Charles Spaniel","Golden Retriever","Boxer","Border Terrier"]

    def get_breeds(self):
        return random.choice(self.__breeds)

class Countries:


    def __init__(self):
        self.__countries = ["Afghanistan","Albania","Algeria",	"Andorra",	"Angola",	"Argentina",	"Armenia",	"Australia",	"Austria",	"Azerbaijan",	"Bahamas",	"Bahrain",	"Bangladesh",	"Barbados",	"Belarus",	"Belgium",	"Belize",	"Benin",	"Bhutan",	"Bolivia",	"Botswana",	"Brazil",	"Brunei",	"Bulgaria",	"Burkina Faso",	"Burundi",	"Cabo Verde",	"Cambodia",	"Cameroon",	"Canada",	"Central African Republic",	"Chad",	"Chile",	"China",	"Colombia",	"Comoros",	"Costa Rica",	"Croatia",	"Cuba",	"Cyprus",	"Denmark",	"Djibouti",	"Dominica",	"Dominican Republic",	"Ecuador",	"Egypt",	"El Salvador",	"Equatorial Guinea",	"Eritrea",	"Estonia",	"Ethiopia",	"Fiji",	"Finland",	"France",	"Gabon",	"Gambia",	"Georgia",	"Germany",	"Ghana",	"Greece",	"Grenada",	"Guatemala",	"Guinea",	"Guinea-Bissau",	"Guyana",	"Haiti",	"Holy See",	"Honduras",	"Hungary",	"Iceland",	"India",	"Indonesia",	"Iran",	"Iraq",	"Ireland",	"Israel",	"Italy",	"Jamaica",	"Japan",	"Jordan",	"Kazakhstan",	"Kenya",	"Kiribati",	"Kuwait",	"Kyrgyzstan",	"Laos",	"Latvia",	"Lebanon",	"Lesotho",	"Liberia",	"Libya",	"Liechtenstein",	"Lithuania",	"Luxembourg",	"Madagascar",	"Malawi",	"Malaysia",	"Maldives",	"Mali",	"Malta",	"Marshall Islands",	"Mauritania",	"Mauritius",	"Mexico",	"Micronesia",	"Moldova",	"Monaco",	"Mongolia",	"Montenegro",	"Morocco",	"Mozambique",	"Namibia",	"Nauru",	"Nepal",	"Netherlands",	"New Zealand",	"Nicaragua",	"Niger",	"Nigeria",	"North Korea",	"North Macedonia",	"Norway",	"Oman",	"Pakistan",	"Palau",	"Palestine State",	"Panama",	"Papua New Guinea",	"Paraguay",	"Peru",	"Philippines",	"Poland",	"Portugal",	"Qatar",	"Romania",	"Russia",	"Rwanda",	"Saint Kitts and Nevis",	"Saint Lucia",	"Saint Vincent and the Grenadines",	"Samoa",	"San Marino",	"Sao Tome and Principe",	"Saudi Arabia",	"Senegal",	"Serbia",	"Seychelles",	"Sierra Leone",	"Singapore",	"Slovakia",	"Slovenia",	"Solomon Islands",	"Somalia",	"South Africa",	"South Korea",	"South Sudan",	"Spain",	"Sri Lanka",	"Sudan",	"Suriname",	"Sweden",	"Switzerland",	"Syria",	"Tajikistan",	"Tanzania",	"Thailand",	"Timor-Leste",	"Togo",	"Tonga",	"Trinidad and Tobago",	"Tunisia",	"Turkey",	"Turkmenistan",	"Tuvalu",	"Uganda",	"Ukraine",	"United Arab Emirates",	"United Kingdom",	"United States",	"Uruguay",	"Uzbekistan",	"Vanuatu",	"Venezuela",	"Vietnam",	"Yemen",	"Zambia",	"Zimbabwe"]

    def get_country(self):
        return random.choice(self.__countries)