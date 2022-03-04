import turtle
import time

turtle.bgcolor('black')

arb_pers = turtle.Turtle()
arb_pers.hideturtle()
arb_pers.penup()
arb_pers.speed(9)
arb_pers.shape('triangle')
arb_pers.color('white')
arb_pers.setpos(-80, 130)
arb_pers.shapesize(stretch_wid=3, stretch_len=3)

arb_di = turtle.Turtle()
arb_di.hideturtle()
arb_di.penup()
arb_di.speed(9)
arb_di.color('white')
arb_di.setpos(-100, 150)


ligne1=turtle.Turtle()
ligne2=turtle.Turtle()
ligne1.color('white')
ligne2.color('white')
ligne1.speed(9)
ligne2.speed(9)
ligne1.hideturtle()
ligne2.hideturtle()
ligne1.right(45)
ligne2.right(135)
ligne1.penup()
ligne1.setpos(200,-50)
ligne2.penup()
ligne2.setpos(-200,-50)
ligne1.pensize(6)
ligne2.pensize(6)


title = turtle.Turtle()
title.hideturtle()
title.penup()
title.color('white')
title.setpos(0,220)

marbre = turtle.Turtle()
premier = turtle.Turtle()
deuxieme = turtle.Turtle()
troisieme = turtle.Turtle()

def creer_but(but, x, y):
    but.hideturtle()
    but.penup()
    but.left(45)
    but.shape('square')
    but.shapesize(stretch_wid=3, stretch_len=3)
    but.color('white')
    but.speed(9)
    but.setpos(x, y)


creer_but(marbre, 0, 150)
creer_but(premier,-200,-50)
creer_but(deuxieme,0,-250)
creer_but(troisieme,200,-50)

marbre.showturtle()
time.sleep(0.5)
marbre.speed(3)
marbre.pensize(6)
marbre.pendown()
marbre.setpos(-200,-50)
premier.showturtle()
time.sleep(0.5)
marbre.setpos(0,-250)
deuxieme.showturtle()
time.sleep(0.5)
marbre.setpos(200,-50)
troisieme.showturtle()
time.sleep(0.5)
marbre.setpos(0,150)

ligne1.pendown()
ligne2.pendown()

while True:
    ligne1.forward(4)
    ligne2.forward(4)
    if ligne2.xcor() <= -600:
        break


title.write('Mathball', False, 'center',('Courier', 80, 'bold'))

time.sleep(2)
title.clear()
title.write('0 - 0', False, 'center', ('Courier', 100, 'bold'))



