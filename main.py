import pygame, sys, random, time, pygame.mixer, pygame.font
from pygame.locals import *

from Platform import Platform
from Character import Character
from Hat import Hat
from Weapon import *

'''
main.py
Creates the outermost frame for the world
@authors: Dan Dangond, Akiva Gordon, Pravina Samaratunga
'''

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 459 #only to show bottommost layer, for all intensive purposes, the height is 450 pixels

size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(size)

background = pygame.image.load('Images/background.png')
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

characterName = 'gel' #blobert, gel or player

plats = []
for i in range(119):
    plats.append(i)
        
for i in range(5):
    plats[i] = Platform(ice, 90+30*i, 30)    
for i in range(5):
    plats[i+5] = Platform(ice, 360+30*i, 30)

for i in range(16):
    plats[i+10] = Platform(ice,60 + 30*i ,90)

for i in range(7):
    plats[i+26] = Platform(ice, 30*i, 150)   
for i in range(7):
    plats[i+33] = Platform(ice, 390+ 30*i, 150)
            
for i in range(12):
    plats[i+40] = Platform(grass, 120+30*i, 210)

for i in range(6):
    plats[i+52] = Platform(grass, 30*i, 270)
for i in range(6):
    plats[i+58] = Platform(grass, 210+30*i, 270)
for i in range(6):
    plats[i+64] = Platform(grass, 420+30*i, 270)
plats[57] = Platform(grass, 135, 270)
plats[58] = Platform(grass, 225, 270)
plats[63] = Platform(grass, 345, 270)
plats[64] = Platform(grass, 435, 270)

for i in range(5):
    plats[i+70] = Platform(grass, 120+30*i, 330)
for i in range(5):
    plats[i+75] = Platform(grass, 330+30*i, 330)

for i in range(3):
    plats[i+80] = Platform(brick,  30*i, 390)        
for i in range(10):
    plats[i+83] = Platform(brick, 150 + 30*i, 390)        
for i in range(3):
    plats[i+93] = Platform(brick,  510+ 30*i, 390)
                
for i in range(20):
    plats[i+96] = Platform(brick, 30*i, 450)
    
plats[116] = Platform(wall, -5, -125)
plats[117] = Platform(wall, 600, -125)
plats[118] = Platform(ceiling, -100, -100)

if(characterName == 'blobert'):
    Dude = Character(blobert, 300, 400)
    Top = Hat(tophat, Dude)
    Fist = Fist(blobFist, 300, 245, 5)
elif(characterName == 'gel'):
    Dude = Character(gel, 300, 400)
    #Top = Hat(tophat, Dude)
    Fist = Fist(gelFist, 300, 245, 5) #should be changed also
elif(characterName == 'player'):
    Dude = Character(player, 300, 400)
    #Top = Hat(tophat, Dude)
    Fist = Fist(stickFist, 300, 245, 5) #should also be changed



while True:
    screen.blit(background, (0,0))
    
    Dude.platformCheck = False


    key = pygame.key.get_pressed()

    Dude.updateSpeed(key)

    
    if key[K_ESCAPE] == True:
        sys.exit()

    if key[K_SPACE] == True:
        Fist.activate()

    for i in range(118):
        Dude.checkCollision(plats[i])
        Dude.platformCheck = False
        Dude.checkOnPlatform(plats[i])
        if Dude.platformCheck == True:
            Dude.land = True
        screen.blit(plats[i].image, plats[i].rect)

    Dude.updateLocation()
    if(characterName == 'blobert'):
        Top.updateLocation()

    Fist.contactPlayer(Dude)
    Fist.updateLocation()
    Fist.tickTimer()

    screen.blit(Dude.image, Dude.rect)
    if(characterName == 'blobert'):
        screen.blit(Top.image, Top.rect)
    screen.blit(Fist.image, Fist.rect)

    pygame.display.update()
    pygame.event.pump()
