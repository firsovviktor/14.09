import turtle as t
n = int(input())
t.shape('turtle')

for i in range(n):
    t.forward(50)
    t.stamp()
    t.backward(50)
    t.right(360/n)
t.left(360/n)
t.forward(50)

t.exitonclick()