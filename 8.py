import turtle as t
t.shape('turtle')
t.speed(0)
k=0.001
for i in range(360*12):
    t.forward(k*i)
    t.left(1)

t.exitonclick()