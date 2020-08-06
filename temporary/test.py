from tkinter import *

# environment set up
root = Tk()
root.overrideredirect(True)
root.title("Scoreboard")
root.geometry("1024x600")
root.columnconfigure(1, minsize=15)
root.configure(background="white")


# variables
counter = 100
counter2 = 0

# variables convert to StringVar
testVar = StringVar()
testVar.set(str(counter))
testVar2 = StringVar()
testVar2.set(str(counter2))

# function to monitor key action


def keyaction(e):
    global counter
    global counter2
    if e.char == "t":
        counter += 1
        testVar.set(str(counter)), e.char
    elif e.char == "i":
        counter2 += 1
        testVar2.set(str(counter2)), e.char


# def counterin2(z):
#    global counter2
#    counter2 += 1
#    testVar2.set(str(counter2)), z.char


# BlueButton = Button(root, text="Blue Point", bg="white", fg="yellow", width=10, height=10, command=keyaction)
# BlueButton.pack()

y2 = Label(root, font=("Arial", 48), textvariable=testVar2).place(x=288, y=275)

y = Label(root, font=("Arial", 28), textvariable=testVar).place(x=625, y=275)



def close(e):
    root.destroy(), e.char


root.bind("<Key>", keyaction)
# root.bind("i", keyaction)
# root.bind("t", keyaction)
root.bind("q", close)
root.mainloop()
