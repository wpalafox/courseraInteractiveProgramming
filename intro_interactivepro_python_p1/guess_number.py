# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

#initialize game
print "Welcome to Guess the Number!"
marker = 1



# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print "\n"
    global marker

    if marker == 1:
        range100()
    elif marker == 2:
        range1000()
    else:
        print "Error"





# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global marker
    marker = 1
    print "\n"+"Guess a number from 0-99"
    global secret_number
    global countdown_guess
    countdown_guess = 7
    print "Chances remaining: "+str(countdown_guess)

    secret_number = random.randrange(0, 100)
    #print "Secret number: "+str(secret_number)

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global marker
    marker = 2
    print "\n"+"Guess a number from 0-999"
    global secret_number
    global countdown_guess
    countdown_guess = 10
    print "Chances remaining: "+str(countdown_guess)

    secret_number = random.randrange(0, 1000)
    #print "Secret number: "+str(secret_number)

def input_guess(guess):
    # main game logic goes here
    print "\n"+"Player guess is "+str(guess)
    ############################
    guess_number = int(guess)

    global countdown_guess
    countdown_guess-= 1
    print "Chances remaining: "+str(countdown_guess)



    if guess_number > secret_number and countdown_guess>0:
        print "Lower"
    elif guess_number < secret_number and countdown_guess>0:
        print "Higher"
    elif guess_number == secret_number and countdown_guess>=0:
        print "You Win! Let's play again."
        if marker == 1:
            range100()
        elif marker == 2:
            range1000()
        else:
            print "Error"

    elif countdown_guess <= 0:
        print "Game Over. New Game. Same Range."
        if marker == 1:
            range100()
        elif marker == 2:
            range1000()
        else:
            print "Error"

    else:
        print "Error"





# create frame
frame = simplegui.create_frame('Guess the number', 250, 250)
frame.add_input('Enter a number between 1-99', input_guess, 25)
frame.add_button('Reset Game', new_game)
frame.add_label('Change to Range 100')
frame.add_button('100', range100,50)
frame.add_label('Change to Range 1000')
frame.add_button('1000', range1000,50)

# register event handlers for control elements and start frame


# call new_game
new_game()


# always remember to check your completed program against the grading rubri
