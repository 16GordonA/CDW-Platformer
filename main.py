import pygame, sys, random, time, pygame.mixer, pygame.font
from pygame.locals import *

from Platform import Platform
'''
main.py

Creates the outermost frame for the world

@authors: Dan Dangond, Akiva Gordon, Pravina Samaratunga
'''

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 450

size = SCREEN_HEIGHT, SCREEN_WIDTH
screen = pygame.display.set_mode(size)

background = pygame.image.load('Images/background.png')
grass = pygame.image.load('Images/Grass tile.png')
ice = pygame.image.load('Images/Ice tile.png')
brick = pygame.image.load('Images/Brick tile.png')

while True:
    print "opened window"
    screen.blit(background, (0, 0)) 
    print 'displayed background'
    pygame.display.update()
    pygame.event.pump()
    time.sleep(1)

    for i in range(150):
        screen.blit(background, (0,0))
        screen.blit(ice, (4*i,3*i))
        pygame.display.update()
        pygame.event.pump()
        
    screen.blit(background, (0,0))
    plats = [0,1,2,3,4,5,6,7,8,9]    
    for i in range(10):
        plats[i] = Platform(ice, 40*i, 30*i)
        screen.blit(plats[i].image, (plats[i].x, plats[i].y))
        
    
    time.sleep(10)



