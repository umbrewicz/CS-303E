# File: Project2.py
# Student: Nick Umbrewicz
# UT EID: nju96
# Course Name: CS303E
# 
# Date: 4/14/22
# Description of Program: This program carries out a number of functions around Fibonacci numbers.

ZERO = "0"
ONE = "1"
TWO = "2"
THREE = "3"
FOUR = "4"
FIVE = "5"
SIX = "6"

ERRORMESSAGE = "ERROR: Illegal value entered."


def firstNFibNumbers(n):
    
    if n <= 0:
        return []

    elif n == 1:
        return [0]
    
    elif n == 2:
        return [0, 1]

    else:

        fib1, fib2 = 0, 1
        fibs = [0, 1]

        for counter in range(2, n):

            fib1, fib2 = fib2, fib1 + fib2
            fibs.append(fib2)

        return fibs
    

def ithFibNumber(i):
    
    fibs = firstNFibNumbers(i + 1)

    if i == 0:
        return 0
    
    elif i == 1:
        return 1
    
    elif i > 1:
        return fibs[i]
    

def lessOrEqualToN(n):

    if n < 0:
        return []

    elif n == 0:
        return [0]

    elif n == 1:
        return [0, 1, 1]

    else:

        fib1, fib2 = 0, 1
        fibs = [0, 1]

        for counter in range(0, n):

            fib1, fib2 = fib2, fib1 + fib2
            
            if fib2 <= n:
                fibs.append(fib2)
                
        return fibs
    

def numLessOrEqualToN(n):
    
    if n < 0:
        return 0

    elif n == 0:
        return 1

    elif n == 1:
        return 3

    else:
        fib1, fib2 = 1, 1
        fibs = [0, 1, 1]
        numLessOrEqual = 3

        for counter in range(0, n):

            fib1, fib2 = fib2, fib1 + fib2
            
            if fib2 <= n:
                fibs.append(fib2)
                numLessOrEqual += 1

        return numLessOrEqual

    
def largestFibNumsToN(n):
    
    rfibs = reversed(lessOrEqualToN(n))
    largestToN = []

    if n == 0:
        return [0]

    while n != 0:
        for i in rfibs:
            if i == 0:
                pass
            elif i <= n:
                largestToN.append(i)
                n = n - i

    return largestToN
        
        
        
command = input('''Welcome to the Fibonacci Number laboratory!\n
The following commands are available:
  0: Exit.
  1: List the first N Fibonacci numbers.
  2: Display the ith Fibonacci number (0-based).
  3: List the Fibonacci numbers less or equal to N.
  4: How many Fibonacci numbers are less or equal to N?
  5: Find a list of the largest Fibonacci numbers that add up to N.
  6: Display this help message.

Please enter a command (0, 1, 2, 3, 4, 5 or 6): ''')

while command != ZERO:

    if command == ONE:
        
        n = int(input("You've asked for the first N Fibonacci numbers. What is N? "))
        while n < 0:
            print(ERRORMESSAGE)
            command = input("\nPlease enter a command (0, 1, 2, 3, 4, 5 or 6): ")
            n = int(input("You've asked for the first N Fibonacci numbers. What is N? "))
        else:
            print(firstNFibNumbers(n))
        command = input("\nPlease enter a command (0, 1, 2, 3, 4, 5 or 6): ")

    if command == TWO:
        
        i = int(input("You've asked for the ith Fibonacci number. What is i? "))
        while i < 0:
            print(ERRORMESSAGE)
            command = input("\nPlease enter a command (0, 1, 2, 3, 4, 5 or 6): ")
            i = int(input("You've asked for the ith Fibonacci number. What is i? "))
        else:
            print(ithFibNumber(i))
        command = input("\nPlease enter a command (0, 1, 2, 3, 4, 5 or 6): ")

    if command == THREE:

        n = int(input("You've asked for the Fibonacci numbers less than or equal to N. What is N? "))
        print(lessOrEqualToN(n))
        command = input("\nPlease enter a command (0, 1, 2, 3, 4, 5 or 6): ")

    if command == FOUR:

        n = int(input("You've asked how many Fibonacci numbers are less than or equal to N. What is N? "))
        print(numLessOrEqualToN(n))
        command = input("\nPlease enter a command (0, 1, 2, 3, 4, 5 or 6): ")

    if command == FIVE:

        n = int(input("You've asked for Fibonacci numbers that sum to N. What is N? "))
        while n < 0:
            print(ERRORMESSAGE)
            command = input("\nPlease enter a command (0, 1, 2, 3, 4, 5 or 6): ")
            n = int(input("You've asked for Fibonacci numbers that sum to N. What is N? "))
        else:
            print(largestFibNumsToN(n))
        command = input("\nPlease enter a command (0, 1, 2, 3, 4, 5 or 6): ")
    
    if command == SIX:

        command = input('''The following commands are available:
  0: Exit.
  1: List the first N Fibonacci numbers.
  2: Display the ith Fibonacci number (0-based).
  3: List the Fibonacci numbers less or equal to N.
  4: How many Fibonacci numbers are less or equal to N?
  5: Find a list of the largest Fibonacci numbers that add up to N.
  6: Display this help message.

Please enter a command (0, 1, 2, 3, 4, 5 or 6): ''')

    else:
        print("ERROR: Illegal command. Try again.\n")
        command = input('''The following commands are available:
  0: Exit.
  1: List the first N Fibonacci numbers.
  2: Display the ith Fibonacci number (0-based).
  3: List the Fibonacci numbers less or equal to N.
  4: How many Fibonacci numbers are less or equal to N?
  5: Find a list of the largest Fibonacci numbers that add up to N.
  6: Display this help message.

Please enter a command (0, 1, 2, 3, 4, 5 or 6): ''')
        

print("\nThanks for using the Fibonacci Laboratory! Goodbye.\n")
