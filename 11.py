def cirl (k):
    for i in range(360):
        t.forward(k)
        t.left(1)
    return 0

def cirr (k):
    for i in range(360):
        t.forward(k)
        t.right(1)
    return 0

import turtle as t
t.shape('turtle')
t.speed(0)
t.left(90)
k=0.1
for i in range (12):
    cirl(1+i*k)
    cirr(1+i*k)

t.exitonclick()