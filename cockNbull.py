''' Create a program that will play the “cows and bulls” game with the user. The game works like this: Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.'''

import random

def check(c,a):
    if c == 4:
        print ("Yesss, your guess has matched!! 4 cocks for you :-) It just took {0} tries to get it right!!!\n" .format(a))
        exit
    else:
        print ("You have {0} cocks and {1} bulls, common give it another try, will you\n" .format(c, 4-c))
        return

def comp(r, g):
    z = 0
    cock = 0
    while z < 4:
        if r[z] == g[z]:
            cock += 1
        z += 1
    return (cock)
            
def guess():
    return input("Please enter your guess 4 digit number! NOWW!\n")
    

if __name__=="__main__":
    print ("Welcome to the cock and bull game!!! yess!! welcome!!! \n")
    rand = random.randint(1000, 9999)
    print (rand)
    rand_list = [ i for i in str(rand) ]
    cock = 0
    atmpt = 0
    while cock < 4:
        guess_list = [ i for i in str(guess()) ]
        atmpt += 1
        cock = comp(rand_list,guess_list)
        result = check(cock,atmpt)
