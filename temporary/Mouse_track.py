from tkinter import Tk, Label

root = Tk()
root.geometry("1024x600")
def motion(event):
    x, y = event.x, event.y
    w = Label(root, text='{}, {}'.format(x, y))
    w.place(x=70, y=90)
    print('{}, {}'.format(x, y))

root.bind('<Motion>', motion)
root.mainloop()