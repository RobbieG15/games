"""
@Author: Robert Greenslade
@
@Title: Pygame Template 
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
pygame.display.set_caption("Pygame Template @RobbieG15")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

#Main Game Loop
running = True
while running:
    #Process input (events)
    for event in pygame.event.get():
        #Check for closing window
        if event.type == pygame.QUIT:
            running = False
    #Update
    all_sprites.update()

    #Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    
    #Has to be after all other drawing
    pygame.display.flip()