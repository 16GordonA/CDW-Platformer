import pygame, sys, random, time, pygame.mixer, pygame.font
from pygame.locals import *

from Platform import Platform
from Character import Character

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

plats = []
for i in range(116):
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

Dude = Character(player, 285, 405)

while True:
    screen.blit(background, (0,0))
    screen.blit(Dude.image, Dude.rect)
    for i in range(116):
        screen.blit(plats[i].image, plats[i].rect)
        
    pygame.display.update()
    pygame.event.pump()
