from turtle import *

speed(10)

def square(jesusnum):
    for sq in range(jesusnum):
        forward(100)
        right(90)
        
for cube in range(4):
    for row in range(4):
        square(4)
        forward(100)
    right(180)
    forward((row+1)*100)
    right(90)
    penup()
    forward(100)
    pendown()
    right(90)

penup()
right(90)
forward(100)
right(-90)
pendown()
