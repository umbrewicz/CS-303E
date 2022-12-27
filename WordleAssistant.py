# File: WordleAssistant.py
# Student: Nick Umbrewicz
# UT EID: nju96
# Course Name: CS303E
# 
# Date: 4/15/2022
# Description of Program: This program stores several functions to be used in Project 3 - Wordle

def createWordlist(filename):

    """ Read words from the provided file and store them in a list.
    The file contains only lowercase ascii characters, are sorted
    alphabetically, one word per line. Filter out any words that are
    not 5 letters long, have duplicate letters, or end in 's'.  Return
    the list of words and the number of words as a pair. """

    newWordlist = open(filename, "r")
    line = newWordlist.readline()
    wordlist = []
    numWords = 0
    
    for line in newWordlist:
        word = line.strip()
        if len(word) == 5:
            if word[4] != "s":
                if len(set(word)) == len(word):
                    wordlist.append(word)
                    numWords += 1

    newWordlist.close()
    return wordlist, numWords

def containsAll(wordlist, include):
    
    """ Given your wordlist, return a set of all words from the wordlist
    that contain all of the letters in the string include.  
    """
    containsAll = set()
    
    for word in wordlist:
        if set(include).issubset(set(word)):
            containsAll.add(word)
        
    return containsAll
            

def containsNone(wordlist, exclude):
    
    """ Given your wordlist, return a set of all words from the wordlist
    that do not contain any of the letters in the string exclude.  
    """

    containsNone = set()

    for word in wordlist:
        if set(exclude).difference(set(word)) == set(exclude):
            containsNone.add(word)
        
    return containsNone

def containsAtPositions(wordlist, posInfo):
    
    """ posInfo is a dictionary that maps letters to positions.
    You can assume that the positions are in [0..4].  Return a set of
    all words from the wordlist that contain the letters from the
    dictionary at the indicated positions. For example, given posInfo
    {'a': 0, 'y': 4}.   This function might return the set:
    {'angry', 'aptly', 'amply', 'amity', 'artsy', 'agony'}. """

    containsAtPositions = set()

    for word in wordlist:
        count = 0
        for i in range(len(word)):
            if word[i] in posInfo and i == posInfo[word[i]]:
                count += 1
        if count == len(posInfo.keys()):
            containsAtPositions.add(word)
        elif word in containsAtPositions:
            containsAtPositions.remove(word)

    return containsAtPositions
    

def getPossibleWords(wordlist, posInfo, include, exclude):
    
    """ Finally, given a wordlist, dictionary posInfo, and
    strings include and exclude, return the set of all words from 
    the wordlist that contains the words that satisfy all of 
    the following:
    * has letters in positions indicated in posInfo
    * contains all letters from string include
    * contains none of the letters from string exclude.
    """

    setWords = containsNone(wordlist, exclude).intersection(containsAll(wordlist, include))
    possibleWords = setWords.intersection(containsAtPositions(wordlist, posInfo))

    return possibleWords
