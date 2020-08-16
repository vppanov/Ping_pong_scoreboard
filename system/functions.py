
from time import sleep
from turtle import Screen, Turtle
from math import fabs
import system.functions
# variable for the game
count = 0
leftScore = 0
rightScore = 0
serve = None
totalLeft = 0
totalRight = 0
player1 = False
player2 = False
playerNames = ["Веско", "Сашо", "Гери", "Георги", "Ивайло", "Друг"]
player1_id = None
player2_id = None
posCount = 0
positionY = 100
positionX = -350
positionX2 = 100
positionY2 = 100
# turtle set up
pen = Turtle()
pen.speed(0)
pen.color("black")
pen.hideturtle()
pen.penup()



