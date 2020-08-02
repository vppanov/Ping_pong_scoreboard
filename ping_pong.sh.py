RedScore = 0
BlueScore = 0

from time import sleep
while RedScore <= 21 and BlueScore <= 21:
    if RedScore == 21:
        print('RED WINS')
        sleep(5)
        RedScore = BlueScore = 0 
    elif BlueScore == 21:
        print('BLUE WINS')
        sleep(5)
        BlueScore = RedScore = 0
    else:
        x = int(input())
        if x == 1:
            RedScore += 1
            print(RedScore, ":", BlueScore)
        elif x == 2:
            BlueScore += 1
            print(RedScore, ":", BlueScore)
        elif x == 'REDRESET':
            RedScore = 3
        else:
            print('Bad Input')