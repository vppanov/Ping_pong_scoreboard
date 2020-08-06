from tkinter import *




global counter
counter = 100
root = Tk()
root.overrideredirect(True)
my_label = Label(root, text="", font=("Arial", 48))
my_label.pack()

testVar = StringVar()
testVar.set(str(counter))
def exitProgram():
    print("Exiting")

def counterIn(e):
    global counter
    counter += 1
    testVar.set(str(counter)), e.char


y = Label(root, font=("Arial", 48), textvariable=testVar)
y.pack()

#    my_label.update()
 #   my_label = Label(root, text=counter, font=("Arial", 48))
  #  my_label.pack()


BlueButton = Button(root, text="Blue Point", bg="white", fg="yellow", width=10, height=10, command=counterIn)
BlueButton.pack()


y = Label(root, font=("Arial", 48), textvariable=testVar)
y.pack()



def exit(event):
    root.destroy()

root.title("Scoreboard")
root.geometry("800x480")
root.configure(background="white")

exitButton = Button(root, text="Exit", command=exitProgram, height=2, width=6)
exitButton.pack()
root.bind("i", counterIn)
root.bind("t", counterIn)
root.bind("q", exit)
root.mainloop()





