from random import *
import turtle as t
t.shape('turtle')
t.speed(2)
vy=20
x=0
y=0
k=0.75
while (1):
    x += 1
    y += vy
    vy -= 1
    if (y<=0):
        vy = k*abs(vy)
    t.goto(x, y)
t.exitonclick()