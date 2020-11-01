def st(n):
    for i in range(n):
        t.forward(200)
        t.right(180 - 180 / n)

import turtle as t
t.shape('turtle')
st(5)
t.penup()
t.goto(-200, 0)
t.pendown()
st(11)
t.exitonclick()