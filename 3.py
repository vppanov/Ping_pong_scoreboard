from tkinter import *

import tkinter.font as tkFont

win = Tk()

myFont = tkFont.Font(family = "Comic Sans", size = 36, weight = "bold")


def exitProgram():
    print ("Exiting")
    
    win.quit()

win.title("Scoreboard")
win.geometry("800x480")
win.configure(background="black")



exitButton = Button(win, text = "Exit", font = myFont, command = exitProgram, height = 2, width = 6)
exitButton.pack()

win.mainloop()





