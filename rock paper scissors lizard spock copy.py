#rock paper scissors lizard spock
#luca magistrelli
#13/10/21

import random

cwins = 0
pwins = 0
options = ["rock","paper","scissors","spock","lizard"]
wins = ["paperrock","scissorspaper","rockscissors","spockscissors","lizardspock","rocklizard","scissorslizard","paperspock","lizardpaper","spockrock"]

eg = int(input("do you want to play tho the best of 3 or to the best of 5?\n"))


for i in range (eg):
    userchoice = input (" rock , paper,sicssors, spock or lizard?\n")
    compchoice = random.choice(options)
    result = userchoice+compchoice

    if result in wins:
        print ("THE HUMAN WINS")
        print (" the computer chose:",compchoice)
        pwins = pwins+1
        print(" THE HUMAN'S SCORE IS:",pwins)
        print("THE COMPUTER'S SCORE IS",cwins,"\n","\n")       
        
        
    elif userchoice == compchoice:
        print ("DRAW")
        print (" the computer chose:",compchoice)
        print(" THE HUMAN'S SCORE IS:",pwins)
        print("THE COMPUTER'S SCORE IS",cwins,"\n","\n")       
        
    else:
        print (" THE COMPUTER WINS")
        print (" the computer chose:",compchoice)
        cwins = cwins+1
        print("THE COMPUTER'S SCORE IS:",cwins)
        print("THE HUMAN'S SCORE IS",pwins,"\n","\n")
    
 

  
