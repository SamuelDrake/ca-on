"""Cannon, hitting targets with projectiles.
Exercises
1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *
from freegames import vectorf

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:#Dibujar todas las pelotas
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):#Dibujar la bola del cañón
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:#Generar nuevas pelotas
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:#Mover pelotas
        target.x -= 0.5

    if inside(ball):#Actualizar la velocidad de la bola de cañón
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()#Crear una copia de todas las bolas
    targets.clear()

    for target in dupe:#Solo regresa a targets las bolas que no ha sido destruidas
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:#Checar si las bolas llegan al final
        if not inside(target):
            target.x=200#No, regresar al lado derecho

    ontimer(move, 50)

setup(420, 420, 370, 0)#Crear ventana
hideturtle()
up()
tracer(False)
onscreenclick(tap)#Checar entrada del mouse
move()
done()