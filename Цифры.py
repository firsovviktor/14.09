c = [0] * 10
c[0] = (1, 1, 1, 1, 1, 0, 1, 0, 0)
c[1] = (0, 1, 0, 1, 0, 0, 0, 1, 0)
c[2] = (0, 1, 0, 0, 1, 0, 1, 0, 1)
c[3] = (0, 0, 0, 0, 1, 1, 0, 1, 1)
c[4] = (1, 1, 0, 1, 0, 1, 0, 0, 0)
c[5] = (1, 0, 0, 1, 1, 1, 1, 0, 0)
c[6] = (0, 0, 1, 1, 0, 1, 1, 1, 0)
c[7] = (0, 0, 1, 0, 1, 0, 0, 1, 0)
c[8] = (1, 1, 1, 1, 1, 1, 1, 0, 0)
c[9] = (1, 1, 0, 0, 1, 1, 0, 0, 1)


def draw1(n):
    d = c[n]
    for i in range(9):
        if d[i]==1:
            draw2(i+1)
    t.forward(70)

def draw2(n):
    t.penup()
    if (n==1):
        t.pendown()
        t.right(90)
        t.forward (40)
        t.backward (40)
        t.left(90)
        t.penup()
    if (n==2):
        t.forward(40)
        draw2(1)
        t.backward(40)
    if (n==3):
        t.right(90)
        t.forward (40)
        t.left(90)
        draw2(1)
        t.left(90)
        t.forward(40)
        t.right(90)
    if (n==4):
        t.forward(40)
        t.right(90)
        t.forward(40)
        t.left(90)
        draw2(1)
        t.left(90)
        t.forward(40)
        t.left(90)
        t.forward(40)
        t.right(180)
    if (n==5):
        t.left(90)
        draw2(1)
        t.right(90)
    if (n==6):
        t.right(90)
        t.forward(40)
        t.left(180)
        draw2(1)
        t.forward(40)
        t.right(90)
    if (n==7):
        t.right(90)
        t.forward(80)
        t.left(180)
        draw2(1)
        t.forward(80)
        t.right(90)
    if (n==8):
        t.forward(40)
        t.right(135)
        t.pendown()
        t.forward(40*2**0.5)
        t.penup()
        t.right(135)
        t.forward(40)
        t.right(90)
    if (n==9):
        t.right(90)
        t.forward(80)
        t.left(135)
        t.pendown()
        t.forward(40*2**0.5)
        t.penup()
        t.left(90)
        t.forward(40*2**0.5)
        t.right(135)
A = input().split()
for i in range(len(A)):
    A[i] = int(A[i])
import turtle as t
t.shape('turtle')
t.penup()
t.goto(-360, 0)
t.speed(0)
for i in range(len(A)):
    draw1(A[i])
t.exitonclick()