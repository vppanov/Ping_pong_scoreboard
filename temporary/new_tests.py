from tkinter import *
from tkinter import ttk


# environment set up


root = Tk()
content = ttk.Frame(root)
frame = ttk.Frame(borderwidth=3)

root.overrideredirect(False)
root.title("Scoreboard")
root.geometry("1024x600")
root.configure(background="white")
for b in range(12):
    root.columnconfigure(b, weight=10)
for i in range(6):
    root.rowconfigure(i, weight=10)

# variables
counter = 100
counter2 = 10
countkey = 0

# variables convert to StringVar
testVar = StringVar()
testVar.set(str(counter))
testVar2 = StringVar()
testVar2.set(str(counter2))
testVar3 = StringVar()
testVar3.set(str(countkey))

# function to monitor key action
otgovor = StringVar()
otgovor.set("oooo")


def keyaction(e):
    global counter
    global counter2
    global countkey

    if e.char == "t":
        counter += 1
        countkey += 1
        testVar.set(str(counter)), e.char
        testVar3.set(str(countkey)), e.char

    elif e.char == "i":
        counter2 += 1
        countkey += 1
        testVar2.set(str(counter2)), e.char
        testVar3.set(str(countkey)), e.char
    elif e.char == "r":
        counter = counter2 = 0
        testVar.set(str(counter)), e.char
        testVar2.set(str(counter2)), e.char

def turns():
    global countkey
    countkey = 0
    global root
    if countkey < 10:
        otgovor.set(">")

    else:
        otgovor.set("dsfsdfsdf")



s = Text(root, height=2, width=30)
s.grid(column=2, row=7)
s.insert(END, "testsadadadasg")





# def counterin2(z):
#    global counter2
#    counter2 += 1
#    testVar2.set(str(counter2)), z.char


# BlueButton = Button(root, text="Blue Point", bg="white", fg="yellow", width=10, height=10, command=keyaction)
# BlueButton.pack()


y2 = Label(root, font=("Arial", 48), textvariable=testVar2, bg="white").grid(column=0, row=4)
y3 = Label(root, font=("Arial", 48), textvariable=testVar3, bg="white").grid(column=1, row=1)
y = Label(root, font=("Arial", 28), textvariable=testVar, bg="white").grid(column=2, row=3)

Text()

def close(e):
    root.destroy(), e.char

zz = Label(root, text=otgovor.get(), textvariable=otgovor).grid(column=1, row=5)


root.bind("<Key>", keyaction)

# root.bind("i", keyaction)
# root.bind("t", keyaction)
root.bind("q", close)
root.mainloop()
