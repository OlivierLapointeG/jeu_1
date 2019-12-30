import turtle as tu

import random as rn

import time

import numpy as np


"""
Définissons des tortues
"""
goal = tu.Turtle(visible=False)
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
    for _ in range(6):
        if abs(bob.pos()[0]) < 293 and abs(bob.pos()[1]) < 243:
            bob.right(7)
            bob.fd(4)

def mleft():
    for _ in range(6):
        if abs(bob.pos()[0]) < 293 and abs(bob.pos()[1]) < 243:
            bob.left(7)
            bob.fd(4)


speed = 2
point = 0

def acce():
    global speed
    speed = 4

def dcce():
    global speed
    speed = 2

fen.listen()


fen.onkey(mright,'Right')
fen.onkey(mleft, 'Left')
fen.onkey(acce, 'Up')
fen.onkeypress(acce, 'Up')
fen.onkeyrelease(dcce, 'Up')

def goalspawn():
    goal.speed(0)
    goal.up()
    goal.shape('circle')
    goal.color('red')
    goal.shapesize(0.5)
    goal.setpos(rn.randint(-200,200),rn.randint(-200,200))
    goal.showturtle()

def score():
    global point
    scorer = tu.Turtle(visible=False)
    scorer.up()
    scorer.speed(0)
    scorer.setpos(-20, 270)
    scorer.color('lightblue')
    scorer.begin_fill()
    scorer.fd(100)
    scorer.setheading(90)
    scorer.fd(30)
    scorer.setheading(180)
    scorer.fd(110)
    scorer.setheading(270)
    scorer.fd(30)
    scorer.setheading(0)
    scorer.fd(10)
    scorer.end_fill()
    scorer.color("black")
    scorer.setpos(-10, 270)
    scorer.write(point, font=("Arial", 20, "normal"))
    point += 1

goalspawn()
score()

while True:
    bob.fd(speed)
    if ((bob.pos()[1] - goal.pos()[1]) ** 2 + (bob.pos()[0] - goal.pos()[0]) ** 2) ** 0.5 < 17:
        goalspawn()
        score()
    a = bob.pos()
    if abs(a[0]) >= 296:
        bob.left(180 - 2* bob.heading())
    if abs(bob.pos()[1]) >= 246:
        bob.left(360 - 2* bob.heading())