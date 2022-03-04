import turtle, time, random

#global variables
game_delay = 0.05
chase_delay = 1
NUM_OF_SHOTS = 1000
shot_speed = 20

#set up window
wn = turtle.Screen()
wn.title('Keep Away by Robbie')
wn.bgcolor('black')
wn.screensize(300,300)
wn.tracer(0)

#set up player
player = turtle.Turtle()
player.speed(0)
player.shape('arrow')
player.goto(0,0)
player.color('blue')
player.penup()

"""
#set up shooting mechanics
shots = []
for shot in range(0, NUM_OF_SHOTS):
    shot = turtle.Turtle()
    shot.hideturtle()
    shot.shape('circle')
    shot.goto(player.xcor(), player.ycor() + 10)
    shot.color('blue')
    shot.penup()
string = ''
for i in shots:
    string += i + ','
print(string)
"""

#set up enemies

enemy1 = turtle.Turtle()
enemy2 = turtle.Turtle()
enemy3 = turtle.Turtle()
enemy4 = turtle.Turtle()
enemy1.penup()
enemy2.penup()
enemy3.penup()
enemy4.penup()
enemy1.speed(0)
enemy2.speed(0)
enemy3.speed(0)
enemy4.speed(0)
enemy1.color('red')
enemy2.color('red')
enemy3.color('red')
enemy4.color('red')
enemy1.shape('square')
enemy2.shape('square')
enemy3.shape('square')
enemy4.shape('square')
enemy1.goto(-130,-130)
enemy2.goto(130,-130)
enemy3.goto(-130,130)
enemy4.goto(130,130)


#movement of enemies

#enemy one move funs
def e1_up():
    enemy1.sety(enemy1.ycor() + random.randint(0,7))
def e1_down():
    enemy1.sety(enemy1.ycor() - random.randint(0,7))
def e1_right():
    enemy1.setx(enemy1.xcor() + random.randint(0,7))
def e1_left():
    enemy1.setx(enemy1.xcor() - random.randint(0,7))
def shake1_ud():
    enemy1.sety(enemy1.ycor() + 2)
    enemy1.sety(enemy1.ycor() - 2)
def shake1_rl():
    enemy1.setx(enemy1.xcor() + 2)
    enemy1.setx(enemy1.xcor() - 2)
    

#enemy two move funs
def e2_up():
    enemy2.sety(enemy2.ycor() + random.randint(0,8))
def e2_down():
    enemy2.sety(enemy2.ycor() - random.randint(0,8))
def e2_right():
    enemy2.setx(enemy2.xcor() + random.randint(0,8))
def e2_left():
    enemy2.setx(enemy2.xcor() - random.randint(0,8))
def shake2_ud():
    enemy2.sety(enemy2.ycor() + 2)
    enemy2.sety(enemy2.ycor() - 2)
def shake2_rl():
    enemy2.setx(enemy2.xcor() + 2)
    enemy2.setx(enemy2.xcor() - 2)

#enemy three move funs
def e3_up():
    enemy3.sety(enemy3.ycor() + random.randint(0,7))
def e3_down():
    enemy3.sety(enemy3.ycor() - random.randint(0,7))
def e3_right():
    enemy3.setx(enemy3.xcor() + random.randint(0,7))
def e3_left():
    enemy3.setx(enemy3.xcor() - random.randint(0,7))
def shake3_ud():
    enemy3.sety(enemy3.ycor() + 2)
    enemy3.sety(enemy3.ycor() - 2)
def shake3_rl():
    enemy3.setx(enemy3.xcor() + 2)
    enemy3.setx(enemy3.xcor() - 2)

#enemy four move funs
def e4_up():
    enemy4.sety(enemy4.ycor() + random.randint(0,6))
def e4_down():
    enemy4.sety(enemy4.ycor() - random.randint(0,6))
def e4_right():
    enemy4.setx(enemy4.xcor() + random.randint(0,6))
def e4_left():
    enemy4.setx(enemy4.xcor() - random.randint(0,6))
def shake4_ud():
    enemy4.sety(enemy4.ycor() + 2)
    enemy4.sety(enemy4.ycor() - 2)
def shake4_rl():
    enemy4.setx(enemy4.xcor() + 2)
    enemy4.setx(enemy4.xcor() - 2)
    
def chase():
    #variables
    enemy1_disx = enemy1.xcor() - player.xcor()
    enemy1_disy = enemy1.ycor() - player.ycor()
    enemy2_disx = enemy2.xcor() - player.xcor()
    enemy2_disy = enemy2.ycor() - player.ycor()
    enemy3_disx = enemy3.xcor() - player.xcor()
    enemy3_disy = enemy3.ycor() - player.ycor()
    enemy4_disx = enemy4.xcor() - player.xcor()
    enemy4_disy = enemy4.ycor() - player.ycor()
    
    #enemy 1 if statements
    if enemy1_disx < 0 and enemy1_disy < 0:
        e1_right()
        e1_up()
    if enemy1_disx < 0 and enemy1_disy > 0:
        e1_right()
        e1_down()
    if enemy1_disx > 0 and enemy1_disy < 0:
        e1_left()
        e1_up()
    if enemy1_disx > 0 and enemy1_disy > 0:
        e1_left()
        e1_down()
    if enemy1_disx == 0 and enemy1_disy < 0:
        shake1_rl()
        e1_up()
    if enemy1_disx == 0 and enemy1_disy > 0:
        shake1_rl()
        e1_down()
    if enemy1_disx > 0 and enemy1_disy == 0:
        shake1_ud()
        e1_left()
    if enemy1_disx < 0 and enemy1_disy == 0:
        shake1_ud()
        e1_right()

    #enemy 2 if statements
    if enemy2_disx < 0 and enemy2_disy < 0:
        e2_right()
        e2_up()
    if enemy2_disx < 0 and enemy2_disy > 0:
        e2_right()
        e2_down()
    if enemy2_disx > 0 and enemy2_disy < 0:
        e2_left()
        e2_up()
    if enemy2_disx > 0 and enemy2_disy > 0:
        e2_left()
        e2_down()
    if enemy2_disx == 0 and enemy2_disy < 0:
        shake2_rl()
        e2_up()
    if enemy2_disx == 0 and enemy2_disy > 0:
        shake2_rl()
        e2_down()
    if enemy2_disx < 0 and enemy2_disy == 0:
        shake2_ud
        e2_right()
    if enemy2_disx > 0 and enemy2_disy == 0:
        shake2_ud()
        e2_left()

    #enemy 3 if statements
    if enemy3_disx < 0 and enemy3_disy < 0:
        e3_right()
        e3_up()
    if enemy3_disx < 0 and enemy3_disy > 0:
        e3_right()
        e3_down()
    if enemy3_disx > 0 and enemy3_disy < 0:
        e3_left()
        e3_up()
    if enemy3_disx > 0 and enemy3_disy > 0:
        e3_left()
        e3_down()
    if enemy3_disx == 0 and enemy3_disy < 0:
        shake3_rl()
        e3_up()
    if enemy3_disx == 0 and enemy3_disy > 0:
        shake3_rl()
        e3_down()
    if enemy3_disx < 0 and enemy3_disy == 0:
        shake3_ud()
        e3_right()
    if enemy3_disx > 0 and enemy3_disy == 0:
        shake3_ud()
        e3_left()

    #enemy 4 if statements
    if enemy4_disx < 0 and enemy4_disy < 0:
        e4_right()
        e4_up()
    if enemy4_disx < 0 and enemy4_disy > 0:
        e4_right()
        e4_down()
    if enemy4_disx > 0 and enemy4_disy < 0:
        e4_left()
        e4_up()
    if enemy4_disx > 0 and enemy4_disy > 0:
        e4_left()
        e4_down()
    if enemy4_disx == 0 and enemy4_disy < 0:
        shake4_rl()
        e4_up()
    if enemy4_disx == 0 and enemy4_disy > 0:
        shake4_rl()
        e4_down()
    if enemy4_disx < 0 and enemy4_disy == 0:
        shake4_ud()
        e4_right()
    if enemy4_disx > 0 and enemy4_disy == 0:
        shake4_ud()
        e4_left()
    

    
#movement functions of player
def move_up():
    player.sety(player.ycor() + 20)

def move_down():
    player.sety(player.ycor() - 20)

def move_right():
    player.setx(player.xcor() + 20)

def move_left():
    player.setx(player.xcor() - 20)

def turn_right():
    player.rt(10)

def turn_left():
    player.lt(10)

def shoot():
    pass

#check catch
def restart():
    time.sleep(1)
    enemy1.goto(-130,-130)
    enemy2.goto(130,-130)
    enemy3.goto(-130,130)
    enemy4.goto(130,130)
    player.goto(0,0)

def catch():
    if player.distance(enemy1) < 15:
        restart()
    elif player.distance(enemy2) < 15:
        restart()
    elif player.distance(enemy3) < 15:
        restart()
    elif player.distance(enemy4) < 15:
        restart()
        
#keybinds
wn.listen()    
wn.onkeypress(move_up, 'w')
wn.onkeypress(move_down, 's')
wn.onkeypress(move_right, 'd')
wn.onkeypress(move_left, 'a')
wn.onkeypress(turn_right, 'Right')
wn.onkeypress(turn_left, 'Left')
wn.onkeypress(shoot, 'space')

#game loop
while True:
    wn.update()
    time.sleep(game_delay)
    wn.ontimer(chase, chase_delay)
    catch()

turtle.mainloop()
    

    
    
