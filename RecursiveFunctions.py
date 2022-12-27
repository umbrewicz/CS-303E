# File: RecursiveFunctions.py
# Student: Nick Umbrewicz
# UT EID: nju96
# Course Name: CS303E
# 
# Date: 4/22/2022
# Description of Program: This program defines a number of recursive functions.

def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in 
    list L. """
    if L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList( key, L[1:] )
    else:
        return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
    """ Add up the non-negative integers to n.
    E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. """
    if n == 0:
        return 0
    else:
        return n + addToN(n - 1)

def findSumOfDigits( n ):
    """ Return the sum of the digits in a non-negative integer. """
    strN = str(n)
    if strN == "0":
        return 0
    else:
        return int(strN[0]) + findSumOfDigits(strN[1:])

def integerToBinary( n ):
    """ Given a nonnegative decimal integer n, return the 
    binary representation as a string. """
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    elif n > 1:
        return str(integerToBinary(n // 2)) + str(n % 2)

def integerToList( n ):
    """ Given a nonnegative decimal integer, return a list of the 
    digits (as strings). """
    strN = str(n)
    if strN == " ":
        return []
    elif n < 10:
        return [strN]
    else:
        return integerToList(n//10) + [str(n%10)]

def isPalindrome( s ):
    """ Return True if string s is a palindrome and False
    otherwise. Count the empty string as a palindrome. """
    if len(s) <= 1:
        return True
    elif s[0] != s[len(s) - 1]:
        return False
    else:
        return isPalindrome(s[1 : len(s) -1])

def findFirstUppercase( s ):
    """ Return the first uppercase letter in 
    string s, if any.  Return None if there
    is none. """
    if s == '':
        return None
    elif s[0].isupper():
        return s[0]
    else:
        return findFirstUppercase(s[1:])

def findFirstUppercaseIndexHelper( s, index ):
    """ Helper function for findFirstUppercaseIndex.
    Return the index of the first uppercase letter, 
    beginning at index.  Return -1 if there is none."""
    if s == "" or index == len(s) - 1:
        return -1
    elif s[index].isupper():
        return index
    else:
        return findFirstUppercaseIndexHelper(s, index + 1)

# The following function is already completed for you.  But 
# make sure you understand what it's doing. 

def findFirstUppercaseIndex( s ):
    """ Return the index of the first uppercase letter in 
    string s, if any.  Return -1 if there is none.  This one 
    requires a helper function, which is the recursive 
    function. """
    return findFirstUppercaseIndexHelper(s, 0)
