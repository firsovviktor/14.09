import turtle

turtle.shape('turtle')
turtle.right (90)
for i in range(10):
    turtle.forward(i*10+10)
    turtle.right(90)
    turtle.forward(i * 10 + 10)
    turtle.right(90)
    turtle.forward(i * 10 + 10)
    turtle.right(90)
    turtle.forward(i * 10 + 10)

    turtle.penup()
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.right(180)
    turtle.pendown()
