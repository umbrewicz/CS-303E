# File: EasterSunday.py
# Student: Nick Umbrewicz
# UT EID: nju96
# Course Name: CS303E
#
# Date Created: January 28, 2022
# Date Last Modified: January 28, 2022
# Description of Program: This program returns the date of Easter Sunday in the year inputted by the user.

year = int(input("Enter year:"))
a = year % 19
b = year / 100
c = year % 100
d = b / 4
e = b % 4
g = (8 * b + 13) / 25
h = (19 * a + b - d - g + 15) % 30
j = c / 4
k = c % 4
m = (a + 11 * h) / 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
month = (h - m + r + 90) / 25
day = (h - m + r + month + 19) % 32

print("In " + str(year) + " Easter Sunday is on month " + str(month) + " and day " + str(day))