
from time import sleep

import turtle


#variable for the game
count = 0
score_b = 0
RedScore = 0
BlueScore = 0
scoreCount = 0


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
        
        if  scoreCount >=0 and scoreCount <=5:
            serve = False
        elif scoreCount >5 and scoreCount <=9:
            serve = True
        elif  scoreCount >11 and scoreCount <=14:
            serve = False
        elif scoreCount >15 and scoreCount <=19:
            serve = True    
        elif  scoreCount >20 and scoreCount <=24:
            serve = False
        elif scoreCount >30 and scoreCount <=34:
            serve = True     
        elif  scoreCount >40 and scoreCount <=45:
            serve = False

           
        if x == "a" and serve is True:
            RedScore += 1
            pen.clear()
            pen.write("> {} : {}".format(RedScore, BlueScore), align="center", font=("Courier", 80, "bold"))
            scoreCount = RedScore + BlueScore

            
            
        elif x == "a" and serve is False:
            RedScore += 1
            pen.clear()
            pen.write("{} : {} <".format(RedScore, BlueScore), align="center", font=("Courier", 80, "bold"))
            scoreCount = RedScore + BlueScore

            
                
        elif x == "b" and serve is True:
            BlueScore += 1
            pen.clear()
            pen.write("> {} : {}".format(RedScore, BlueScore), align="center", font=("Courier", 80, "bold"))
            scoreCount = RedScore + BlueScore

            
        elif x == "b" and serve is False:
            BlueScore += 1
            pen.clear()
            pen.write("{} : {} <".format(RedScore, BlueScore), align="center", font=("Courier", 80, "bold"))
            scoreCount = RedScore + BlueScore

    
        else:
            pen.clear()
            pen.write('Bad Input')