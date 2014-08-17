import pygame, sys, random, time, pygame.mixer, pygame.font
from pygame.locals import *

from Platform import Platform
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
    for i in range(116):
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
        plats[i+10] = Platform(ice,60 + 30*i ,90)
        screen.blit(plats[i+10].image, (plats[i+10].x, plats[i+10].y))
    pygame.display.update()
    
    for i in range(7):
        plats[i+26] = Platform(ice, 30*i, 150)
        screen.blit(plats[i+26].image, (plats[i+26].x, plats[i+26].y))
        
    for i in range(7):
        plats[i+33] = Platform(ice, 390+ 30*i, 150)
        screen.blit(plats[i+33].image, (plats[i+33].x, plats[i+33].y))
        
    pygame.display.update()
        
    for i in range(12):
        plats[i+40] = Platform(grass, 120+30*i, 210)
        screen.blit(plats[i+40].image, (plats[i+40].x, plats[i+40].y))
    
    pygame.display.update()
    
    for i in range(6):
        plats[i+52] = Platform(grass, 30*i, 270)
        screen.blit(plats[i+52].image, (plats[i+52].x, plats[i+52].y))
    
    for i in range(6):
        plats[i+58] = Platform(grass, 210+30*i, 270)
        screen.blit(plats[i+58].image, (plats[i+58].x, plats[i+58].y))
    
    for i in range(6):
        plats[i+64] = Platform(grass, 420+30*i, 270)
        screen.blit(plats[i+64].image, (plats[i+64].x, plats[i+64].y))
        
    for i in range(5):
        plats[i+70] = Platform(grass, 120+30*i, 330)
        screen.blit(plats[i+70].image, (plats[i+70].x, plats[i+70].y))
        
    for i in range(5):
        plats[i+75] = Platform(grass, 330+30*i, 330)
        screen.blit(plats[i+75].image, (plats[i+75].x, plats[i+75].y))
        
    for i in range(3):
        plats[i+80] = Platform(brick,  30*i, 390)
        screen.blit(plats[i+80].image, (plats[i+80].x, plats[i+80].y))
        
    for i in range(10):
        plats[i+83] = Platform(brick, 150 + 30*i, 390)
        screen.blit(plats[i+83].image, (plats[i+83].x, plats[i+83].y))
        
    for i in range(3):
        plats[i+93] = Platform(brick,  510+ 30*i, 390)
        screen.blit(plats[i+93].image, (plats[i+93].x, plats[i+93].y))
        
    for i in range(20):
        plats[i+96] = Platform(brick, 30*i, 450)
        screen.blit(plats[i+96].image, (plats[i+96].x, plats[i+96].y))
        
    pygame.display.update()
    
    while True:
        time.sleep(1)
        pygame.event.pump()