from time import sleep
import turtle

# variable for the game
count = 0
score_b = 0
RedScore = 0
BlueScore = 0
scoreCount = 0
leftServe = 0
rightServe = 0

root = turtle.Screen()
root.title("Scoreboard")
root.bgcolor("black")
root.setup(width=800, height=600)

pen = turtle.Turtle()


pen.color("white")

pen.goto(0, 0)
root.update()

root.tracer(False)
dist = 2
for i in range(200):
    pen.forward(dist)
    pen.right(90)
    dist += 2

root.update()
root.mainloop()