import turtle
def trg(x,y,a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(60)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
trg(0,0,180)