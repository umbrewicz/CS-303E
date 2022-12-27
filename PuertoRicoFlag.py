# File: PuertoRicoFlag.py
# Student: Nick Umbrewicz
# UT EID: nju96
# Course Name: CS303E
# 
# Date: 4/29/2022
# Description of Program: This program uses Turtle Graphics to draw the Puerto Rican flag.

import turtle

RED = '#E92228'
WHITE = '#FFFFFF'
BLUE = '#3A5EAB'

def drawRectangle(ttl, x, y, width, length, color):
    # draw the rectangle (red and white stripes) of the Puerto Rican flag

    stripeWidth = width // 5
    
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    
    for i in range(2):
        ttl.forward(length)
        ttl.right(90)
        ttl.forward(width)
        ttl.right(90)

    for i in range(3):
        ttl.penup()
        ttl.goto(x, y)
        ttl.setheading(0)
        ttl.pendown()
        ttl.pencolor(0, 0, 0)
        ttl.fillcolor(RED)
        ttl.begin_fill()
        
        for i in range(2):
            ttl.forward(length)
            ttl.right(90)
            ttl.forward(stripeWidth)
            ttl.right(90)
            
        ttl.end_fill()
        ttl.penup()
        y -= stripeWidth * 2
        
    ttl.penup()
    ttl.hideturtle()

def drawTriangle(ttl, x1, y1, x2, y2, x3, y3, color):
    # draw the blue triangle of the Puerto Rican flag
    
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()

    ttl.pencolor(0, 0, 0)
    ttl.fillcolor(BLUE)
    ttl.begin_fill()

    ttl.goto(x2, y2)
    ttl.goto(x3, y3)
    ttl.goto(x1, y1)

    ttl.end_fill()
    ttl.penup()
    ttl.hideturtle()

def drawStar(ttl, x, y, point_side_length, color):
    # draw the white star of the Puerto Rican flag

    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()

    ttl.pencolor(0, 0, 0)
    ttl.fillcolor(WHITE)
    ttl.begin_fill()

    triangle_points = 0

    while triangle_points < 5:
        ttl.forward(point_side_length)
        ttl.left(72)
        ttl.forward(point_side_length)
        ttl.right(144)
        triangle_points += 1
        
    ttl.end_fill()
    ttl.penup()
    ttl.hideturtle()

# running the program

Bill = turtle.Turtle()
Bill.speed(10)
drawRectangle(Bill, -300, 200, 400, 600, "black")
drawTriangle(Bill, -300, 200, 0, 0, -300, -200, "black")
drawStar(Bill, -264, 24, 56, "black")
