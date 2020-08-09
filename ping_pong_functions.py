# # #        TO DO LIST
# 1. Create a player selection screen. Use the turtle pen with different shape for selection and display player names.
# 2. Update reset function when we have a player selection screen
# 3. Add player IDs + names and add match information to table
# 4. Use time to record match duration and append it to table
# 5. Prepare a page with statistics and best players for the moment


from time import sleep
from turtle import Screen, Turtle
from math import fabs

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
window.bgcolor("black")
window.setup(width=1024, height=600)
window.tracer(0)

# turtle set up
pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()

#  welcome messages
pen.goto(0, 150)
pen.write("Welcome to scoreboard!", align="center", font=("Arial", 60, "bold"))
pen.goto(0, -100)
pen.write("Please choose serving player.", align="center", font=("Arial", 60, "bold"))

# definitions of game functions
def resetscore():
    global serve, totalLeft, totalRight, leftScore, rightScore, count
    serve = None
    totalLeft = totalRight = leftScore = rightScore = count = 0
    pen.clear()
    pen.goto(0, 220)
    pen.write("New game!", align="center", font=("Arial", 60, "bold"))
    pen.goto(0, -100)
    pen.write("Who is serving ?", align="center", font=("Arial", 60, "bold"))


def serveistrue():
    global leftScore, rightScore, totalLeft, totalRight
    pen.clear()
    pen.color("green")
    pen.write("> {} : {} ".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
    pen.goto(0, 220)
    pen.color("white")
    pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
              font=("Arial", 60, "bold"))
    pen.goto(0, -100)


def serveisfalse():
    global leftScore, rightScore, totalLeft, totalRight
    pen.clear()
    pen.color("green")
    pen.write(" {} : {} <".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
    pen.goto(0, 220)
    pen.color("white")
    pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
              font=("Arial", 60, "bold"))
    pen.goto(0, -100)


def servicecheck():
    global serve, count
    if count == 4:
        serve = not serve
        count = -1  # resetting the counter to negative number to handle service turn


def rightwins():
    global rightScore, leftScore, count, totalRight, totalLeft
    totalRight += 1
    rightScore = leftScore = count = 0
    pen.goto(0, -200)
    pen.write('Right  WINS !', align="center", font=("Arial", 100, "bold"))
    pen.goto(0, -100)
    sleep(5)
    pen.clear()
    pen.color("green")
    pen.write(" {} : {} <".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
    pen.goto(0, 220)
    pen.color("white")
    pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center", font=("Arial", 60, "bold"))
    pen.goto(0, -100)


def leftwins():
    global totalLeft, totalRight, leftScore, rightScore, count
    totalLeft += 1
    leftScore = rightScore = count = 0
    pen.goto(0, -200)
    pen.write('Left  WINS !', align="center", font=("Arial", 100, "bold"))
    pen.goto(0, -100)
    sleep(5)
    pen.clear()
    pen.color("green")
    pen.write("> {} : {} ".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
    pen.goto(0, 220)
    pen.color("white")
    pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
              font=("Arial", 60, "bold"))
    pen.goto(0, -100)


def servingturndisplay():
    global serve, leftScore, rightScore, totalLeft, totalLeft
    if serve:
        pen.clear()
        pen.color("green")
        pen.write("> {} : {} ".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
        pen.goto(0, 220)
        pen.color("white")
        pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center", font=("Arial", 60, "bold"))
        pen.goto(0, -100)
    elif not serve:
        pen.clear()
        pen.color("green")
        pen.write(" {} : {} <".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
        pen.goto(0, 220)
        pen.color("white")
        pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center", font=("Arial", 60, "bold"))
        pen.goto(0, -100)


def wronginput():
    global count
    count -= 1
    pen.goto(0, 150)
    pen.write("Wrong input ", align="center", font=("Arial", 60, "bold"))
    pen.goto(0, -100)

# game logic
while leftScore <= 40 and rightScore <= 40:  # maximum points
    window.update()
    if serve is None:
        z = str(input())
        if z == "q":  # command to close window
            window.bye()
        elif z == "1":
            serve = True  # serving left player
            servingturndisplay()
        elif z == "2":
            serve = False  # serving right player
            servingturndisplay()
    while leftScore >= 20 and rightScore >= 20:  # handling overtime
        if serve is True:
            serve = not serve  # switching serving player to right player
        elif serve is False:
            serve = not serve  # switching serving player to left player
        count = 0
        x = str(input())
        count += 1
        if x == "r":  # reset result
            resetscore()
        elif x == "4":  # point for left player
            leftScore += 1
            if serve is True:
                serveistrue()
                if fabs(rightScore - leftScore) == 2:  # checking for two points difference
                    leftwins()  # game ends
                    serve = True  # assigning serve turn for next game
            elif serve is False:
                serveisfalse()
                if fabs(leftScore - rightScore) == 2:
                    leftwins()
                    serve = True  # assigning serve turn for next game
        elif x == "5":  # point for right  player
            rightScore += 1
            if serve is True:
                serveistrue()
                if fabs(leftScore - rightScore) == 2:  # checking for two points difference
                    rightwins()
                    serve = False
            elif serve is False:
                serveisfalse()
                if fabs(leftScore - rightScore) == 2:  # checking for two points difference
                    rightwins()
                    serve = False
        else:
            wronginput()  # handling wrong keyboard input
    if leftScore == 21:  # left wins
        leftwins()
    elif rightScore == 21:  # right wins
        rightwins()
    else:
        x = str(input())
        count += 1
        if x == "r":  # reset result
            resetscore()
        elif x == "4":  # point for left player
            leftScore += 1
            if serve is True:
                serveistrue()
                servicecheck()
            elif serve is False:
                serveisfalse()
                servicecheck()
        elif x == "5":  # point for right  player
            rightScore += 1
            if serve is True:
                serveistrue()
                servicecheck()
            elif serve is False:
                serveisfalse()
                servicecheck()
        elif x == "q":  # close program
            window.bye()
        else:
            wronginput() # handling wrong keyboard input
