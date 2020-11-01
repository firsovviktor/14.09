import turtle as t
n=int(input())
l=40
a=15
k=1.2
t.shape('turtle')
t.speed(1)
for i in range(2**(n-1)):
    d=0
    for j in range(n):
        if(j==n-1):
            t.color('green')
            t.width(3)
        t.forward(l/k**j)
        if (j == n - 1):
            t.color('black')
            t.width(1)
        b=(i//2**j)%2
        d+=(-1)**b
        t.left((-1)**b*a)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.right(d*a)
t.exitonclick()