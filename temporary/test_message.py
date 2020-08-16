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
window.title("Scoreboard")
window.bgcolor("black")
window.setup(width=1024, height=600)
window.tracer(0)

# turtle set up
pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 150)
pen.write("Welcome to scoreboard!", align="center", font=("Arial", 60, "bold"))
pen.goto(0, -100)
pen.write("Please choose serving player.", align="center", font=("Arial", 60, "bold"))

while leftScore <= 40 and rightScore <= 40:
    window.update()
    if serve is None:
        z = str(input())
        if z == "q":  # command to close window
            window.bye()

        elif z == "1":
            serve = True  # serving left player
            pen.clear()
            pen.color("green")
            pen.write("> {} : {} ".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
            pen.goto(0, 220)
            pen.color("white")
            pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center", font=("Arial", 60, "bold"))
            pen.goto(0, -100)

        elif z == "2":
            serve = False  # serving right player
            pen.clear()
            pen.color("green")
            pen.write(" {} : {} <".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
            pen.goto(0, 220)
            pen.color("white")
            pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center", font=("Arial", 60, "bold"))
            pen.goto(0, -100)

    while leftScore >= 20 and rightScore >= 20:
        if serve is True:
            serve = not serve  # serving right player
        elif serve is False:
            serve = not serve  # serving left player
        count = 0
        x = str(input())
        count += 1
        if x == "r":  # reset result
            serve = None
            totalLeft = totalRight = leftScore = rightScore = count = 0
            pen.clear()
            pen.goto(0, 220)
            pen.write("New game!", align="center", font=("Arial", 60, "bold"))
            pen.goto(0, -100)
            pen.write("Who is serving ?", align="center", font=("Arial", 60, "bold"))

        elif x == "a":
            leftScore += 1
            if serve is True:
                pen.clear()
                pen.color("green")
                pen.write("> {} : {} ".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
                pen.goto(0, 220)
                pen.color("white")
                pen.color("white")
                pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
                          font=("Arial", 60, "bold"))
                pen.goto(0, -100)

                if fabs(rightScore - leftScore) == 2:   # checking for two points difference
                    pen.goto(0, -200)
                    pen.write('Left  WINS !', align="center", font=("Arial", 100, "bold"))
                    pen.goto(0, -100)
                    leftScore = rightScore = 0
                    sleep(5)
                    count = 0
                    pen.clear()
                    pen.color("green")
                    pen.write("> {} : {} ".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
                    serve = True
                    totalLeft += 1
                    pen.goto(0, 220)
                    pen.color("white")
                    pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
                              font=("Arial", 60, "bold"))
                    pen.goto(0, -100)

            elif serve is False:
                pen.clear()
                pen.color("green")
                pen.write(" {} : {} <".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
                pen.goto(0, 220)
                pen.color("white")
                pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
                          font=("Arial", 60, "bold"))
                pen.goto(0, -100)

                if fabs(leftScore - rightScore) == 2:
                    pen.goto(0, -200)
                    pen.write('Left  WINS !', align="center", font=("Arial", 100, "bold"))
                    pen.goto(0, -100)
                    leftScore = rightScore = 0
                    sleep(5)
                    count = 0
                    pen.clear()
                    pen.color("green")
                    pen.write(" {} : {} <".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
                    serve = True
                    totalLeft += 1
                    pen.goto(0, 220)
                    pen.color("white")
                    pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
                              font=("Arial", 60, "bold"))
                    pen.goto(0, -100)

        elif x == "b":
            rightScore += 1
            if serve is True:
                pen.clear()
                pen.color("green")
                pen.write("> {} : {} ".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
                pen.goto(0, 220)
                pen.color("white")
                pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
                          font=("Arial", 60, "bold"))
                pen.goto(0, -100)

                if fabs(leftScore - rightScore) == 2:  # checking for two points difference
                    pen.goto(0, -200)
                    pen.write('Right  WINS !', align="center", font=("Arial", 100, "bold"))
                    pen.goto(0, -100)
                    leftScore = rightScore = 0
                    sleep(5)
                    count = 0
                    pen.clear()
                    pen.color("green")
                    pen.write("> {} : {} ".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
                    serve = False
                    totalRight += 1
                    pen.goto(0, 220)
                    pen.color("white")
                    pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
                              font=("Arial", 60, "bold"))
                    pen.goto(0, -100)

            elif serve is False:
                pen.clear()
                pen.color("green")
                pen.write(" {} : {} <".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
                pen.goto(0, 220)
                pen.color("white")
                pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
                          font=("Arial", 60, "bold"))
                pen.goto(0, -100)

                if fabs(leftScore - rightScore) == 2:
                    pen.goto(0, -200)
                    pen.write('Right  WINS !', align="center", font=("Arial", 100, "bold"))
                    pen.goto(0, -100)
                    leftScore = rightScore = 0
                    sleep(5)
                    count = 0
                    sleep(5)
                    pen.clear()
                    pen.color("green")
                    pen.write(" {} : {} <".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
                    serve = False
                    totalRight += 1
                    pen.goto(0, 220)
                    pen.color("white")
                    pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
                              font=("Arial", 60, "bold"))
                    pen.goto(0, -100)

    if leftScore == 2:
        pen.goto(0, -200)
        pen.write('Left  WINS !', align="center", font=("Arial", 100, "bold"))
        pen.goto(0, -100)
        leftScore = rightScore = 0
        sleep(5)
        count = 0
        totalLeft += 1
        pen.clear()
        pen.color("green")
        pen.write("> {} : {} ".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
        pen.goto(0, 220)
        pen.color("white")
        pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center", font=("Arial", 60, "bold"))
        pen.goto(0, -100)

    elif rightScore == 2:
        pen.goto(0, -200)
        pen.write('Right  WINS !', align="center", font=("Arial", 100, "bold"))
        pen.goto(0, -100)
        rightScore = leftScore = 0
        sleep(5)
        count = 0
        totalRight += 1
        pen.clear()
        pen.color("green")
        pen.write(" {} : {} <".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
        pen.goto(0, 220)
        pen.color("white")
        pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center", font=("Arial", 60, "bold"))
        pen.goto(0, -100)

    else:
        x = str(input())
        count += 1
        if x == "r":  # reset result
            serve = None
            totalLeft = totalRight = leftScore = rightScore = count = 0
            pen.clear()
            pen.goto(0, 220)
            pen.write("New game!", align="center", font=("Arial", 60, "bold"))
            pen.goto(0, -100)
            pen.write("Who is serving ?", align="center", font=("Arial", 60, "bold"))

        elif x == "a":
            leftScore += 1
            if serve is True:
                pen.clear()
                pen.color("green")
                pen.write("> {} : {} ".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
                pen.goto(0, 220)
                pen.color("white")
                pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
                          font=("Arial", 60, "bold"))
                pen.goto(0, -100)
                if count == 4:
                    serve = not serve
                    count = -1

            elif serve is False:
                pen.clear()
                pen.color("green")
                pen.write(" {} : {} <".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
                pen.goto(0, 220)
                pen.color("white")
                pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
                          font=("Arial", 60, "bold"))
                pen.goto(0, -100)
                if count == 4:
                    serve = not serve
                    count = -1

        elif x == "b":
            rightScore += 1
            if serve is True:
                pen.clear()
                pen.color("green")
                pen.write("> {} : {} ".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
                pen.goto(0, 220)
                pen.color("white")
                pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
                          font=("Arial", 60, "bold"))
                pen.goto(0, -100)
                if count == 4:
                    serve = not serve
                    count = -1

            elif serve is False:
                pen.clear()
                pen.color("green")
                pen.write(" {} : {} <".format(leftScore, rightScore), align="center", font=("Arial", 200, "bold"))
                pen.goto(0, 220)
                pen.color("white")
                pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
                          font=("Arial", 60, "bold"))
                pen.goto(0, -100)
                if count == 4:
                    serve = not serve
                    count = -1

        elif x == "q":  # close window
            window.bye()
