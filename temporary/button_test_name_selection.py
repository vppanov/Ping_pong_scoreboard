

from time import sleep
from turtle import Screen, Turtle
import RPi.GPIO as GPIO
from gpiozero import Button
buttonA = Button(16)
buttonB = Button(26)

# variable for the game
player1 = False
player2 = None
playerNames = ["Веско", "Сашо", "Гери", "Георги", "Ивайло", "Друг"]
player1_id = None
player2_id = None
posCount = 0
positionY = 100
positionX = -350
positionX2 = 100
positionY2 = 100

# window screen set up
window = Screen()
window.title("Table tennis scoreboard")
window.bgcolor("white")
window.setup(width=1024, height=600)


# turtle set up
pen = Turtle()
pen.speed(0)
pen.color("black")
pen.shape("circle")
pen.hideturtle()
pen.down()
pen.up()


def setplayer(e):
    global positionY
    if 0 < posCount <= 3:
        red_position = positionY + 100
        pen.color("red")
        pen.begin_fill()
        pen.goto(positionX, red_position)
        pen.down()
        pen.circle(35)
        pen.end_fill()
        pen.up()
        pen.goto(0, 200)
        pen.write("Player selected", align="center", font=("Arial", 60, "bold"))
        e = not e
        return e

    elif 3 < posCount <= 5:
        red_position2 = positionY2 + 100
        pen.color("red")
        pen.begin_fill()
        pen.goto(positionX2, red_position2)
        pen.down()
        pen.circle(35)
        pen.end_fill()
        pen.up()
        pen.goto(0, 200)
        pen.write("Player selected", align="center", font=("Arial", 60, "bold"))
        e = not e
        return e
    elif posCount == 0:
        pen.color("red")
        pen.begin_fill()
        pen.goto(100, -100)
        pen.down()
        pen.circle(35)
        pen.end_fill()
        pen.up()
        pen.goto(0, 200)
        pen.write("Player selected", align="center", font=("Arial", 60, "bold"))
        e = not e
        return e


def printnames():
    pen.color("black")
    pen.goto(-200, 100)
    pen.write("Веско", align="center", font=("Arial", 60, "bold"))
    pen.goto(-200, 0)
    pen.write("Сашо", align="center", font=("Arial", 60, "bold"))
    pen.goto(-200, -100)
    pen.write("Гери", align="center", font=("Arial", 60, "bold"))
    pen.goto(300, 100)
    pen.write("Георги", align="center", font=("Arial", 60, "bold"))
    pen.goto(300, 0)
    pen.write("Ивайло", align="center", font=("Arial", 60, "bold"))
    pen.goto(300, -100)
    pen.write("Друг", align="center", font=("Arial", 60, "bold"))


def position():
    global positionY, positionX, positionX2, positionY2, posCount
    if posCount <= 3:
        pen.color("yellow")
        pen.begin_fill()
        pen.goto(positionX, positionY)
        pen.down()
        pen.circle(35)
        pen.end_fill()
        pen.up()
        positionY -= 100
    elif 3 < posCount <= 5:
        pen.color("yellow")
        pen.begin_fill()
        pen.goto(positionX2, positionY2)
        pen.down()
        pen.circle(35)
        pen.end_fill()
        pen.up()
        positionY2 -= 100
    elif posCount >= 6:
        pen.color("yellow")
        pen.begin_fill()
        pen.goto(positionX2, positionY2)
        pen.down()
        pen.circle(35)
        pen.end_fill()
        pen.up()
        positionY2 -= 100
        posCount = 0
        positionY = 100
        positionX = -350
        positionX2 = 100
        positionY2 = 100



while True:
    window.update()
    sleep(0.3)
    while player1 is not True or player2 is not True:
        printnames()

        if buttonA.is_active and player1 is False:
            posCount += 1
            pen.clear()
            printnames()
            position()
        elif buttonB.is_active and player1 is False:
            player2 = False
            if positionY == 100 and posCount > 0:
                player1 = setplayer(player1)
                player1_id = playerNames.index("Веско")
                sleep(3)
                pen.clear()
            elif positionY == 0:
                player1 = setplayer(player1)
                player1_id = playerNames.index("Сашо")
                sleep(3)
                pen.clear()
            elif positionY == -100:
                player1 = setplayer(player1)
                player1_id = playerNames.index("Гери")
                sleep(3)
                pen.clear()
            elif positionY2 == 100 and posCount > 0:
                player1 = setplayer(player1)
                player1_id = playerNames.index("Георги")
                sleep(3)
                pen.clear()
            elif positionY2 == 0:
                player1 = setplayer(player1)
                player1_id = playerNames.index("Ивайло")
                sleep(3)
                pen.clear()
            else:
                player1 = setplayer(player1)
                player1_id = playerNames.index("Друг")
                sleep(3)
                pen.clear()
        elif buttonA.is_active and player2 is False:
            posCount += 1
            pen.clear()
            printnames()
            position()
        elif buttonB.is_active and player2 is False:
            if positionY == 100 and posCount > 0:
                player2 = setplayer(player2)
                player2_id = playerNames.index("Веско")
                sleep(3)
                pen.clear()
            elif positionY == 0:
                player2 = setplayer(player2)
                player2_id = playerNames.index("Сашо")
                sleep(3)
                pen.clear()
            elif positionY == -100:
                player2 = setplayer(player2)
                player2_id = playerNames.index("Гери")
                sleep(3)
                pen.clear()
            elif positionY2 == 100 and posCount > 0:
                player2 = setplayer(player2)
                player2_id = playerNames.index("Георги")
                sleep(3)
                pen.clear()
            elif positionY2 == 0:
                player2 = setplayer(player2)
                player2_id = playerNames.index("Ивайло")
                sleep(3)
                pen.clear()
            else:
                player2 = setplayer(player2)
                player2_id = playerNames.index("Друг")
                sleep(3)
                pen.clear()


window.mainloop()
