def cir(k):
    pi=3.1415926
    t.penup()
    t.left(90)
    t.forward(360/(2*pi))
    t.right(90)
    t.pendown()
    for i in range(360):
        t.forward(1)
        t.right (1)
    return 0

import turtle as t
n = 6
t.shape('turtle')
t.speed(0)

for i in range(n):
    t.penup()
    t.forward(50)
    t.backward(50)
    t.right(360/n)
    t.pendown()
    cir(1)

t.exitonclick()