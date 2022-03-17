import random

secretNumb= random.randint(0,10)



i=0

while(i<5):

    myNumber = int(input('guess  a number btwn 1 and 9: '))

    if(myNumber == secretNumb):
       print('you guessed the correct number')
       break

    elif(myNumber < secretNumb):
        print('your guess was too low: guess a number higher than ', myNumber)
        

    elif(myNumber > secretNumb):
        print('your guess was too high: guess a number lower than ', myNumber)


    if(i == 4):
        print('sorry time out: the number was', secretNumb)

    i=i+1






    
