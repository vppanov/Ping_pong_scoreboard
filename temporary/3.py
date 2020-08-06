from tkinter import *

root = Tk()
root.title(' Canvas')

root.geometry("1024x600")
counter = 100
w = 1024
h = 600
x = w//2
y = h//2
my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack()

oval = my_canvas.create_rectangle(x, y, x+10, y+10)
my_canvas.pack()


def score(root):
    global counter
    my_canvas.delete(root)
    square = my_canvas.create_rectangle(200,150, x-350, y-250, fill="white")
    counter += 1
    my_text = my_canvas.create_text(124, 50, text=str(counter), font=("Arial", 48))
    my_canvas.delete(root)



score(root)

root.bind("i", score)
root.bind("q", exit)
root.mainloop()