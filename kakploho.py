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
    t.right(135)
hlcpt()

#sail
def sl():
    t.right(90)
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
    t.right(225)

sl()

#left man
def lft_man():
    t.left(225)
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
lft_man()

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
    t.done()
rckt()
