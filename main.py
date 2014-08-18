import pygame, sys, random, time, pygame.mixer, pygame.font
from pygame.locals import *

from Platform import Platform
from Character import Character
from Hat import Hat
from Weapon import *

'''
main.py
Creates the outermost frame for the world
'''

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 459  # only to show bottommost layer, for all intensive purposes, the height is 450 pixels

size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(size)

background = pygame.image.load('Images/background.png')
background2 = pygame.image.load('Images/night.png')
grass = pygame.image.load('Images/Grass tile.png')
ice = pygame.image.load('Images/Ice tile.png')
brick = pygame.image.load('Images/Brick tile.png')
player = pygame.image.load('Images/Player.png')
wall = pygame.image.load('Images/wall.png')
ceiling = pygame.image.load('Images/Ceiling.png')
gel = pygame.image.load('Images/Blob Player.png')
blobert = pygame.image.load('Images/Blobert.png')

tophat = pygame.image.load('Images/topHat.png')

sword = pygame.image.load('Weapon Pics/Sword.png')
dagger = pygame.image.load('Weapon Pics/Dagger.png')
spear = pygame.image.load('Weapon Pics/Spear.png')

blobFist = pygame.image.load('Weapon Pics/blobertFist.png')
gelFist = pygame.image.load('Weapon Pics/Gel Fist.png')
stickFist = pygame.image.load('Weapon Pics/Stick Fist.png')

bow = pygame.image.load('Weapon Pics/Bow.png')
arrow = pygame.image.load('Weapon Pics/Arrow.png')

characterName = 'gel'  # blobert, gel or player


# read in plats from arena file
f = open("arena_1.txt", "r")
plats = []
plat_strings = []
for i in range(9):  # 9 IS THE LENGTH OF PLAT - NEEDS TO BE CHANGED IF NUMBER OF ROWS CHANGES
    plat_strings.append(f.readline())
plat_strings.remove(plat_strings[0])
plats.append(Platform(wall, -5, -125))
plats.append(Platform(wall, 600, -125))
plats.append(Platform(ceiling, -100, -100))
for p in range(len(plat_strings)):
    for c in range(len(plat_strings[p])):
        img = None
        if plat_strings[p][c] == "i":
            img = Platform(ice, c * 30, 30 + p * 60)
        elif plat_strings[p][c] == "g":
            img = Platform(grass, c * 30, 30 + p * 60)
        elif plat_strings[p][c] == "b":
            img = Platform(brick, c * 30, 30 + p * 60)
        if img is not None:
            plats.append(img)

if(characterName == 'blobert'):
    Dude = Character(blobert, 300, 400)
    Top = Hat(tophat, Dude)
    Fist = MeleeWeapon(blobFist, 300, 245, 5, "blobFist")
elif(characterName == 'gel'):
    Dude = Character(gel, 300, 400)
    #Top = Hat(tophat, Dude)
    Fist = MeleeWeapon(gelFist, 300, 245, 5, "gelFist")
elif(characterName == 'player'):
    Dude = Character(player, 300, 400)
    #Top = Hat(tophat, Dude)
    Fist = MeleeWeapon(stickFist, 300, 245, 5, "stickFist")

Sword = MeleeWeapon(sword, 150, 65, 8, "Sword")
Dagger = MeleeWeapon(dagger, 450, 65, 10, "Dagger")
Spear = MeleeWeapon(spear, 15, 210, 5, "Spear")
HandGun = RangeWeapon(blobFist, stickFist, 570, 60, 2, "HandGun", "Hand")
BowAndArrow = RangeWeapon(bow, arrow, 15, 425, 3, "Bow and Arrow", "Arrow")


weapons = [Fist, Sword, Dagger, Spear, HandGun, BowAndArrow]

while True:
    time.sleep(.01)
    screen.blit(background2, (0, 0))
    Dude.platformCheck = False

    key = pygame.key.get_pressed()

    Dude.updateSpeed(key)

    if key[K_ESCAPE]:
        sys.exit()

    if key[K_SPACE]:
        for i in range(len(weapons)):
            weapons[i].activate()

    for i in range(len(plats)):
        Dude.checkCollision(plats[i])
        Dude.platformCheck = False
        Dude.checkOnPlatform(plats[i])
        if Dude.platformCheck:
            Dude.land = True
        screen.blit(plats[i].image, plats[i].rect)

    Dude.updateLocation()
    for i in range(len(weapons)):
        if(weapons[i].owner == Dude):
            weapons[i].setDirection(Dude.direction)
    if(characterName == 'blobert'):
        Top.updateLocation()

    for i in range(len(weapons)):
        weapons[i].contactPlayer(Dude)
        weapons[i].updateLocation()
        weapons[i].tickTimer()

    screen.blit(Dude.image, Dude.rect)
    if(characterName == 'blobert'):
        screen.blit(Top.image, Top.rect)
    for i in range(len(weapons)):
        screen.blit(weapons[i].image, weapons[i].rect)
        if(isinstance(weapons[i], RangeWeapon)):
           for j in range(len(weapons[i].p_array)):
               screen.blit(weapons[i].p_array[j].image, weapons[i].p_array[j].rect)

    pygame.display.update()
    pygame.event.pump()
