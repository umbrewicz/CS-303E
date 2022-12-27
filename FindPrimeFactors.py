# File: FindPrimeFactors.py
# Student: Nick Umbrewicz
# UT EID: nju96
# Course Name: CS303E
# 
# Date: 04/01/2022
# Description of Program: This program finds the prime factorization of a user-inputted number

import math

def isPrime(num):
    if (num < 2) or (num % 2 == 0):
        return (num == 2)
    divisor = 3
    while (divisor <= math.sqrt(num)):
        if num % divisor == 0:
            return False
        else:
            divisor += 2
    return True

def findNextPrime(num):
    if num < 2:
        return 2
    if num % 2 == 0:
        num -= 1
    guess = num + 2
    while (not isPrime(guess)):
        guess += 1
    return guess
        
print("Find Prime Factors:")
int1 = 1
list1 = []

while int1 != 0:
    int1 = int(input("Enter a positive integer (or 0 to stop): "))
    if int1 == 0:
        print("Goodbye!\n")
        pass
    elif int1 == 1:
        print("   1 has no prime factorization.\n")
    elif int1 < 0:
        print("   Negative integer entered. Try again.\n")
    else:
        if isPrime(int1) == True:
            list1.append(int1)
        else:
            list1 = []
            d = 2
            num = int1
            while num > 1:
                if num % d == 0:
                    num /= d
                    list1.append(d)
                else:
                    d = findNextPrime(d) 
        print("   The prime factorization of", int1, "is:", list1, "\n")
