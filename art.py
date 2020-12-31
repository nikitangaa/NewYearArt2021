#Happy NW! ;)
#By Nikita Gorbachev
import turtle
import random


WHITE = 'white'
RED = 'red'
LIGHTBLUE = 'lightblue'


t = turtle.Turtle()
def hat():
    t.speed(1)
    t.penup()
    t.goto(-90, -40)
    t.pendown()
    t.pensize(8)
    t.forward(180)
    t.circle(20, 180)
    t.forward(180)
    t.circle(20, 180)
    t.penup()
    t.circle(20, -180)
    t.right(90)
    t.pendown()
    t.fillcolor(RED)
    t.begin_fill()
    t.right(180)
    t.circle(180, -90)
    t.left(90)
    t.forward(180)
    t.end_fill()
    t.penup()
    t.left(180)
    t.forward(180)
    t.pendown()
    t.left(90)
    t.circle(-20, 360)
    t.penup()
    t.goto(-30, 0)
    t.write('Merry Xmas!)')
    

def snow():
    t.speed(9)
    t.pencolor(LIGHTBLUE)
    while (True):
        osx = random.randint(-300, 300)
        osy = random.randint(-300, 300)
        t.penup()
        t.goto(osx, osy)
        t.pendown()
        t.forward(46)
        t.right(180)
        t.forward(23)
        t.right(90)
        t.forward(23)
        t.right(180)
        t.forward(46)
        

hat()
snow()
turtle.done()
