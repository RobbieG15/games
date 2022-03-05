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
WIDTH = 360
HEIGHT = 480
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
all_sprites = pygame.sprite.Group()

#playerSize
x = 50
y = 50
width = 40
height = 60
vel = 5

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

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel

    #Update
    all_sprites.update()

    #Draw / Render
    pygame.draw.rect(screen, (255,0,0), (x,y,width,height))
    pygame.display.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)
    
    #Has to be after all other drawing
    pygame.display.flip()