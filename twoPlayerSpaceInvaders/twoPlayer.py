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

# shooting mechanics
velBulletTop = -8
velBulletBottom = 8
bulletsPlayer1 = []
bulletsPlayer2 = []
bulletSize = (5,5)
count = 30
rate1 = 10
rate2 = 10

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

# health and death checking
totalHealthP1 = 150
totalHealthP2 = 150
damage = 10

def checkDie():
    # checks if playerHealth <= 0, resets game if so
    if totalHealthP1 <= 0:
        resetGame()
    elif totalHealthP2 <= 0:
        resetGame()

# player hit check
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
startOrNot = False

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
winP1Text = smallFont.render(f"Wins: {winP1}", True, WHITE)
winP2Text = smallFont.render(f"Wins: {winP2}", True, WHITE)

def checkWin():
    global totalHealthP1
    global totalHealthP2
    global winP1
    global winP2
    global winP2Text
    global winP1Text

    if totalHealthP2 <= 0:
        winP1 += 1
        winP1Text = smallFont.render(f"Wins: {winP1}", True, WHITE)
    else:
        winP2 += 1
        winP2Text = smallFont.render(f"Wins: {winP2}", True, WHITE)

def resetGame():

    # getting access to the variables needed
    global totalHealthP1
    global totalHealthP2
    global bulletsPlayer1
    global bulletsPlayer2
    global playing
    global powerups
    global powerupsP1
    global powerupsP2
    
    # Check who won
    checkWin()

    #resetting them all
    totalHealthP1 = 150
    totalHealthP2 = 150
    bulletsPlayer1 = []
    bulletsPlayer2 = []
    playing = False
    powerups = []
    powerupsP1 = []
    powerupsP2 = []

# powerups
powerupDurationSec = 8
powerupDuration = powerupDurationSec * FPS
spawnDurationSec = 5
spawnDuration = spawnDurationSec * FPS
size = (20,20)
powerups = []
powerupsP1 = []
powerupsP2 = []
speedBoostImg = pygame.image.load("SpeedPickup.png").convert()
speedBoostImg = pygame.transform.scale(speedBoostImg, size)
speedBulletImg = pygame.image.load("SpeedBullet.png").convert()
speedBulletImg = pygame.transform.scale(speedBulletImg, size)
machineGunImg = pygame.image.load("MachineGun.png").convert()
machineGunImg = pygame.transform.scale(machineGunImg, size)

def resetSpeeds():
    global vel
    global vel1
    global velBulletBottom
    global velBulletTop
    global rate1
    global rate2

    vel = 5
    vel1 = 5
    rate1 = 10
    rate2 = 10
    velBulletBottom = 8
    velBulletTop = -8

# spawn powerup
def spawn():
    global powerups

    powerType = random.randint(0,2)
    spawnPos = (random.randint(50,750), random.randint(50, 550))

    if powerType == 0:
        # Speed Boost
        powerups.append([GREEN, spawnPos, speedBoostImg, 0])
    elif powerType == 1:
        # machine gun
        powerups.append([WHITE, spawnPos, machineGunImg, 1])
    else:
        # Speed Shot
        powerups.append([RED, spawnPos, speedBulletImg,2])

    if len(powerups) > 4:
        powerups.pop(0)

# increase speed powerup
def speedBoost(player):
    global vel
    global vel1

    speedBoost = 3
    if player == 1:
        vel += speedBoost
    else:
        vel1 += speedBoost

# shoot triple powerup
def machineGun(player):
    global rate1
    global rate2

    rateMultiplier = .5
    if player == 1:
        rate1 *= rateMultiplier
    else:
        rate2 *= rateMultiplier


# shoot faster powerup
def speedShot(player):
    global velBulletBottom
    global velBulletTop

    shotMultiplier = 2
    if player == 1:
        velBulletTop *= shotMultiplier
    else:
        velBulletBottom *= shotMultiplier

def pickup():
    global powerups
    global powerupsP1
    global powerupsP2

    # start the powerup
    for powerup in powerups:
        if powerup[1][0] in range(x-10, x+10) and powerup[1][1] in range(y, y+25):
            if powerup[3] == 0:
                powerupsP1.append([1, powerupDuration])
            elif powerup[3] == 1:
                powerupsP1.append([2, powerupDuration])
            else:
                powerupsP1.append([3, powerupDuration])
                
            powerups.remove(powerup)

        elif powerup[1][0] in range(x1-10, x1+10) and powerup[1][1] in range(y1-50, y1-25):
            if powerup  [3] == 0:
                powerupsP2.append([1, powerupDuration])
            elif powerup[3] == 1:
                powerupsP2.append([2, powerupDuration])
            else:
                powerupsP2.append([3, powerupDuration])
            
            powerups.remove(powerup)

def applyPowerups():
    for i in powerupsP1:
        i[1] -= 1
        if i[0] == 1:
            speedBoost(1)
        elif i[0] == 2:
            machineGun(1)
        else:
            speedShot(1)

        if i[1] <= 0:
            powerupsP1.remove(i)
        
    for i in powerupsP2:
        i[1] -= 1
        if i[0] == 1:
            speedBoost(2)
        elif i[0] == 2:
            machineGun(2)
        else:
            speedShot(2)

        if i[1] <= 0:
            powerupsP2.remove(i)

# obstacles
boulderSize = (70,70)
boulderDamage = 50
boulders = []
boulderDurationSec = 4
boulderDuration = boulderDurationSec * FPS
boulderIMG = pygame.image.load("Boulder.png")
boulderIMG = pygame.transform.scale(boulderIMG, boulderSize)

def spawnBoulder():
    global boulderIMG

    print("spawning Boulder")
    boulderVel = 45 * (1/FPS)
    side = random.randint(1, 2)
    if side == 1:
        ypos = -50
    else:
        ypos = 650
        boulderVel = -boulderVel
    xpos = random.randint(50,750)

    boulders.append([xpos, ypos, boulderVel, boulderIMG])

def moveBoulder():
    global boulders

    for boulder in boulders:
        boulder[1] += boulder[2]
        screen.blit(boulder[3], (boulder[0], boulder[1]))

def hitBoulder():
    global totalHealthP1
    global totalHealthP2

    for boulder in boulders:
        if x in range(boulder[0], boulder[0] + boulderSize[0]) and (y+25) in range(round(boulder[1]), round(boulder[1]) + boulderSize[1]):
            totalHealthP1 -= boulderDamage
            boulders.remove(boulder)
        if x1 in range(boulder[0], boulder[0] + boulderSize[0]) and (y1-25) in range(round(boulder[1]), round(boulder[1]) + boulderSize[1]):
            totalHealthP2 -= boulderDamage
            boulders.remove(boulder)

def removeBoulder():
    global boulders

    for boulder in boulders:
        if boulder[1] < -50:
            boulders.remove(boulder)
        elif boulder[1] > 650:
            boulders.remove(boulder)


# Pygame processes
running = True
def keyStrokes():
    global running
    global x
    global y
    global x1
    global y1
    global vel
    global vel1
    global startOrNot

    #Process input (events)
    for event in pygame.event.get():

        #Check for closing window
        if event.type == pygame.QUIT:
            running = False
        
        startOrNot = startButton.click(event)   

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
        x1 -= vel1
    if keys[pygame.K_RIGHT] and x1 < 780:
        x1 += vel1
    if keys[pygame.K_UP] and y1 > 320:
        y1 -= vel1
    if keys[pygame.K_DOWN] and y1 < 600:
        y1 += vel1

#Main Game Loop
while running:

    # pygame keystrokes and events
    keyStrokes()

    # main Menu check and logic
    mainMenu()

    # powerup changes
    resetSpeeds()
    pickup()
    applyPowerups()

    # boulder changes
    moveBoulder()
    hitBoulder()
    removeBoulder()

    # Shooting
    if count > 0:
        count -= 1
    else:
        count = 30

    if playing:
        if spawnDuration == 0:
            spawn()
            spawnDuration = spawnDurationSec * FPS
        else: 
            spawnDuration -= 1

        if boulderDuration == 0:
            spawnBoulder()
            boulderDuration = boulderDurationSec * FPS
        else:
            boulderDuration -= 1

        if count % rate1 == 0:
            bulletsPlayer1.append([x+10,y+25])
        if count % rate2 == 0:   
            bulletsPlayer2.append([x1+10,y1-25])

        shoot(bulletsPlayer1, velBulletTop)
        shoot(bulletsPlayer2, velBulletBottom)
        moveBoulder()

    # Collisions / Health / Reset
    checkHit(bulletsPlayer1, bulletsPlayer2, x, y, x1, y1-25)

    #Draw / Render

    # drawing powerups
    for i in powerups:
        screen.blit(i[2], i[1])

    screen.blit(winP1Text, (10, 10)) # win total player 1 text
    screen.blit(winP2Text, (10,560)) # win total player 2 text

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