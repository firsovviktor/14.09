from random import *
import turtle as t

while (1):
    a=random()
    b=randint(10, 50)
    t.right(a*360)
    t.forward(b)
t.exitonclick()