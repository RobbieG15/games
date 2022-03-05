"""
@Author: Robert Greenslade
@
@Title: Pong
@
@Date: March 4th, 2022
"""

import turtle

wn = turtle.Screen()
wn.title('Pong @RobbieG15')
wn.bgcolor('black')
wn.setup(width=800, height=600)

#score
score_a = 0
score_b = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('blue')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('yellow')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('red')
ball.penup()
ball.goto(0,0)
ball.dx = 3.2
ball.dy = 3.2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align='center', font=("Courier", 24, 'normal'))

#function paddle_a movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

#function paddle_b movement
def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

#keyboard binding for paddle_a movement
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


#main game loop
while True:
    wn.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #boarder checking
    if ball.ycor() > 290:
        ball.sety(288)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-288)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -3.2
        score_a += 1
        pen.clear()
        pen.write(f"Player 1: {score_a}  Player 2: {score_b}", align='center', font=("Courier", 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = 3.2
        score_b += 1
        pen.clear()
        pen.write(f"Player 1: {score_a}  Player 2: {score_b}", align='center', font=("Courier", 24, 'normal'))

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        if ball.dx < 13:
            ball.dx *= -1.25
        else:
            ball.dx = 4

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        if ball.dx < 13:
            ball.dx *= -1.25
        else:
            ball.dx = 4
    
    #game score controls
    if score_a == 4:
        pen.goto(0,0)
        pen.write("Player 1 has won!", align='center', font=("Courier", 24, 'normal'))
        ball.goto(0,0)
        ball.dx *= 0 
        
    if score_b == 4:
        pen.goto(0,0)
        pen.write("Player 2 has won!", align='center', font=("Courier", 24, 'normal'))
        ball.goto(0,0)
        ball.dx *= 0 
        