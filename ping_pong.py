#!/usr/bin/python3
try:
    import tkinter as tk

except:
    print("You need Python 3.8 installed and Python Tkinter. This script will automatically install dependencies... :]")
    import os

    os.system('sudo apt-get install python3.8 python3-tk')
    import tkinter as tk
from time import sleep
window = tk.Tk()

window.configure(bg='black')
window.geometry('1024x600')
window.overrideredirect(True)

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

scoreRed = 0
scoreBlue = 0

global BlueWonBoolean
global RedWonBoolean
BlueWonBoolean = False
RedWonBoolean = False

RedText = tk.StringVar()
BlueText = tk.StringVar()

RedText.set(str(scoreRed))
BlueText.set(str(scoreBlue))



def addBlue():
    global scoreBlue
    scoreBlue += 1
    BlueText.set(str(scoreBlue))
    if scoreBlue == 21:
        global BlueWonBoolean
        BlueWonBoolean = True
        print("\nBlue Won!!!\nBLUE | RED\n " + str(scoreBlue) + "  :  " + str(scoreRed))



        global BlueWon
        BlueWon = tk.Label(text="Blue Won!!!",
                           foreground="white",
                           background="black",
                           width=10,
                           height=10)
        BlueWon.pack(side=tk.TOP, fill=tk.X)


def addRed():
    global scoreRed
    scoreRed += 1
    RedText.set(str(scoreRed))
    if scoreRed == 21:
        global RedWonBoolean
        RedWonBoolean = True
        print("\nRed Won!!!\nRED | BLUE\n" + str(scoreRed) + "  :  " + str(scoreBlue))

        global RedWon
        RedWon = tk.Label(text="Red Won!!!",
                          foreground="white",
                          background="black",
                          width=10,
                          height=10)
        RedWon.pack(side=tk.TOP, fill=tk.X)


def resetScore():
    global scoreRed
    global scoreBlue
    global BlueWonBoolean
    global RedWonBoolean
    scoreRed = 0
    scoreBlue = 0
    RedText.set(str(scoreRed))
    BlueText.set(str(scoreBlue))
    BlueLabel.pack(side=tk.LEFT, fill=tk.X)
    RedLabel.pack(side=tk.RIGHT, fill=tk.X)

    if BlueWonBoolean == True:
        BlueWon.destroy()
        BlueWonBoolean = False
    elif RedWonBoolean == True:
        RedWon.destroy()
        RedWonBoolean = False

    BlueButton = tk.Button(window, text="Blue Point", bg="white", fg="yellow", width=30, height=15, command=addBlue)
    RedButton = tk.Button(window, text="Red Point", bg="red", fg="black", width=30, height=15, command=addRed)
    ResetButton = tk.Button(window, text="Reset", width=10, height=3, command=resetScore)

    BlueLabel.pack(side=tk.LEFT, fill=tk.X)
    RedLabel.pack(side=tk.RIGHT, fill=tk.X)




while True:
    try:

        BlueLabel = tk.Label(
            textvariable=BlueText,
            foreground="white",
            background="black",
            width=10,
            height=5
        )

        RedLabel = tk.Label(
            textvariable=RedText,
            foreground="white",
            background="black",
            width=10,
            height=5
        )

        BlueButton = tk.Button(window, text="Blue Point", bg="black", fg="WHITE", width=30, height=15, command=addBlue)
        RedButton = tk.Button(window, text="Red Point", bg="black", fg="WHITE", width=30, height=15, command=addRed)
        ResetButton = tk.Button(window, text="Reset", bg="black", fg="WHITE", width=10, height=3, command=resetScore)


        # image = tk.PhotoImage(file="cornHole.png")
        # imageLabel = tk.Label(image=image)

        BlueLabel.pack(side=tk.LEFT, fill=tk.X)
        RedLabel.pack(side=tk.RIGHT, fill=tk.X)

        BlueButton.pack(side=tk.LEFT, fill=tk.X)
        RedButton.pack(side=tk.RIGHT, fill=tk.X)
        # imageLabel.pack(side=tk.TOP, fill=tk.X)

        ResetButton.pack(side=tk.TOP, fill=tk.X)
        window.bind("<Escape>", exit)
        window.mainloop()
    except:
        exit()




