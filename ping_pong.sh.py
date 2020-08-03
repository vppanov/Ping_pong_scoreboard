
from time import sleep

import turtle 

#variable for the game
count = 0
score_b = 0
RedScore = 0
BlueScore = 0
scoreCount = 0
leftServe = 0
rightServe = 0

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
if z == "1":
    serve = True
elif z == "2":
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
        count +=1
        
        

           
        if x == "a":
            leftServe+=1
            RedScore += 1
            scoreCount = RedScore + BlueScore
            if serve is True:
                
                pen.clear()
                pen.write("> {} : {}".format(RedScore, BlueScore), align="center", font=("Courier", 80, "bold"))
                if count ==4:
                    serve = not serve
                    count = 0
                
                
            elif serve is False:
               
                pen.clear()
                pen.write("{} : {} <".format(RedScore, BlueScore), align="center", font=("Courier", 80, "bold"))
                if count ==4:
                    serve = not serve
                    count = 0 
      
                
        elif x == "b":
            rightServe +=1
            BlueScore += 1
            scoreCount = RedScore + BlueScore
            if serve is True:
                
                pen.clear()
                pen.write("> {} : {}".format(RedScore, BlueScore), align="center", font=("Courier", 80, "bold"))
                if count ==4:
                    serve = not serve
                    count = 0
                    
            elif serve is False:
                
                pen.clear()
                pen.write("{} : {} <".format(RedScore, BlueScore), align="center", font=("Courier", 80, "bold"))
                if count ==4:
                    serve = not serve
                    count = 0
    
        else:
            pen.clear()
            pen.write('Bad Input')