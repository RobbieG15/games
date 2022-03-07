"""
@Author: Robert Greenslade
@
@Title: Two Player Game
@
@Date: June 28, 2021
"""

#Imports Needed
from ast import While
from turtle import width
import pygame

#Constant Variables for Window
WIDTH = 800
HEIGHT = 600
FPS = 30

# Colors
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

# Fonts
smallFont = pygame.font.SysFont('Corbel',35)

# player1 variables
x = 50
y = 50
vel = 5

# player2 variables
x1 = 50
y1 = 550
vel1 = 5

# shooting variables
velBulletTop = -5
velBulletBottom = 5
bulletsPlayer1 = []
bulletsPlayer2 = []
bulletSize = (5,5)
count = 30
rate = 15

def shoot(bullets, vel):
    for i in bullets:
        # checks to see if bullet is off screen to get rid of it 
        if i[1] < -50:
            bullets.remove(i)
        elif i[1] > 650:
            bullets.remove(i)
        
        # for each bullet in list, increment the position 
        i[1] -= vel
        
        # redraw the bullet at new position
        pygame.draw.rect(screen, WHITE, pygame.Rect(i, bulletSize))

# health
totalHealthP1 = 150
totalHealthP2 = 150
damage = 10

def checkDie():
    # checks if playerHealth <= 0, resets game if so
    if totalHealthP1 <= 0:
        resetGame()
    elif totalHealthP2 <= 0:
        resetGame()

# collision checking
def checkHit(bullets1, bullets2, x, y, x1, y1):

    # getting access to variables needed
    global totalHealthP1
    global totalHealthP2

    # checking for a hit
    for i in bullets1:
        if (i[0] in range(x1, x1+20)) and (i[1] in range(y1, y1+25)):
            bullets1.remove(i)
            totalHealthP2 -= damage
    for i in bullets2:
        if (i[0] in range(x, x+20)) and (i[1] in range(y, y+25)):
            bullets2.remove(i)
            totalHealthP1 -= damage
    
    # checking for a player death (health <= 0)
    checkDie()

# Main Menu
playing = False
playText = smallFont.render("Play", True, WHITE)

class Button:
    """Create a button, then blit the surface in the while loop"""
 
    def __init__(self, text,  pos, font, bg="black"):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, WHITE)
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
    def show(self):
        screen.blit(self.surface, (self.x, self.y))
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True

startButton = Button("Play", (350, 300), font=30, bg=GREEN)

def mainMenu():
    global playing

    if startOrNot:
        playing = True
        screen.fill(BLACK)
    if playing == False:
        startButton.show()




# Game reset
winP1 = 0
winP2 = 0

def checkWin():
    global totalHealthP1
    global totalHealthP2
    global winP1
    global winP2

    if totalHealthP2 <= 0:
        winP2 += 1
    else:
        winP1 += 1

def resetGame():

    # getting access to the variables needed
    global totalHealthP1
    global totalHealthP2
    global bulletsPlayer1
    global bulletsPlayer2
    global playing
    
    # Check who won
    checkWin()

    #resetting them all
    totalHealthP1 = 150
    totalHealthP2 = 150
    bulletsPlayer1 = []
    bulletsPlayer2 = []
    playing = False

#Main Game Loop
running = True
while running:



    #Process input (events)
    for event in pygame.event.get():

        #Check for closing window
        if event.type == pygame.QUIT:
            running = False
        
        startOrNot = startButton.click(event)
        

    # main Menu check and logic
    mainMenu()

    #keys
    keys = pygame.key.get_pressed()

    # Player 1 movement
    if keys[pygame.K_a] and x > 0:
        x -= vel
    if keys[pygame.K_d] and x < 780:
        x += vel
    if keys[pygame.K_w] and y > 0:
        y -= vel
    if keys[pygame.K_s] and y < 270:
        y += vel

    # Player 2 movement
    if keys[pygame.K_LEFT] and x1 > 0:
        x1 -= vel
    if keys[pygame.K_RIGHT] and x1 < 780:
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

    if playing:
        if count % rate == 0:
            bulletsPlayer1.append([x+10,y+25])
            bulletsPlayer2.append([x1+10,y1-25])

        shoot(bulletsPlayer1, velBulletTop)
        shoot(bulletsPlayer2, velBulletBottom)

    # Collisions / Health / Reset
    checkHit(bulletsPlayer1, bulletsPlayer2, x, y, x1, y1-25)

    #Draw / Render

    winP1Text = smallFont.render(f"Wins: {winP1}", True, WHITE)
    winP2Text = smallFont.render(f"Wins: {winP2}", True, WHITE)
    screen.blit(winP1Text, (10, 10))
    screen.blit(winP2Text, (10,560))

    pygame.draw.rect(screen, RED, pygame.Rect((625,10), (totalHealthP1, 20))) # red health bar
    pygame.draw.rect(screen, RED, (625, 10, 150, 20), 2, border_radius=1) # red health bar outline
    
    pygame.draw.rect(screen, BLUE, pygame.Rect((625, 570), (totalHealthP2, 20))) # blue health bar
    pygame.draw.rect(screen, BLUE, (625, 570, 150, 20), 2, border_radius=1) # blue health bar outline

    pygame.draw.polygon(screen, RED, points=[(x, y), (x+20, y), (x+10, y+25)]) # red player
    pygame.draw.polygon(screen, BLUE, points=[(x1, y1), (x1+20, y1), (x1+10, y1-25)]) # blue player
    
    # Update / Tick
    pygame.display.update()
    clock.tick(FPS)

    screen.fill(BLACK)