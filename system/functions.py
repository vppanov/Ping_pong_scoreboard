def wronginput():
    global count
    count -= 1
    pen.goto(0, 150)
    pen.write("Грешен бутон", align="center", font=("Arial", 60, "bold"))
    pen.goto(0, -100)


def resetgame():
    window.bgcolor("black")
    pen.color("white")
    global serve, totalLeft, totalRight, leftScore, rightScore, count, game_state, player1, player2, posCount, \
        positionX, positionY, positionX2, positionY2, player1_id, player2_id, size
    serve = [True, False]
    totalLeft = totalRight = leftScore = rightScore = count = 0
    pen.clear()
    pen.goto(0, 200)
    pen.write("Нова игра!", align="center", font=("Arial", 60, "bold"))
    pen.goto(0, -100)
    player1 = False
    player2 = False
    player1_id = None
    player2_id = None
    size = None
    posCount = 0
    positionY = 100
    positionX = -350
    positionX2 = 100
    positionY2 = 100
    game_state = 25