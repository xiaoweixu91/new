# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
range_num=-1
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global range_num        
    global chance
    if range_num>=100:
        secret_number=range_num
        chance=10
    elif range_num>=0 and range_num<100:
        secret_number=range_num
        chance=7
    else:
        secret_number=random.randrange(0,100)
        chance=7   
    
# define event handlers for control panel
def range100():
    global range_num
    range_num=random.randrange(0,100)
    print "the range has change to 100,a new game will begin."
    # button that changes the range to [0,100) and starts a new game 
    new_game()
    

def range1000():
    global range_num
    range_num=random.randrange(0,1000)
    print "the range has change to 1000,a new game will begin."
    new_game()

    # button that changes the range to [0,1000) and starts a new game     
    
    
def input_guess(guess):
    # main game logic goes here	
    number=int(guess)
    print "the guess is ",number
    if number < secret_number:
        print "Higher!"
        global chance
        if chance > 1:
            chance-=1
            print "you still have ",chance,"oppurtunities to guess"
        else:
            print "you lose!"
            print "A new game will begin"


            new_game()
    elif number > secret_number:
        print "Lower!"
        
        if chance > 1:
            chance-=1
            print "you still have ",chance,"oppurtunities to guess"

        else:
            print "you lose!"
            print "A new game will begin"
            
            new_game()
    else :
        print "Correct!"
        print "A new game will begin"
        
        new_game()
    

    
# create frame
frame= simplegui.create_frame("Guessing number game",200,200,200)

# register event handlers for control elements and start frame
inp=frame.add_input("Guess number",input_guess,30)
botton1=frame.add_button("range100",range100)
botton2=frame.add_button("range1000",range1000)

# call new_game 
frame.start()
new_game()


# always remember to check your completed program against the grading rubric

