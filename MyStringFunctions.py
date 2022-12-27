# File: MyStringFunctions.py
# Student: Nick Umbrewicz
# UT EID: nju96
# Course Name: CS303E
# 
# Date: 3/28/2022
# Description of Program: This program defines a number of string functions.

def myAppend(str, ch):
    return str + ch

def myCount(str, ch):

    counter = 0
    for letter in str:
        if letter == ch:
            counter += 1
    return counter
    
    # Return the number of times character ch appears
    # in str.

def myExtend(str1, str2):

    extendedString = str1
    for letter in str2:
        extendedString += letter
    return extendedString
    
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.

def myMin(str):

    if str == "":
        print("Empty string: no min value")
        return None   
    else:
        lowest = str[0]
        for letter in str:
            if ord(letter) <= ord(lowest):
                lowest = letter
        return lowest
    
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.

def myInsert(str, i, ch):

    if i > len(str):
        print("Invalid index")
        return None
    else:
        newString = str[0:i] + ch + str[i:]
        return newString
        
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.

def myPop(str, i):

    if i >= len(str):
        print("Invalid index")
        return str, None
    else:
        newString = str[0:i] + str[i+1:]
        return newString, str[i]
    
    # Return two results: 
    # 1. a new string that is like str but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(str), and return str unchanged and None

def myFind(str, ch):

    if ch not in str:
        return -1
    else:
        counter = 0
        index = -1
        while counter < 1:
            for letter in str:
                index += 1
                if letter == ch:
                    counter += 1
                    return index
    
    # Return the index of the first (leftmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.

def myRFind(str, ch):

    if ch not in str:
        return -1
    else:
        counter = -1
        for letter in str:
            counter += 1
            if str[counter] == ch:
                index = counter
        return index
    
    # Return the index of the last (rightmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.

def myRemove(str, ch):

    if ch not in str:
        return str
    else:
        counter = 0
        i = -1
        while counter < 1:
            for letter in str:
                i += 1
                if letter == ch:
                    counter += 1
                    return str[:i] + str[i + 1:]
            
    # Return a new string with the first occurrence of ch 
    # removed.  If there is none, return str.

def myRemoveAll(str, ch):

    if ch not in str:
        return str
    else:
        newString = ""
        for letter in str:
            if letter != ch:
                newString += letter
    return newString
    
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.

def myReverse(str):

    reverseString = ""
    for letter in str[len(str)::-1]:
        reverseString += letter
    return reverseString
    
    # Return a new string like str but with the characters
    # in the reverse order.
