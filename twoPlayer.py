"""
@Author: Robert Greenslade
@
@Title: Two Player Game
@
@Date: June 28, 2021
"""

#Imports Needed
import pygame
import random

#Constant Variables
WIDTH = 800
HEIGHT = 600
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Initializing Pygame and Window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player Game @RobbieG15")
clock = pygame.time.Clock()

# player1 variables
x = 50
y = 50
vel = 5

# player2 variables
x1 = 50
y1 = 550
vel1 = 5

# shooting
velBulletTop = -5
velBulletBottom = 5
bulletsPlayer1 = []
bulletsPlayer2 = []
bulletSize = (5,5)
count = 30
rate = 15

def shoot(bullets, vel):
    for i in bullets:
        if i[1] < -50:
            bullets.remove(i)
        i[1] -= vel
        pygame.draw.rect(screen, WHITE, pygame.Rect(i, bulletSize))

# collision checking
def checkHit(bullets, x, y):
    for i in bullets:
        if (i[0] in range(x, x+10)) and (i[1] in range(y, y+25)):
            resetGame()

# Game reset
def resetGame():
    print('GameReset')

#Main Game Loop
running = True
while running:
    #Process input (events)
    for event in pygame.event.get():
        #Check for closing window
        if event.type == pygame.QUIT:
            running = False

    #keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > 0:
        x -= vel
    if keys[pygame.K_d] and x < 750:
        x += vel
    if keys[pygame.K_w] and y > 0:
        y -= vel
    if keys[pygame.K_s] and y < 270:
        y += vel

    if keys[pygame.K_LEFT] and x1 > 0:
        x1 -= vel
    if keys[pygame.K_RIGHT] and x1 < 750:
        x1 += vel
    if keys[pygame.K_UP] and y1 > 320:
        y1 -= vel
    if keys[pygame.K_DOWN] and y1 < 600:
        y1 += vel

    # Shooting
    if count > 0:
        count -= 1
    else:
        count = 30

    if count % rate == 0:
        bulletsPlayer1.append([x+10,y+25])
        bulletsPlayer2.append([x1+10,y1-25])

    shoot(bulletsPlayer1, velBulletTop)
    shoot(bulletsPlayer2, velBulletBottom)

    # collision checking
    checkHit(bulletsPlayer1, x1, y1)
    checkHit(bulletsPlayer2, x, y)

    #Draw / Render
    pygame.draw.polygon(screen, RED, points=[(x, y), (x+20, y), (x+10, y+25)])
    pygame.draw.polygon(screen, BLUE, points=[(x1, y1), (x1+20, y1), (x1+10, y1-25)])
    pygame.display.update()
    clock.tick(FPS)

    screen.fill(BLACK)