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

if True:
    print "opened window"
    screen.blit(background, (0, 0)) 
    print 'displayed background'
    pygame.display.update()
    pygame.event.pump()
    #time.sleep(1)

    '''
    for i in range(150):
        screen.blit(background, (0,0))
        screen.blit(ice, (4*i,3*i))
        pygame.display.update()
        pygame.event.pump()
    '''
        
    screen.blit(background, (0,0))
    plats = []
    for i in range(100):
        plats.append(i)
    for i in range(5):
        plats[i] = Platform(ice, 90+30*i, 30)
        screen.blit(plats[i].image, (plats[i].x, plats[i].y))
        
    pygame.display.update()
    
    for i in range(5):
        plats[i+5] = Platform(ice, 360+30*i, 30)
        screen.blit(plats[i+5].image, (plats[i+5].x, plats[i+5].y))
        
    pygame.display.update()
    
    for i in range(16):
        print "line 2"
        plats[i+10] = Platform(ice,60 + 30*i ,90)
        screen.blit(plats[i+10].image, (plats[i+10].x, plats[i+10].y))
    pygame.display.update()
    
    while True:
        time.sleep(1)
        pygame.event.pump()