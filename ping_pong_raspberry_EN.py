from time import sleep
from turtle import Screen, Turtle
from math import fabs, ceil
from sqlite3 import connect
from datetime import date
from timeit import default_timer
from random import choice
from gpiozero import Button

# buttons

buttonA = Button(16)
buttonB = Button(26)
buttonC = Button(10)  # TBD
buttonD = Button(11)  # TBD

# database creation

exec(open('system/database.py').read())  # executing database creation file

# variable for the game
count = 0
leftScore = 0
rightScore = 0
serve = [True, False]
totalLeft = 0
totalRight = 0
player1 = False
player2 = False
player3 = None
player4 = None
playerNames = ["John", "Tim", "Andy", "Thomas", "Adam", "Guest"]
player1_id = None
player2_id = None
player3_id = None
player4_id = None
posCount = 0
positionY = 100
positionX = -350
positionX2 = 100
positionY2 = 100
match_duration = None
game_state = 0
gamepoints = 0
servechange = 0
penalties = 0
start_game = None
doubles = None
DATABASE_NAME = 'system/stats.db'

# # # Game states ####
# 0 - choose game play
# 50 - choose game type
# 100 - choose game size
# 150 - choose players
# 200 - in game


# window screen set up
window = Screen()
window.title("Table tennis scoreboard")
window.bgcolor("black")
window.setup(width=1024, height=600)
window.delay(0)
window.tracer(False)

# turtle set up
pen = Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.penup()


# definitions of game functions


def database_update_singles():
    global player2_id, player1_id, playerNames, match_duration, leftScore, rightScore
    conn = connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute(
        'INSERT INTO Singles_statistics (Player_1_Name, Player_2_Name, Player_1_Score, Player_2_Score, '
        'Match_duration, Date) VALUES (?, ?, ?, ?, ?, ?)', [playerNames[player1_id], playerNames[player2_id], leftScore,
                                                            rightScore, match_duration, date.today()])
    conn.commit()
    conn.close()
    return c.lastrowid


def database_update_doubles():
    global player1_id, player2_id, player3_id, player4_id, playerNames, match_duration, leftScore, rightScore
    teamA = playerNames[player1_id] + "-" + playerNames[player2_id]
    teamB = playerNames[player3_id] + "-" + playerNames[player4_id]
    conn = connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute(
        'INSERT INTO Doubles_statistics (Team_1_Name, Team_2_Name, Team_1_Score, Team_2_Score, '
        'Match_duration, Date) VALUES (?, ?, ?, ?, ?, ?)', [teamA, teamB, leftScore,
                                                            rightScore, match_duration, date.today()])
    conn.commit()
    conn.close()
    return c.lastrowid


def gameformat():
    pen.goto(-220, 0)
    pen.write("Quick game", align="center", font=("Arial", 40, "bold"))
    pen.goto(-220, -100)
    pen.write("Button A", align="center", font=("Arial", 25, "bold"))
    pen.goto(250, 0)
    pen.write("New game", align="center", font=("Arial", 40, "bold"))
    pen.goto(250, -100)
    pen.write("Button B", align="center", font=("Arial", 25, "bold"))


def gametype():
    pen.goto(-220, 0)
    pen.write("Singles", align="center", font=("Arial", 40, "bold"))
    pen.goto(-220, -100)
    pen.write("Button A", align="center", font=("Arial", 25, "bold"))
    pen.goto(250, 0)
    pen.write("Doubles", align="center", font=("Arial", 40, "bold"))
    pen.goto(250, -100)
    pen.write("Button B", align="center", font=("Arial", 25, "bold"))


def gamesize():
    pen.goto(-220, 0)
    pen.write("Big set", align="center", font=("Arial", 40, "bold"))
    pen.goto(-220, -100)
    pen.write("Button A", align="center", font=("Arial", 25, "bold"))
    pen.goto(250, 0)
    pen.write("Small set", align="center", font=("Arial", 40, "bold"))
    pen.goto(250, -100)
    pen.write("Button B", align="center", font=("Arial", 25, "bold"))


def buttonAcolor():
    pen.color("red")
    pen.goto(-220, -100)
    pen.write("Button A", align="center", font=("Arial", 25, "bold"))
    pen.color("white")
    sleep(0.5)
    pen.clear()


def buttonBcolor():
    pen.color("red")
    pen.goto(250, -100)
    pen.write("Button B", align="center", font=("Arial", 25, "bold"))
    pen.color("white")
    sleep(0.5)
    pen.clear()


def resetgame():
    window.bgcolor("black")
    pen.color("white")
    global serve, totalLeft, totalRight, leftScore, rightScore, count, game_state, player1, player2, player3, player4, \
        posCount, positionX, positionY, positionX2, positionY2, player1_id, player2_id, player3_id, player4_id, doubles
    serve = [True, False]
    totalLeft = totalRight = leftScore = rightScore = count = 0
    pen.clear()
    pen.goto(0, 200)
    pen.write("New game!", align="center", font=("Arial", 40, "bold"))
    pen.goto(0, -100)
    player1 = False
    player2 = False
    player3 = None
    player4 = None
    player1_id = None
    player2_id = None
    player3_id = None
    player4_id = None
    doubles = None
    posCount = 0
    positionY = 100
    positionX = -350
    positionX2 = 100
    positionY2 = 100
    game_state = 0


def totalscore():
    pen.goto(0, 220)
    pen.color("white")
    pen.write("Total score {} : {}".format(totalLeft, totalRight), align="center",
              font=("Arial", 40, "bold"))
    pen.goto(0, -100)


def serveistrue():
    global leftScore, rightScore, totalLeft, totalRight
    pen.clear()
    pen.color("green")
    if leftScore <= 9 and rightScore <= 9:
        pen.goto(-400, -100)
        pen.write(">", align="center", font=("Arial", 150, "bold"))
        pen.goto(0, -100)
        pen.write("{} : {}".format(leftScore, rightScore), align="center", font=("Arial", 150, "bold"))
    elif leftScore >= 10 and rightScore <= 9:
        pen.goto(-400, -100)
        pen.write(">", align="center", font=("Arial", 150, "bold"))
        pen.goto(0, -100)
        pen.write("{} : {}  ".format(leftScore, rightScore), align="center", font=("Arial", 150, "bold"))
    elif rightScore >= 10 and leftScore <= 9:
        pen.goto(-400, -100)
        pen.write(">", align="center", font=("Arial", 150, "bold"))
        pen.goto(0, -100)
        pen.write("  {} : {}".format(leftScore, rightScore), align="center", font=("Arial", 150, "bold"))
    elif rightScore >= 10 and leftScore >= 10:
        pen.goto(-400, -100)
        pen.write(">", align="center", font=("Arial", 150, "bold"))
        pen.goto(0, -100)
        pen.write("{} : {}".format(leftScore, rightScore), align="center", font=("Arial", 150, "bold"))
    totalscore()


def serveisfalse():
    global leftScore, rightScore, totalLeft, totalRight
    pen.clear()
    pen.color("green")
    if leftScore <= 9 and rightScore <= 9:
        pen.goto(400, -100)
        pen.write("<", align="center", font=("Arial", 150, "bold"))
        pen.goto(0, -100)
        pen.write("{} : {}".format(leftScore, rightScore), align="center", font=("Arial", 150, "bold"))
    elif leftScore >= 10 and rightScore <= 9:
        pen.goto(400, -100)
        pen.write("<", align="center", font=("Arial", 150, "bold"))
        pen.goto(0, -100)
        pen.write("{} : {}  ".format(leftScore, rightScore), align="center", font=("Arial", 150, "bold"))
    elif rightScore >= 10 and leftScore <= 9:
        totalscore()
        pen.color("green")
        pen.goto(400, -100)
        pen.write("<", align="center", font=("Arial", 150, "bold"))
        pen.goto(0, -100)
        pen.write("  {} : {}".format(leftScore, rightScore), align="center", font=("Arial", 150, "bold"))
    elif rightScore >= 10 and leftScore >= 10:
        pen.goto(400, -100)
        pen.write("<", align="center", font=("Arial", 150, "bold"))
        pen.goto(0, -100)
        pen.write("{} : {}".format(leftScore, rightScore), align="center", font=("Arial", 150, "bold"))
    totalscore()


def servicecheck():
    global serve, count, servechange
    if count == servechange:
        serve = not serve
        count = -1  # resetting the counter to negative number to handle service turn


def servingturndisplay():
    global serve, leftScore, rightScore, totalLeft, totalLeft
    if serve:
        pen.clear()
        pen.color("green")
        pen.goto(-400, -100)
        pen.write(">", align="center", font=("Arial", 150, "bold"))
        pen.goto(0, -100)
        pen.write("{} : {}".format(leftScore, rightScore), align="center", font=("Arial", 150, "bold"))
        totalscore()
    elif not serve:
        pen.clear()
        pen.color("green")
        pen.goto(400, -100)
        pen.write("<", align="center", font=("Arial", 150, "bold"))
        pen.goto(0, -100)
        pen.write("{} : {}".format(leftScore, rightScore), align="center", font=("Arial", 150, "bold"))
        totalscore()


def serveswitch():
    global serve
    if serve is True:
        serve = not serve  # switching serving player to right player
    elif serve is False:
        serve = not serve  # switching serving player to left player


def rightwins():
    global totalLeft, totalRight, rightScore, leftScore, count, start_game, match_duration, player1_id, player2_id, \
        player3_id, player4_id, serve
    totalRight += 1
    end_game = default_timer()
    match_duration_raw = end_game - start_game
    match_duration = ceil(match_duration_raw / 60)
    if doubles is True:
        database_update_doubles()
    elif doubles is False:
        database_update_singles()
    rightScore = leftScore = count = 0
    start_game = default_timer()
    pen.goto(0, -200)
    pen.write('Game Won !', align="center", font=("Arial", 75, "bold"))
    pen.goto(0, -100)
    sleep(5)
    pen.clear()
    if doubles is True:
        player1_id, player2_id, player3_id, player4_id = player4_id, player3_id, player2_id, player1_id
    elif doubles is False:
        player1_id, player2_id = player2_id, player1_id
    totalLeft, totalRight = totalRight, totalLeft
    totalscore()
    pen.clear()
    serve = True
    servingturndisplay()


def leftwins():
    global totalLeft, totalRight, rightScore, leftScore, count, start_game, match_duration, player1_id, player2_id, \
        player3_id, player4_id, serve
    totalLeft += 1
    end_game = default_timer()
    match_duration_raw = end_game - start_game
    match_duration = ceil(match_duration_raw / 60)
    if doubles is True:
        database_update_doubles()
    elif doubles is False:
        database_update_singles()
    leftScore = rightScore = count = 0
    start_game = default_timer()
    pen.goto(0, -200)
    pen.write('Game Won !', align="center", font=("Arial", 75, "bold"))
    pen.goto(0, -100)
    sleep(5)
    pen.clear()
    if doubles is True:
        player1_id, player2_id, player3_id, player4_id = player4_id, player3_id, player2_id, player1_id
    elif doubles is False:
        player1_id, player2_id = player2_id, player1_id
    totalLeft, totalRight = totalRight, totalLeft
    totalscore()
    pen.clear()
    serve = False
    servingturndisplay()


def printnames():
    pen.color("white")
    pen.goto(-200, 100)
    pen.write("John", align="center", font=("Arial", 40, "bold"))
    pen.goto(-200, 0)
    pen.write("Tim", align="center", font=("Arial", 40, "bold"))
    pen.goto(-200, -100)
    pen.write("Andy", align="center", font=("Arial", 40, "bold"))
    pen.goto(300, 100)
    pen.write("Thomas", align="center", font=("Arial", 40, "bold"))
    pen.goto(300, 0)
    pen.write("Adam", align="center", font=("Arial", 40, "bold"))
    pen.goto(300, -100)
    pen.write("Guest", align="center", font=("Arial", 40, "bold"))
    pen.goto(0, -180)
    pen.write("Choose - Button A", align="center", font=("Arial", 25, "bold"))
    pen.goto(0, -240)
    pen.write("Confirm - Бутон Б", align="center", font=("Arial", 25, "bold"))
    pen.goto(0, -180)


def position():
    global positionY, positionX, positionX2, positionY2, posCount
    if posCount <= 3:
        pen.color("yellow")
        pen.begin_fill()
        pen.goto(positionX, positionY)
        pen.down()
        pen.circle(25)
        pen.end_fill()
        pen.up()
        positionY -= 100
    elif 3 < posCount <= 5:
        pen.color("yellow")
        pen.begin_fill()
        pen.goto(positionX2, positionY2)
        pen.down()
        pen.circle(25)
        pen.end_fill()
        pen.up()
        positionY2 -= 100
    elif posCount >= 6:
        pen.color("yellow")
        pen.begin_fill()
        pen.goto(positionX2, positionY2)
        pen.down()
        pen.circle(25)
        pen.end_fill()
        pen.up()
        positionY2 -= 100
        posCount = 0
        positionY = 100
        positionX = -350
        positionX2 = 100
        positionY2 = 100


def playercheck():
    global player1, player2, player3, player4, player1_id, player2_id, player3_id, player4_id
    if doubles is True:
        if player2_id == player1_id and player2 is True and player1 is True:
            pen.goto(0, 200)
            pen.write("Player is already selected", align="center", font=("Arial", 40, "bold"))
            printnames()
            player2 = False
            player2_id = None
            sleep(1)
            pen.clear()
        elif player3_id == player1_id and player4 is True and player1 is True:
            pen.goto(0, 200)
            pen.write("Player is already selected", align="center", font=("Arial", 40, "bold"))
            printnames()
            player3 = False
            player3_id = None
            sleep(1)
            pen.clear()
        elif player3_id == player2_id and player3 is True and player2 is True:
            pen.goto(0, 200)
            pen.write("Player is already selected", align="center", font=("Arial", 40, "bold"))
            printnames()
            player3 = False
            player3_id = None
            sleep(1)
            pen.clear()
        elif player4_id == player1_id and player4 is True and player1 is True:
            pen.goto(0, 200)
            pen.write("Player is already selected", align="center", font=("Arial", 40, "bold"))
            printnames()
            player4 = False
            player4_id = None
            sleep(1)
            pen.clear()
        elif player4_id == player2_id and player4 is True and player2 is True:
            pen.goto(0, 200)
            pen.write("Player is already selected", align="center", font=("Arial", 40, "bold"))
            printnames()
            player4 = False
            player4_id = None
            sleep(1)
            pen.clear()
        elif player4_id == player3_id and player4 is True and player3 is True:
            pen.goto(0, 200)
            pen.write("Player is already selected", align="center", font=("Arial", 40, "bold"))
            printnames()
            player4 = False
            player4_id = None
            sleep(1)
            pen.clear()
    elif doubles is False:
        if player1_id == player2_id:
            pen.goto(0, 200)
            pen.write("Player is already selected", align="center", font=("Arial", 40, "bold"))
            printnames()
            player1 = False
            player2 = False
            player1_id = None
            player2_id = None
            sleep(1)
            pen.clear()


def setplayer(e):
    global positionY
    if 0 < posCount <= 3:
        red_position = positionY + 100
        pen.color("red")
        pen.begin_fill()
        pen.goto(positionX, red_position)
        pen.down()
        pen.circle(25)
        pen.end_fill()
        pen.up()
        pen.goto(0, 200)
        pen.write("Player is selected", align="center", font=("Arial", 40, "bold"))
        e = not e
        return e
    elif 3 < posCount <= 5:
        red_position2 = positionY2 + 100
        pen.color("red")
        pen.begin_fill()
        pen.goto(positionX2, red_position2)
        pen.down()
        pen.circle(25)
        pen.end_fill()
        pen.up()
        pen.goto(0, 200)
        pen.write("Player is selected", align="center", font=("Arial", 40, "bold"))
        e = not e
        return e
    elif posCount == 0:
        pen.color("red")
        pen.begin_fill()
        pen.goto(100, -100)
        pen.down()
        pen.circle(25)
        pen.end_fill()
        pen.up()
        pen.goto(0, 200)
        pen.write("Player is selected", align="center", font=("Arial", 40, "bold"))
        e = not e
        return e


def slowraspberry():
    sleep(0.15)


# game logic


while True:
    while game_state == 0:
        slowraspberry()
        gameformat()
        if buttonA.is_active:
            gamepoints = 21
            servechange = 4
            penalties = 20
            player1_id = 0
            player2_id = 1
            buttonAcolor()
            doubles = False
            game_state = 200
        elif buttonB.is_active:
            buttonBcolor()
            game_state = 50
        elif buttonA.is_active and buttonB.is_active:
            resetgame()
        elif buttonC.is_active:  # command to close window
            window.bye()
    while game_state == 50:
        slowraspberry()
        gametype()
        if buttonA.is_active:  # singles
            game_state = 100
            doubles = False
            buttonAcolor()
        elif buttonB.is_active:  # doubles
            doubles = True
            gamepoints = 21
            servechange = 4
            penalties = 20
            game_state = 150
            player3 = False
            player4 = False
            buttonBcolor()
        elif buttonA.is_active and buttonB.is_active:
            resetgame()
        elif buttonC.is_active:  # command to close window
            window.bye()
    while game_state == 100:
        slowraspberry()
        gamesize()
        if buttonA.is_active:
            gamepoints = 21
            servechange = 4
            penalties = 20
            game_state = 150
            buttonAcolor()
        elif buttonB.is_active:
            gamepoints = 11
            servechange = 1
            penalties = 10
            game_state = 150
            buttonBcolor()
        elif buttonA.is_active and buttonB.is_active:
            resetgame()
        elif buttonC.is_active:  # command to close window
            window.bye()
    while game_state == 150:
        while player1 is not True:
            printnames()
            slowraspberry()
            if buttonA.is_active and player1 is False:
                posCount += 1
                pen.clear()
                printnames()
                position()
            elif buttonB.is_active and player1 is False:
                if positionY == 0:
                    player1 = setplayer(player1)
                    player1_id = playerNames.index("John")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY == -100:
                    player1 = setplayer(player1)
                    player1_id = playerNames.index("Tim")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY == -200 and posCount <= 3:
                    player1 = setplayer(player1)
                    player1_id = playerNames.index("Andy")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY2 == 0 and posCount > 0:
                    player1 = setplayer(player1)
                    player1_id = playerNames.index("Thomas")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY2 == -100 and posCount > 0:
                    player1 = setplayer(player1)
                    player1_id = playerNames.index("Adam")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                else:
                    player1 = setplayer(player1)
                    player1_id = playerNames.index("Guest")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
        while player2 is not True and player1 is True:
            printnames()
            slowraspberry()
            if buttonA.is_active and player2 is False:
                posCount += 1
                pen.clear()
                printnames()
                position()
            elif buttonB.is_active and player2 is False:
                if positionY == 0:
                    player2 = setplayer(player2)
                    player2_id = playerNames.index("John")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY == -100:
                    player2 = setplayer(player2)
                    player2_id = playerNames.index("Tim")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY == -200 and posCount <= 3:
                    player2 = setplayer(player2)
                    player2_id = playerNames.index("Andy")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY2 == 0 and posCount > 0:
                    player2 = setplayer(player2)
                    player2_id = playerNames.index("Thomas")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY2 == -100 and posCount > 0:
                    player2 = setplayer(player2)
                    player2_id = playerNames.index("Adam")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                else:
                    player2 = setplayer(player2)
                    player2_id = playerNames.index("Guest")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
        while player3 is False and player2 is True:
            printnames()
            slowraspberry()
            if buttonA.is_active and player3 is False:
                posCount += 1
                pen.clear()
                printnames()
                position()
            elif buttonB.is_active and player3 is False:
                if positionY == 0:
                    player3 = setplayer(player3)
                    player3_id = playerNames.index("John")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY == -100:
                    player3 = setplayer(player3)
                    player3_id = playerNames.index("Tim")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY == -200 and posCount <= 3:
                    player3 = setplayer(player3)
                    player3_id = playerNames.index("Andy")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY2 == 0 and posCount > 0:
                    player3 = setplayer(player3)
                    player3_id = playerNames.index("Thomas")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY2 == -100 and posCount > 0:
                    player3 = setplayer(player3)
                    player3_id = playerNames.index("Adam")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                else:
                    player3 = setplayer(player3)
                    player3_id = playerNames.index("Guest")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
        while player4 is False and player3 is True:
            printnames()
            slowraspberry()
            if buttonA.is_active and player4 is False:
                posCount += 1
                pen.clear()
                printnames()
                position()
            elif buttonB.is_active and player4 is False:
                if positionY == 0:
                    player4 = setplayer(player4)
                    player4_id = playerNames.index("John")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY == -100:
                    player4 = setplayer(player4)
                    player4_id = playerNames.index("Tim")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY == -200 and posCount <= 3:
                    player4 = setplayer(player4)
                    player4_id = playerNames.index("Andy")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY2 == 0 and posCount > 0:
                    player4 = setplayer(player4)
                    player4_id = playerNames.index("Thomas")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                elif positionY2 == -100 and posCount > 0:
                    player4 = setplayer(player4)
                    player4_id = playerNames.index("Adam")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
                else:
                    player4 = setplayer(player4)
                    player4_id = playerNames.index("Guest")
                    sleep(0.5)
                    pen.clear()
                    playercheck()
        if player1 is True and player2 is True and player3 is True and player4 is True:
            game_state = 200
        elif player1 is True and player2 is True:
            game_state = 200
    sleep(0.5)
    start_game = default_timer()
    serve = choice(serve)
    servingturndisplay()
    while game_state == 200:
        if leftScore >= penalties and rightScore >= penalties:
            while leftScore >= penalties and rightScore >= penalties:  # handling overtime
                serveswitch()
                slowraspberry()
                if buttonA.is_active:  # point for left player
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
                elif buttonB.is_active:  # point for right  player
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
                elif buttonA.is_active and buttonB.is_active:
                    resetgame()
                elif buttonC.is_active:  # command to close window
                    window.bye()

        elif leftScore == gamepoints:  # left wins
            leftwins()
        elif rightScore == gamepoints:  # right wins
            rightwins()
        else:
            slowraspberry()
            if buttonA.is_active:  # point for left player
                count += 1
                leftScore += 1
                if serve is True:
                    serveistrue()
                    servicecheck()
                elif serve is False:
                    serveisfalse()
                    servicecheck()
            elif buttonB.is_active:  # point for right  player
                count += 1
                rightScore += 1
                if serve is True:
                    serveistrue()
                    servicecheck()
                elif serve is False:
                    serveisfalse()
                    servicecheck()
            elif buttonA.is_active and buttonB.is_active:
                resetgame()
            elif buttonC.is_active:  # command to close window
                window.bye()

window.mainloop()
window.bye()
