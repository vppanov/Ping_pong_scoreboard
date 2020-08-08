from tkinter import *

class Window():

    def __init__(self, root):

        self.top = Label(root, text = "Test")
        self.top.pack()

        self.e = Entry(root)
        self.e.pack()
        self.e.focus_set()

        self.b = Button(root, text = "Enter", command = self.function)
        self.b.pack()

        self.answer = StringVar()
        self.answer.set("Enter answer")

        self.check = Label(root, text = self.answer.get(), textvariable = self.answer)
        self.check.pack()


otgovor = StringVar()
otgovor.set("Proba")

textt = Label(root, text= self.answer.get(),  )
textt.pack()

    #Functions
    def function(self):

        data = self.e.get()

        if data == "5":
            self.answer.set("Correct")
        else:
            self.answer.set("Incorrect")

root = Tk()
w = Window(root)
root.mainloop()