# Random Number Generator Game
# Z_NAULT
# 2/10/2018
# User gives input of 4 digits, that are compared by the user to 4 randomly generated numbers from 1-100.
# 2/26/2018 Added def function, infinite loop, & removed global.
# 3/9/2018 Created error messages for input over 100. Gives user option to restart/end game.
# 3/9/2018 Added Def repeat for restarting of game = Ver1.1
# 3/13/2018 Cleaned up code = Ver1.2
from random import *


def repeat():
    while 1 == 1:
        play_again = str(input("Would you like to play again? y/n???"))
        if play_again == "y":
            numgengame()
        elif play_again == "n":
            print("Goodbye!")  # If/elif statements asking user if they want to play again.
            exit()
        else:
            print("*****************************\nERROR GAME RESTART!!!\n******************************\n\n\n\n")
            numgengame()


def numgengame():  # My use of the def function was to repeat the game.
    """ Takes user input, and displays random numbers from 1-100."""
    print("Feeling Lucky?!?\n\nThis is a random number generator from 1-100.\n\
     I want you to see if you can guess what 4 numbers will pop up!")
    g1 = int(input("Guess #1 "))
    if g1 > 100:
        print("Number is over 100!")
        repeat()
    g2 = int(input("Guess #2 "))
    if g2 > 100:
       print("Number is over 100!")
       repeat()
    g3 = int(input("Guess #3 "))
    if g3 > 100:
        print("Number is over 100!")
        repeat()
    g4 = int(input("Guess #4 "))
    if g4 > 100:
        print("Number is over 100!")
        repeat()
    else:
        bigG = sorted((g1, g2, g3, g4))
        print("Calculating...")
        input("Press enter key for answers!")

        items = list(range(0, 101))
        shuffle(items)

        print("The winning numbers are!")
        ans = (items[1:21])
        print(sorted(ans))
        print("Your numbers selected were:")
        print(bigG)
        for n in ans:
            if n is g1:
                print("You got a match!", g1)
            elif n is g2:
                print("You got a match!", g2)
            elif n is g3:
                print("You got a match!", g3)
            elif n is g4:
                print("You got a match!", g4)


# Main
numgengame()
repeat()
