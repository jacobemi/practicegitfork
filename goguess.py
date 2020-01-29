import random

def goguess():
    
    number = int(random.randint(1,20)) #Selects a 'random' integer between 1 and 20
    guesses = 1
    
    print 'I have a number between 1 and 20 inclusive.'
    
    guess = int(raw_input('Guess: ')) #Prompts user for their first guess
    
    while guess != number: #If the guess is not the number, this block runs
        if guess > number: # If the guess is higher, it gives feedback, adds new guess to the count, prompts user for another guess
            print str(guess) + ' is too high.'
            guesses += 1
            guess = int(raw_input('Guess: '))
            
        if guess < number: # If the guess is lower, it gives feedback, adds new guess to the count, prompts user for another guess
            print str(guess) + ' is too low.'
            guesses +=1
            guess = int(raw_input('Guess: '))
            
    print 'Right! my number is ' + str(number) + '! You guessed in ' + str(guesses) + ' guesses!' #This runs when the guess is correct
#haha            
