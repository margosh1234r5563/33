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
    trng_90(-265, 205, 45)
    turtle.right(270)
    trng_90(-220,210, 45)
    turtle.right(90)
    trng_90(-230, 160, 30)
    turtle.left(180)
    trng_90(-225, 160, 23)
    turtle.left(270)
    sqr(-215,240,23)
    turtle.left(270)
    prlm(-245,285, 20 )
    turtle.left(225)
    trng_90(-200, 205, 23)

rabbit()

def fish():
    turtle.left(270)
    trng_90(75, 225, 40)
    turtle.done()

fish()
