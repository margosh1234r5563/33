import turtle
t=turtle.Pen()
turtle.setup(600, 600)
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
    trng(-225,-176,55)
    t.left(180)
    trng(-228,-193,55)
    trng(-223,-256,27)
    t.right(135)
    sqr(-182,-256,28)
    t.right(180)
    trng(-183,-258,40)
    t.left(135)
    prlm(-214,-287,28)
sl()
def lft_man():
    t.left(90)
    sqr(-225,90,31)
    t.right(135)
    trng(-237,-12,55)
    prlm(-240,42,28)
    t.left(45)
    trng(-219,1, 55)
    t.right(90)
    trng(-216,-34,40)
    t.left(135)
    trng_90(-219,-77,27)
    t.left(90)
    trng_90(-272,-47,27)
lft_man()
def rckt():
    trng(225,-146,27)
    t.right(180)
    trng(225,-148,40)
    t.right(180)
    trng(224, -150, 55)
    t.left(135)
    trng_90(265,-190,55)
    t.right(135)
    sqr(201,-252,31)
    trng(199,-253,31)
    prlm(289,-298,31)
rckt()



