import turtle
turtle.setup(600, 600)
t=turtle.Pen()

import math
def sqr (x,y,a):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    for i in range (4):
        t.forward(a)
        t.left(90)

def trng (x,y,d):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.forward(d)
    t.right(90)
    t.forward(d)
    t.right(135)
    t.forward(math.sqrt(d**2+d**2))

#Квадрат
def sqr(x, y, a):
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)

import math
#Прямоугольный треугольник
def trng_90(x,y,s):
    d = math.sqrt(2 * s * s)
    t.up()
    t.setposition(x,y)
    t.down()
    t.forward(s)
    t.right(135)
    t.forward(d)
    t.right(135)
    t.forward(s)

def prllgrm (x,y,f):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    for i in range(2):
        t.forward(math.sqrt(f**2 + f**2))
        t.left(45)
        t.forward(f)
        t.left(135)

#Параллелограмм
import math
def prlm(x,y,m):
    e = math.sqrt(2 * m * m)
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(m)
    t.right(45)
    t.forward(e)
    t.right(135)
    t.forward(m)
    t.right(45)
    t.forward(e)
    t.right(135)

def rabbit():
    trng_90(-265,205, 45)
    t.right(270)
    trng_90(-220,210, 45)
    t.right(90)
    trng_90(-230,160, 30)
    t.left(180)
    trng_90(-225,160, 23)
    t.left(270)
    sqr(-215,240,23)
    t.left(270)
    prlm(-245,285, 20 )
    t.left(225)
    trng_90(-200,205, 23)
    t.left(45)

def fish():
    t.right(135)
    trng_90(75,225, 40)

    t.right(45)
    trng_90(41,285, 55)

    t.right(180)
    trng_90(41,170, 55)
    t.right(45)
    sqr(35,228,35 )
    t.right(45)
    prlm(-20,228, 30)
    t.right(180)
    trng_90(-45, 223, 25)
    t.right(270)
    trng_90(-50, 198, 25)
    t.right(315)

#chicken
def chckn():
    trng_90(255, 275, 25)
    t.right(45)
    sqr(240, 255, 25)
    trng_90(210, 225, 55)
    t.right(180)
    trng_90(205, 255, 55)
    t.right(45)
    prlm(145,255, 30 )
    trng_90(176, 285, 40)
    trng_90(235, 190, 25)
    t.right(135)

#right man
def rght_man():
    t.left(135)
    sqr(225, 70,31)
    t.right(135)
    trng_90(225,65,55)
    t.right(180)
    trng_90(220,65,55)
    t.right(90)
    trng_90(280,-35,25)
    t.right(270)
    trng_90(225, -30, 35)
    t.right(90)
    prlm(190, -65, 30)
    t.right(270)
    trng_90(210, -75, 25)
    t.left(90)

#cube that is made from different shapes
def yohuuuu():
    t.right(135)
    trng_90(-5,0,205)
    t.right(180)
    trng_90(0, 2, 205)
    t.right(180)
    prlm(-150, -150, 102)
    t.right(90)
    trng_90(0, -1, 102)
    t.right(225)
    trng_90(150, -150, 150)
    t.right(225)
    trng_90(78, 75, 102)
    t.left(270)
    sqr(4, 0, 100)
    t.right(45)


#helicopter
def hlcpt():
    t.pendown()
    t.right(45)
    trng(30,-211,55)
    t.left(45)
    trng(27,-289,55)
    t.left(135)
    trng(-32,-272,27)
    t.left(45)
    trng(-17,-253,27)
    t.left(225)
    sqr(-45,-240,28)
    t.right(180)
    trng(-37,-208,45)
    t.left(225)
    prlm(30,-208,30)
    t.right(45)

#sail
def sl():
    t.left(180)
    trng(-198,-173,27)
    trng(-225,-175,55)
    t.left(180)
    trng(-228,-193,55)
    trng(-225,-256,27)
    t.right(45)
    sqr(-185,-256,28)
    t.right(270)
    trng(-184,-259,40)
    t.left(135)
    prllgrm(-216,-287,28)
    t.right(135)

#left man
def lft_man():
    t.right(135)
    sqr(-196,93,31)
    t.right(135)
    trng(-227,12,55)
    prllgrm(-230,66,28)
    t.left(45)
    trng(-209,25, 55)
    t.right(90)
    trng(-206,-10,40)
    t.left(45)
    trng(-209,-91,27)
    t.left(180)
    trng(-287,-50,27)
    t.left(135)

#spacecraft
def rckt():
    t.left(45)
    trng(199,-128,27)
    t.right(180)
    trng(198, -130, 40)
    t.right(180)
    trng(198, -133, 55)
    t.left(45)
    trng(238, -252, 55)
    t.right(45)
    sqr(220, -238, 31)
    t.left(90)
    trng(173, -239, 31)
    t.left(45)
    prlm(263, -283, 31)
    t.right(90)

rabbit()
fish()
chckn()
rght_man()
rckt()
hlcpt()
sl()
lft_man()
yohuuuu()
