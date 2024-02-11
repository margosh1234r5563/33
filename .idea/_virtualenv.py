import turtle
turtle.setup(600, 600)
#Квадрат
def sqr(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)



#Ромб
def rmb(x,y,b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(b)
    turtle.right(45)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(45)
    turtle.forward(b)
    turtle.right(135)


#Правильный треугольник
def trng(x, y, c):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(c)
    turtle.right(120)
    turtle.forward(c)
    turtle.right(120)
    turtle.forward(c)

import math
#Прямоугольный треугольник
def trng_90(x,y,s):
    d = math.sqrt(2 * s * s)
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(s)
    turtle.right(135)
    turtle.forward(d)
    turtle.right(135)
    turtle.forward(s)

#Параллелограмм
import math
def prlm(x,y,m):
    e = math.sqrt(2 * m * m)
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(m)
    turtle.right(45)
    turtle.forward(e)
    turtle.right(135)
    turtle.forward(m)
    turtle.right(45)
    turtle.forward(e)
    turtle.right(135)

def rabbit():
    trng_90(-265,205, 45)
    turtle.right(270)
    trng_90(-220,210, 45)
    turtle.right(90)
    trng_90(-230,160, 30)
    turtle.left(180)
    trng_90(-225,160, 23)
    turtle.left(270)
    sqr(-215,240,23)
    turtle.left(270)
    prlm(-245,285, 20 )
    turtle.left(225)
    trng_90(-200,205, 23)

rabbit()

def fish():
    turtle.right(90)
    trng_90(75,225, 40)

    turtle.right(45)
    trng_90(41,285, 55)

    turtle.right(180)
    trng_90(41,170, 55)
    turtle.right(45)
    sqr(35,228,35 )
    turtle.right(45)
    prlm(-20,228, 30)
    turtle.right(180)
    trng_90(-45, 223, 25)
    turtle.right(270)
    trng_90(-50, 198, 25)

fish()

def cock():
    turtle.right(315)
    trng_90(255, 275, 25)
    turtle.right(45)
    sqr(240, 255, 25)
    trng_90(210, 225, 55)
    turtle.right(180)
    trng_90(205, 255, 55)
    turtle.right(45)
    prlm(145,255, 30 )
    trng_90(176, 285, 40)
    trng_90(235, 190, 25)

cock()

def fun_man():
    sqr(225, 70,31)
    turtle.right(135)
    trng_90(225,65,55)
    turtle.right(180)
    trng_90(220,65,55)
    turtle.right(90)
    trng_90(280,-35,25)
    turtle.right(270)
    trng_90(225, -30, 35)
    turtle.right(90)
    prlm(190, -65, 30)
    turtle.right(270)
    trng_90(210, -75, 25)

fun_man()
def yohuuuu():
    turtle.right(45)
    trng_90(-5,0,205)
    turtle.right(180)
    trng_90(0, 2, 205)
    turtle.right(180)
    prlm(-150, -150, 102)
    turtle.right(90)
    trng_90(0, -1, 102)
    turtle.right(225)
    trng_90(150, -150, 150)
    turtle.right(225)
    trng_90(78, 75, 102)
    turtle.left(270)
    sqr(4, 0, 100)

yohuuuu()

t=turtle.Pen()
import math
def sqr (x,y,a):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    for i in range (4):
        t.forward(a)
        t.left(90)

def rmb (x,y,b):
    t.penup()
    t.setposition(x, y)
    t.pendown()
    for i in range(2):
        t.forward(b)
        t.left(135)
        t.forward(b)
        t.left(45)

def trng_90 (x,y,e):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.forward(e)
    t.left(90)
    t.forward(e)
    t.left(135)
    t.forward(math.sqrt(e**2+e**2))
#в этой команде черепаха смотрит в лево
def trng (x,y,d):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.forward(d)
    t.right(90)
    t.forward(d)
    t.right(135)
    t.forward(math.sqrt(d**2+d**2))
def prlm (x,y,f):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    for i in range(2):
        t.forward(math.sqrt(f**2 + f**2))
        t.left(45)
        t.forward(f)
        t.left(135)

def hlcpt():
    t.pendown()
    t.left(45)
    trng_90(30,-290,55)
    t.right(135)
    trng(27,-290,55)
    t.left(135)
    trng(-33,-272,27)
    t.left(45)
    trng(-18,-253,27)
    t.left(135)
    sqr(-47,-240,28)
    trng_90(27,-210,45)
    prlm(30,-210,30)
hlcpt()

def sl():
    t.right(90)
    trng_90(-225,-146,27)
    t.left(180)
    trng(-225,-175,55)
    t.left(180)
    trng(-228,-193,55)
    trng(-225,-256,27)
    t.right(135)
    sqr(-184,-256,28)
    t.right(180)
    trng(-183,-258,40)
    t.left(135)
    prlm(-214,-286,28)
sl()
def lft_man():
    t.left(90)
    sqr(-215,114,31)
    t.right(135)
    trng(-227,12,55)
    prlm(-230,66,28)
    t.left(45)
    trng(-209,25, 55)
    t.right(90)
    trng(-206,-10,40)
    t.left(135)
    trng_90(-209,-53,27)
    t.left(90)
    trng_90(-262,-33,27)
lft_man()
def rckt():
    trng(225,-131,27)
    t.right(180)
    trng(225,-133,40)
    t.right(180)
    trng(224, -135, 55)
    t.left(135)
    trng_90(265,-175,55)
    t.right(135)
    sqr(201,-237,31)
    trng(199,-238,31)
    prlm(289,-278,31)
    turtle.done()
rckt()