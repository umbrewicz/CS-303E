# File: wordle.py
# Student: Nick Umbrewicz
# UT EID: nju96
# Course Name: CS303E
# 
# Date: 5/02/2022
# Description of Program: This program runs a Wordle-like game.

def createWordlist(filename):

    """ Read words from the provided file and store them in a list.
    The file contains only lowercase ascii characters, are sorted
    alphabetically, one word per line. Filter out any words that are
    not 5 letters long, have duplicate letters, or end in 's'.  Return
    the list of words and the number of words as a pair. """

    import os.path
    from os import path
    
    file_exists = path.exists(filename)
   
    if file_exists == True:
        
        newWordlist = open(filename, "r")
        line = newWordlist.readline()
        wordlist = []

        for line in newWordlist:
            word = line.strip()
            if wordOK(word) == True:
                wordlist.append(word)
        
        newWordlist.close()
        return wordlist
    
    else:
        return False


    


def wordOK(word):

    """ Filter function to determine if a word matches our criteria
        and is added to the wordlist. """

    if len(word) == 5 and len(set(word)) == 5 and word[4] != "s":
        return True
    else:
        return False


    


def returnRandom(wordlist):
    
    """ Return a random word from the wordlist. """
    
    import random
    
    wordlist = createWordlist(wordlist)
    
    return random.choice(wordlist)





def binarySearch(wordlist, key):

    """ Search if word is in wordlist. """
    
    low = 0
    high = len(wordlist) - 1
    
    while (high >= low):
        mid = (low + high) // 2
        if key < wordlist[mid]:
            high = mid - 1
        elif key == wordlist[mid]:
            return mid
        else:
            low = mid + 1
            
    return (- low - 1)





def playWordle(answer = None):

    """ Play the Wordle game. """

    print('''Welcome to WORDLE, the popular word game. The goal is to guess a
five letter word chosen at random from our wordlist.  None of the
words on the wordlist have any duplicate letters.

You will be allowed 6 guesses.  Guesses must be from the allowed
wordlist.  We'll tell you if they're not.

Each letter in your guess will be marked as follows:

    x means that the letter does not appear in the answer
    ^ means that the letter is correct and in the correct location
    + means that the letter is correct, but in the wrong location

Good luck!\n''')

    file = input("Enter the name of the file from which to extract the wordlist: ")

    wordlist = createWordlist(file)
    
    while wordlist == False:
        print("File does not exist. Try again!")
        file = input("Enter the name of the file from which to extract the wordlist: ")
        wordlist = createWordlist(file)

    if answer == None:
        answer = returnRandom(file)
        
    if binarySearch(wordlist, answer.lower()) < 0:
        print("\nAnswer supplied is not legal.")
        return
        
    answer = answer.lower()
    guessCount = 1
    
    while guessCount < 7 or guess != answer:

        guess = input("\nEnter your guess (" + str(guessCount) + "): ")
        guess = guess.lower()
        
        if binarySearch(wordlist, guess) < 0:
            print("Guess must be a 5-letter word in the wordlist. Try again!", end = "")
            continue

        else:
            print(guess[0].upper(), guess[1].upper(), guess[2].upper(),
                  guess[3].upper(), guess[4].upper(), sep = "  ")
    
            for i in range(len(guess)):
                if guess[i] not in answer:
                    print("x", end = "  ")
                if guess[i] in answer and guess[i] != answer[i]:
                    print("+", end = "  ")
                if guess[i] == answer[i]:
                    print("^", end = "  ")

        guessCount += 1
        
        if guess == answer:
            print("\nCONGRATULATIONS! You win!")
            break
        
        elif guessCount == 7:
            print("\nSorry! The word was", answer + ".", "Better luck next time!")
            break
