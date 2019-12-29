import turtle as tu

import random as rn

import time

"""
Définissons des tortues
"""
bob = tu.Turtle()
bob.up()
bob.color('green')
bob.speed(0)
bob.shapesize(2)
carre = tu.Turtle()
carre.speed(0)
carre.pensize(5)
carre.up()
carre.setpos(300, 250)
carre.setheading(270)
carre.down()
carre.fd(500)
carre.right(90)
carre.fd(600)
carre.right(90)
carre.fd(500)
carre.right(90)
carre.fd(600)
carre.right(90)
carre.hideturtle()
carre.up()
carre.setpos(-100,0)
carre.down()

def perdre():
    fen.clearscreen()
    carre.write('Vous avez perdu', font=('Arial', 40, 'bold'))


"""
définissons notre fenêtre de jeu
"""
fen = tu.Screen()
fen.bgcolor('lightblue')

def mright():
    if abs(bob.pos()[0]) < 293 and abs(bob.pos()[1]) < 243:
        bob.right(20)

def mleft():
    if abs(bob.pos()[0]) < 293 and abs(bob.pos()[1]) < 243:
        bob.left(20)

def droite():
    if abs(bob.pos()[0]) < 293 and abs(bob.pos()[1]) < 243:
        bob.right(7)
        bob.fd(5)

def gauche():
    if abs(bob.pos()[0]) < 293 and abs(bob.pos()[1]) < 243:
        bob.left(7)
        bob.fd(5)

speed = 2


def acce():
    global speed
    speed = 4.5

def dcce():
    global speed
    speed = 2

fen.listen()


fen.onkey(mright,'Right')
fen.onkeypress(droite, "Right")
fen.onkeypress(gauche, 'Left')
fen.onkey(mleft, 'Left')
fen.onkey(acce, 'Up')
fen.onkeypress(acce, 'Up')
fen.onkeyrelease(dcce, 'Up')

def goalspawn():
    goal = tu.Turtle(visible=False)
    goal.up()
    goal.shape('circle')
    goal.color('red')
    goal.shapesize(1)
    goal.setpos(rn.randint(-200,200),rn.randint(-200,200))
    goal.showturtle()

goalspawn()

while True:
    bob.fd(speed)
    a = bob.pos()
    if abs(a[0]) >= 296:
        bob.left(180 - 2* bob.heading())
    if abs(bob.pos()[1]) >= 246:
        bob.left(360 - 2* bob.heading())