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
        # self.__greeting = CapitalCities()
        self.__randomGreetings = [CapitalCities,MathQuiz]

    def execute(self):
        current_time = datetime.now().time()
        school_finish = time(15,0,0)
        school_start = time(9,0)

        # if school_start < current_time < school_finish:
        self.__greeting  = MorningGreeting()
        # self.__greeting = random.choice(self.__randomGreetings)()
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
                 self.__ui.after(2500, self.__ui.stop)
                

class GenericGreeting:

     @property
     def message(self):
         return ["Hi, Sam!"]

class MorningGreeting:
     @property
     def message(self):
         return ["Good morning, Sam", "Have you done your morning chores?","Eaten breakfast?,\nBrushed teeth?\nGone toilet?"]

class MathQuiz:
     @property
     def message(self):
         first_number = random.randrange(0,5)
         second_number = random.randrange(0,5)
         total = first_number + second_number
         return ["Ready for a math quiz, Sam?","What is {0} + {1}?".format(first_number, second_number), "{0} + {1} = {2}".format(first_number, second_number,total)]

class CapitalCities:
     @property
     def message(self):
        country = Countries().get_country()
        api_url = 'https://api.api-ninjas.com/v1/country?name={0}'.format(country)
        response = requests.get(api_url, headers={'X-Api-Key': 'rInxjc8lmjG+C0NLpIQAfg==PbQmi3w6GeiKloEU'})
        if response.status_code == requests.codes.ok:
            text = json.loads(response.text)
            return["The capital of {0} is {1}".format(country,text[0]["capital"])]
        else:
            return ["The capital of New Zealand is Wellington"]

       

class Countries:


    def __init__(self):
        self.__countries = ["Afghanistan","Albania","Algeria",	"Andorra",	"Angola",	"Argentina",	"Armenia",	"Australia",	"Austria",	"Azerbaijan",	"Bahamas",	"Bahrain",	"Bangladesh",	"Barbados",	"Belarus",	"Belgium",	"Belize",	"Benin",	"Bhutan",	"Bolivia",	"Botswana",	"Brazil",	"Brunei",	"Bulgaria",	"Burkina Faso",	"Burundi",	"Cabo Verde",	"Cambodia",	"Cameroon",	"Canada",	"Central African Republic",	"Chad",	"Chile",	"China",	"Colombia",	"Comoros",	"Costa Rica",	"Croatia",	"Cuba",	"Cyprus",	"Denmark",	"Djibouti",	"Dominica",	"Dominican Republic",	"Ecuador",	"Egypt",	"El Salvador",	"Equatorial Guinea",	"Eritrea",	"Estonia",	"Ethiopia",	"Fiji",	"Finland",	"France",	"Gabon",	"Gambia",	"Georgia",	"Germany",	"Ghana",	"Greece",	"Grenada",	"Guatemala",	"Guinea",	"Guinea-Bissau",	"Guyana",	"Haiti",	"Holy See",	"Honduras",	"Hungary",	"Iceland",	"India",	"Indonesia",	"Iran",	"Iraq",	"Ireland",	"Israel",	"Italy",	"Jamaica",	"Japan",	"Jordan",	"Kazakhstan",	"Kenya",	"Kiribati",	"Kuwait",	"Kyrgyzstan",	"Laos",	"Latvia",	"Lebanon",	"Lesotho",	"Liberia",	"Libya",	"Liechtenstein",	"Lithuania",	"Luxembourg",	"Madagascar",	"Malawi",	"Malaysia",	"Maldives",	"Mali",	"Malta",	"Marshall Islands",	"Mauritania",	"Mauritius",	"Mexico",	"Micronesia",	"Moldova",	"Monaco",	"Mongolia",	"Montenegro",	"Morocco",	"Mozambique",	"Namibia",	"Nauru",	"Nepal",	"Netherlands",	"New Zealand",	"Nicaragua",	"Niger",	"Nigeria",	"North Korea",	"North Macedonia",	"Norway",	"Oman",	"Pakistan",	"Palau",	"Palestine State",	"Panama",	"Papua New Guinea",	"Paraguay",	"Peru",	"Philippines",	"Poland",	"Portugal",	"Qatar",	"Romania",	"Russia",	"Rwanda",	"Saint Kitts and Nevis",	"Saint Lucia",	"Saint Vincent and the Grenadines",	"Samoa",	"San Marino",	"Sao Tome and Principe",	"Saudi Arabia",	"Senegal",	"Serbia",	"Seychelles",	"Sierra Leone",	"Singapore",	"Slovakia",	"Slovenia",	"Solomon Islands",	"Somalia",	"South Africa",	"South Korea",	"South Sudan",	"Spain",	"Sri Lanka",	"Sudan",	"Suriname",	"Sweden",	"Switzerland",	"Syria",	"Tajikistan",	"Tanzania",	"Thailand",	"Timor-Leste",	"Togo",	"Tonga",	"Trinidad and Tobago",	"Tunisia",	"Turkey",	"Turkmenistan",	"Tuvalu",	"Uganda",	"Ukraine",	"United Arab Emirates",	"United Kingdom",	"United States",	"Uruguay",	"Uzbekistan",	"Vanuatu",	"Venezuela",	"Vietnam",	"Yemen",	"Zambia",	"Zimbabwe"]

    def get_country(self):
        return random.choice(self.__countries)