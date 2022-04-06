from ctypes import alignment
from tkinter import *

class GuiTest:

    def __init__(self) -> None:
        self.__root = Tk()
        self.__greetingLabel = Label(font=('Times', 24), text="this is a test of the string position \ntest position here \nloreum ipsum", anchor="w", justify="left")
        self.__greetingLabel.place(x=10,y=10)
        
        self.__root.wm_attributes("-topmost", True)
        self.__root.geometry("500x500")
        self.__root.mainloop()


if __name__ == "__main__":
    GuiTest()
        