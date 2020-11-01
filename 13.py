def cir(k):
    pi=3.1415926
    t.penup()
    t.left(90)
    t.forward(360*k/(2*pi))
    t.right(90)
    t.pendown()
    for i in range(360):
        t.forward(k)
        t.right (1)
    return 0

def cir2(k):
    pi=3.1415926
    t.penup()
    t.left(90)
    t.forward(360*k/(2*pi))
    t.right(90)
    t.pendown()
    for i in range(180):
        t.forward(k)
        t.right (1)
    return 0

import turtle as t
pi=3.1415926
t.shape('turtle')
t.speed(0)
t.color('yellow')
t.begin_fill()
cir(1.5)
t.end_fill()
t.penup()
t.color('black')

t.goto(0, 0)
t.left(90)
t.forward(40)
t.left(90)
t.forward(30)

t.color('blue')
t.begin_fill()
cir(0.2)
t.end_fill()

t.penup()
t.goto(0, 0)
t.right(90)
t.forward(40)
t.right(90)
t.forward(30)

t.begin_fill()
cir(0.2)
t.end_fill()
t.penup()

t.color('black')
t.width(6)
t.goto(0, 10)
t.pendown()
t.right(90)
t.forward(30)

t.penup()
t.color('red')
cir2(pi/4.5)
t.exitonclick()