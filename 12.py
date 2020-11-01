def cirr (k, n):
    for i in range(360*12):
        t.forward(k)
        t.left (i)
        t.forward(n)
        t.right (i)
        t.right(1)
    return 0

import turtle as t
t.shape('turtle')
t.speed(0)
n=0.5
cirr(1, n)

t.exitonclick()