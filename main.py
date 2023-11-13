import pygame
from pygame import mixer
import random
import asyncio
pygame.init()

# Create Screen
screen = pygame.display.set_mode((800, 800))

# Title and Icon
pygame.display.set_caption("Invoker Game")
icon = pygame.image.load("Invoker.png")
pygame.display.set_icon(icon)

# Sound
mixer.music.load('InvokeSound.wav')
mixer.music.set_volume(0.1)

# BelowHud
invoke = pygame.image.load('invoke.png')

# The Q W E
quas = pygame.image.load('quas.png')
wex = pygame.image.load('wex.png')
exort = pygame.image.load('exort.png')
pressedOrb = []
num_of_orbs = 0

for i in range(3):
    pressedOrb.append(exort)

# Gameover
font = pygame.font.Font('freesansbold.ttf', 96)

textX = 400
textY = 400

# Invoking
invokeParameter = 0
posParameter = [0, 0, 0]

# Enemy Aka Spells
alacrity = pygame.image.load('alacrity.png')
chaos_meteor = pygame.image.load('chaos-Meteor.png')
cold_snap = pygame.image.load('cold-snap.png')
deafening_blast = pygame.image.load('deafening-blast.png')
emp = pygame.image.load('emp.png')
forge_spirit = pygame.image.load('forge-spirit.png')
ghost_walk = pygame.image.load('ghost-walk.png')
ice_wall = pygame.image.load('ice-wall.png')
sun_strike = pygame.image.load('sun-strike.png')
tornado = pygame.image.load('tornado.png')

spell = []
spell.append(alacrity)
spell.append(chaos_meteor)
spell.append(cold_snap)
spell.append(deafening_blast)
spell.append(emp)
spell.append(forge_spirit)
spell.append(ghost_walk)
spell.append(ice_wall)
spell.append(sun_strike)
spell.append(tornado)

randomEnemy = []
enemyX = []
enemyY = []
enemyY_change = []
num_of_enemies = 3

for i in range(num_of_enemies):
    randomEnemy.append(random.randint(0, 9))
    enemyX.append(random.randint(0, 700))
    enemyY.append(-100)
    enemyY_change.append(0.075)



def enemy(x, y, i):
    screen.blit(spell[i], (x, y))

def game_over_text():
    over_text = font.render("Ha! You lose.", True, (255, 255, 255))
    screen.blit(over_text, (100, 350))

def drawOrbPos1(x, y):
    screen.blit(pressedOrb[0], (x, y))


def drawOrbPos2(x, y):
    screen.blit(pressedOrb[1], (x, y))


def drawOrbPos3(x, y):
    screen.blit(pressedOrb[2], (x, y))


def invokeUlt():
    mixer.music.play()
    print(invokeParameter)
    for i in range(num_of_enemies):
        if randomEnemy[i] == 0:
            if invokeParameter == 120:
                randomEnemy[i] = random.randint(0, 9)
                enemyX[i] = random.randint(0, 700)
                enemyY[i] = -100
        elif randomEnemy[i] == 1:
            if invokeParameter == 210:
                randomEnemy[i] = random.randint(0, 9)
                enemyX[i] = random.randint(0, 700)
                enemyY[i] = -100
        elif randomEnemy[i] == 2:
            if invokeParameter == 3:
                randomEnemy[i] = random.randint(0, 9)
                enemyX[i] = random.randint(0, 700)
                enemyY[i] = -100
        elif randomEnemy[i] == 3:
            if invokeParameter == 111:
                randomEnemy[i] = random.randint(0, 9)
                enemyX[i] = random.randint(0, 700)
                enemyY[i] = -100
        elif randomEnemy[i] == 4:
            if invokeParameter == 30:
                randomEnemy[i] = random.randint(0, 9)
                enemyX[i] = random.randint(0, 700)
                enemyY[i] = -100
        elif randomEnemy[i] == 5:
            if invokeParameter == 201:
                randomEnemy[i] = random.randint(0, 9)
                enemyX[i] = random.randint(0, 700)
                enemyY[i] = -100
        elif randomEnemy[i] == 6:
            if invokeParameter == 12:
                randomEnemy[i] = random.randint(0, 9)
                enemyX[i] = random.randint(0, 700)
                enemyY[i] = -100
        elif randomEnemy[i] == 7:
            if invokeParameter == 102:
                randomEnemy[i] = random.randint(0, 9)
                enemyX[i] = random.randint(0, 700)
                enemyY[i] = -100
        elif randomEnemy[i] == 8:
            if invokeParameter == 300:
                randomEnemy[i] = random.randint(0, 9)
                enemyX[i] = random.randint(0, 700)
                enemyY[i] = -100
        elif randomEnemy[i] == 9:
            if invokeParameter == 21:
                randomEnemy[i] = random.randint(0, 9)
                enemyX[i] = random.randint(0, 700)
                enemyY[i] = -100

async def main():
    global num_of_orbs
    global invokeParameter
    run = True
    while run:

        # Drawing the screen
        screen.fill((0, 0, 0))
        screen.blit(invoke, (700, 700))

        # Close Button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pressedOrb[2] = pressedOrb[1]
                    pressedOrb[1] = pressedOrb[0]
                    pressedOrb[0] = quas
                    if num_of_orbs < 3:
                        num_of_orbs += 1
                if event.key == pygame.K_w:
                    pressedOrb[2] = pressedOrb[1]
                    pressedOrb[1] = pressedOrb[0]
                    pressedOrb[0] = wex
                    if num_of_orbs < 3:
                        num_of_orbs += 1
                if event.key == pygame.K_e:
                    pressedOrb[2] = pressedOrb[1]
                    pressedOrb[1] = pressedOrb[0]
                    pressedOrb[0] = exort
                    if num_of_orbs < 3:
                        num_of_orbs += 1
                if event.key == pygame.K_r:
                    invokeUlt()

        if num_of_orbs == 1:
            drawOrbPos1(0, 700)

        if num_of_orbs == 2:
            drawOrbPos1(0, 700)
            drawOrbPos2(100, 700)

        if num_of_orbs > 2:
            for i in range(3):
                if pressedOrb[i] == quas:
                    posParameter[i] = 1
                if pressedOrb[i] == wex:
                    posParameter[i] = 10
                if pressedOrb[i] == exort:
                    posParameter[i] = 100

            invokeParameter = posParameter[0] + posParameter[1] + posParameter[2]
            drawOrbPos1(0, 700)
            drawOrbPos2(100, 700)
            drawOrbPos3(200, 700)

        # Enemy Movement
        for i in range(num_of_enemies):

            # Game over right here!
            if enemyY[i] > 750:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            enemyY_change[i] += 0.0000075
            enemyY[i] += enemyY_change[i]


            enemy(enemyX[i], enemyY[i], randomEnemy[i])

        pygame.display.update()
        await asyncio.sleep(0)
asyncio.run(main())
