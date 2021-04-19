import random

def HANGMAN_GAME():
    print ('___HANGMAN___by.Kojima')
    wordlist =['dance', 'teacher', 'inhabitant', 'forge', 'expertise',
               'horoscope', 'drift', 'message', 'float', 'cute', 'stain',
               'bucket', 'battle', 'seller']
    secret = random.choice(wordlist)
    guesses = ''
    turns = 10


    while turns > 0:
        missed = 0
        guess = input('\nInput a letter: ')
        guesses += guess
        for letter in secret:
            if letter in guesses:
                print (letter,end=' ')
            else:
                print ('_',end=' ')
                missed= missed + 1

        if missed == 0:
            print ('\nYou win!')
            break



        if guess not in secret:
            turns = turns -1
            print ('\nNope.')
            print ('\n',turns, 'more turns')
            if turns == 9: print (' __ __ ')

            if turns == 8:
                print ('    | ')
                print ('    | ')
                print ('    | ')
                print ('    | ')
                print (' ___|___ ')

            if turns == 7:
                print ('    _____ ')
                print ('    | ')
                print ('    | ')
                print ('    | ')
                print ('    | ')
                print (' ___|___ ')

            if turns == 6:
                print ('    _____ ')
                print ('    |   |')
                print ('    | ')
                print ('    | ')
                print ('    | ')
                print (' ___|___ ')

            if turns == 5:
                print ('    _____ ')
                print ('    |   |')
                print ('    |   O')
                print ('    | ')
                print ('    | ')
                print (' ___|___ ')

            if turns == 4:
                print ('    _____ ')
                print ('    |   |')
                print ('    |   O')
                print ('    |   |')
                print ('    | ')
                print (' ___|___ ')

            if turns == 3:
                print ('    _____ ')
                print ('    |   |')
                print ('    |   O')
                print ('    |  /|')
                print ('    | ')
                print (' ___|___ ')

            if turns == 2:
                print ('    _____ ')
                print ('    |   |')
                print ('    |   O')
                print ('    |  /|\ ')
                print ('    | ')
                print (' ___|___ ')

            if turns == 1:
                print ('    _____ ')
                print ('    |   |')
                print ('    |   O')
                print ('    |  /|\ ')
                print ('    |  /')
                print (' ___|___ ')

            if turns == 0:
                print ('    _____ ')
                print ('    |   |')
                print ('    |   O')
                print ('    |  /|\ ')
                print ('    |  / \ ')
                print (' ___|___ ')

            if turns == 0:
                print ('\nThe answer is ', secret)
playagain = 'Y'
while playagain == 'Y':
    if playagain == 'Y':
        HANGMAN_GAME()
        print('Play again? (Y/N)')
        playagain = input()