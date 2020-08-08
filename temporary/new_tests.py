from tkinter import *

# environment set up
root = Tk()
root.overrideredirect(False)
root.title("Scoreboard")
root.geometry("1024x600")
root.configure(background="white")
root.focus_set()
for b in range(12):
    root.grid_columnconfigure(b, minsize=85)
for i in range(6):
    root.grid_rowconfigure(i, minsize=100)

# variables
counterLeft = 0
counterRight = 0
countTotal = 0

# variables convert to StringVar
counterLeftVar = StringVar()
counterLeftVar.set(str(counterLeft))
counterRightVar = StringVar()
counterRightVar.set(str(counterRight))
counterTotalVar = StringVar()
counterTotalVar.set(str(countTotal))

# function to monitor key action
boolean = True


def keyaction(e):
    global counterLeft
    global counterRight
    global countTotal
    global BlueWon
    global boolean
    if e.char == "i":
        counterLeft += 1
        countTotal += 1
        counterLeftVar.set(str(counterLeft)), e.char
        counterTotalVar.set(str(countTotal)), e.char
    elif e.char == "o":
        counterRight += 1
        countTotal += 1
        counterRightVar.set(str(counterRight)), e.char
        counterTotalVar.set(str(countTotal)), e.char
    elif e.char == "r":
        counterLeft = counterRight = 0
        counterLeftVar.set(str(counterLeft)), e.char
        counterRightVar.set(str(counterRight)), e.char
        if totCount is None:
            totCount.destroy()


# s = Text(root, height=2, width=30).grid(column=2, row=7)
#zz = Label(root, textvariable=messageBox).grid(column=1, row=0)



# total score

#totCountLabel = Label(root, font=("Arial", 28), text="Total Score", bg="white").grid(column=3, row=1)

totCount = Label(root, font=("Arial", 48), textvariable=counterTotalVar, bg="white").grid(column=5, row=1)
# Score on the screen
left = Label(root, font=("Arial", 48), textvariable=counterLeftVar, bg="white").grid(column=4, row=3)
middle = Label(root, text=" : ", font=("Arial bold", 40), bg="white").grid(column=5, row=3)
right = Label(root, font=("Arial", 48), textvariable=counterRightVar, bg="white").grid(column=6, row=3)


if countTotal > 10:
    BlueWon = Label(root, font=("Arial", 20), text="Game Over", bg="white").grid(column=0, row=0)
elif countTotal > 0:
    BlueWon = Label(root, font=("Arial", 20), text="Game running", bg="white").grid(column=0, row=0)



def close(e):
    root.destroy(), e.char

while True:
    try:
        root.bind("<Key>", keyaction)
# root.bind("i", keyaction)
# root.bind("t", keyaction)
        root.bind("q", close)
        root.bind("<Escape>", exit)
        root.mainloop()
    except:
        exit()

