from ctypes import alignment
from tkinter import *
from turtle import color
from PIL import ImageTk, Image
import urllib.request
import io

class GuiTest:

    def __init__(self) -> None:
        self.__root = Tk()
        self.__greetingLabel = Label(font=('Times', 36,'bold'), bg="black", fg="white",  text="this is a test of the string position \ntest position here \nloreum ipsum", anchor="w", justify="left")
        self.__greetingLabel.place(x=650,y=250)
        with urllib.request.urlopen('https://api-ninjas.com/images/dogs/golden_retriever.jpg') as u:
            raw_data = u.read()
        image = Image.open(io.BytesIO(raw_data))
        self.__image = ImageTk.PhotoImage(image)
        #self.__imagelab = Label(self.__root,image=self.__image)
        # # self.__imagelab.place(x=450,y=450)
        self.__greetingLabel.config( text='Hello',image=self.__image,compound='bottom')
        self.__root.configure(bg="black")
        self.__root.wm_attributes("-topmost", True)
        #self.__root.geometry("500x500")
        self.__root.wm_attributes("-fullscreen", True)
        self.__root.mainloop()

    


if __name__ == "__main__":
    GuiTest()
        