from ctypes import alignment
from tkinter import *
from turtle import color

class GuiTest:

    def __init__(self) -> None:
        self.__root = Tk()
        self.__greetingLabel = Label(font=('Times', 24), bg="black", fg="white", text="this is a test of the string position \ntest position here \nloreum ipsum", anchor="w", justify="left")
        self.__greetingLabel.place(x=10,y=10)
        self.__root.configure(bg="black")
        self.__root.wm_attributes("-topmost", True)
        #self.__root.geometry("500x500")
        self.__root.wm_attributes("-fullscreen", True)
        self.__root.mainloop()


if __name__ == "__main__":
    GuiTest()
        