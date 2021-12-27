import turtle
import time
import random

retraso = 0.1
marcador = 0
marcador_alto = 0

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("gray")
s.title("Proyecto Snake")

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape('square')
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = 'stop'
serpiente.color('green')

comida = turtle.Turtle()
comida.shape("circle")
comida.color("orange")
comida.penup()
comida.speed(0)
comida.goto(0,100)

cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,-260)
texto.write("Marcador:0 \tMarcador mas alto: 0", align="center",font=("verdana", 24, "normal"))

def arriba():

 serpiente.direction = "up"

def abajo():
    serpiente.direction = "down"

def derecha():
    serpiente.direction = "right"

def izquierda():
    serpiente.direction = "left"

def movimiento():
    if serpiente.direction == "up":
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    if serpiente.direction == "down":
        y = serpiente.ycor()
        serpiente.sety(y + -20)
    if serpiente.direction == "right":
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    if serpiente.direction == "left":
        x = serpiente.xcor()
        serpiente.setx(x - 20)

s.listen()
s.onkeypress(arriba,"Up")
s.onkeypress(abajo,"Down")
s.onkeypress(izquierda,"Left")
s.onkeypress(derecha,"Right")

while True:
    s.update()

    if serpiente.xcor() > 300 or serpiente.xcor() < -300 or serpiente.ycor() > 300 or serpiente.ycor() < -300:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = "stop"
        cuerpo.clear()

        marcador = 0
        texto.clear()
        texto.write("Marcador:{}\tMarcador mas alto:{}".format(marcador,marcador_alto),align = "center", font=("verdana",24,"normal"))

    if serpiente.distance(comida) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        comida.goto(x,y)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("green")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)

        marcador += 10
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write("Marcador:{}\tMarcador mas alto:{}".format(marcador,marcador_alto),align = "center", font=("verdana",24,"normal"))


    total = len(cuerpo)
    for index in range (total -1,0,-1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x,y)
        
    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x,y)

    movimiento()

    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
            serpiente.direction = "stop"


    time.sleep(retraso)


turtle.done()
