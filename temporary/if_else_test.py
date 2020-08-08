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
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
pen.write("Who is serving ?")

def addBlue():
    global BlueScore
    BlueScore += 1

def addRed():
    global RedScore
    RedScore += 1

while RedScore <= 21 and BlueScore <= 21:
    root.update()
    pen.write(f"{RedScore} : {BlueScore} <", align="center", font=("Courier", 80, "bold"))


def close():
    root.bye()


