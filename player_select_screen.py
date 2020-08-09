
from time import sleep
from turtle import Screen, Turtle

# variable for the game

count = 0
leftScore = 0
rightScore = 0
serve = None
totalLeft = 0
totalRight = 0

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


#  writing names
player1 = False
player2 = False
playerNames = ["Веско", "Сашо", "Гери"]
player1_id = None
player2_id = None
posCount = 0

def setplayer(e):
    global positiony
    position = positiony + 100
    pen.color("red")
    pen.begin_fill()
    pen.goto(-200, position)
    pen.down()
    pen.circle(35)
    pen.end_fill()
    pen.up()
    pen.goto(0, 200)
    pen.write("Player selected", align="center", font=("Arial", 60, "bold"))
    pen.goto(0, -100)
    positiony = 100
    e = not e
    return e

def printnames():
    pen.color("black")
    pen.goto(0, 100)
    pen.write("Веско", align="center", font=("Arial", 60, "bold"))
    pen.goto(0, 0)
    pen.write("Сашо", align="center", font=("Arial", 60, "bold"))
    pen.goto(0, -100)
    pen.write("Гери", align="center", font=("Arial", 60, "bold"))

def printcircle():
    pen.color("yellow")
    pen.begin_fill()
    pen.goto(-200, positiony)
    pen.down()
    pen.circle(35)
    pen.end_fill()
    pen.up()



positiony = 100
positiony2 = 100
while True:
    window.update()
    while player1 is not True or player2 is not True:
        printnames()
        x = input(str(input))
        if x == "n" and player1 is False:
            pen.clear()
            printnames()
            printcircle()
            positiony -= 100
        elif x == "o" and player1 is False:
            if positiony == 0:
                player1 = setplayer(player1)
                player1_id = playerNames.index("Веско")
                sleep(4)
                pen.clear()
            elif positiony == -100:
                player1 = setplayer(player1)
                player1_id = playerNames.index("Сашо")
                sleep(4)
                pen.clear()
            elif positiony == -200:
                player1 = setplayer(player1)
                player1_id = playerNames.index("Гери")
                sleep(4)
                pen.clear()
        elif x == "n" and player2 is False:
            pen.clear()
            printnames()
            printcircle()
            positiony -= 100
        elif x == "o" and player2 is False:
            if positiony == 0:
                player2 = setplayer(player2)
                player2_id = playerNames.index("Веско")
                sleep(4)
                pen.clear()
            elif positiony == -100:
                player2 = setplayer(player2)
                player2_id = playerNames.index("Сашо")
                sleep(4)
                pen.clear()
            elif positiony == -200:
                player2 = setplayer(player2)
                player2_id = playerNames.index("Гери")
                sleep(4)
                pen.clear()



window.mainloop()
