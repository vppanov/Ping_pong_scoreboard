
from time import sleep

import turtle


#variable for the game
score_a = 0
score_b = 0
RedScore = 0
BlueScore = 0


wn = turtle.Screen()
wn.title("Scoreboard")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
pen.write("Who is serving ?")

z = str(input())
if z == "p":
    serve = True
else:
    serve = False
        
#pen.write("{} : {}".format(RedScore, BlueScore), align="center", font=("Courier", 80, "bold"))


while  RedScore <= 21 and BlueScore <= 21:
    wn.update()
   
    
 

    if RedScore == 21:
        pen.write('RED WINS')
        sleep(5)
        RedScore = BlueScore = 0 
        pen.clear()
    elif BlueScore == 21:
        
        pen.write('BLUE WINS')
        sleep(5)
        BlueScore = RedScore = 0
        pen.clear()
        
    else:
        
        x = str(input())
        if x == "a" and serve is True:
            RedScore += 1
            pen.clear()
            pen.write("> {} : {}".format(RedScore, BlueScore), align="center", font=("Courier", 80, "bold"))
        elif x == "a" and serve is False:
            RedScore += 1
            pen.clear()
            pen.write("{} : {} <".format(RedScore, BlueScore), align="center", font=("Courier", 80, "bold"))
            
            
        elif x == "b":
            BlueScore += 1
            pen.clear()
            pen.write("{} : {}".format(RedScore, BlueScore), align="center", font=("Courier", 80, "bold"))
            
 
        else:
            pen.clear()
            pen.write('Bad Input')