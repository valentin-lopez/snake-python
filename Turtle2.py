#probando comandos
import turtle

s = turtle.Screen()
t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.right(90)

while i <= 100:
    t.circle(i)
    i+=1

turtle.done()