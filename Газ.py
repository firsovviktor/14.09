from random import randint
import turtle

def collide(n, m):
    turtle.color('red')
    turtle.penup()
    turtle.goto(0, 0)
    s='Вы убили черепашек под номерами '+str(n)+' и '+str(m)
    turtle.write(s, align='center', font=('Red', 20))

number_of_turtles = 20
t=[0]*20
for i in range(20):
    t[0][i]=randint(-200, 200) # x
    t[1][i]=randint(-200, 200) # y
    t[2][i]=randint(-10, 10) #vx
    t[3][i]=randint(-10, 10) #vy

steps_of_time_number = 100

turtle.penup()
turtle.goto(-300, -300)
turtle.pendown()
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.hideturtle()


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.goto(randint(-200, 200), randint(-200, 200))

for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(2)

n=randint(1, number_of_turtles-1)
m=randint(1, number_of_turtles)
if (m==n):
    m=n+1
collide(m, n)

turtle.exitonclick()

