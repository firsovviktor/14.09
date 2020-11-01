def pol(n, l):
    pi=3.1415926
    t.penup()
    t.left(90)
    t.forward(l / (2 * np.sin(pi / n)))
    t.right(90)
    t.pendown()

    t.right(360/(2*n))
    for i in range(n):
        t.forward(l)
        t.right(360/n)
    t.left(360 / (2 * n))

    t.penup()
    t.right(90)
    t.forward(l / (2 * np.sin(pi / n)))
    t.left(90)
    t.pendown()
    return 0

import turtle as t
import numpy as np
t.shape('turtle')
t.left(90)

for i in range(10):
    pol(i+3, 100)

t.exitonclick()