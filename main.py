import pygame, sys, random, time, pygame.mixer, pygame.font
from pygame.locals import *
'''
main.py

Creates the outermost frame for the world

@authors: Dan Dangond, Akiva Gordon, Pravina Samaratunga
'''

size = 600, 450
screen = pygame.display.set_mode(size)


background = pygame.image.load('Images/background.png')
grass = pygame.image.load('Images/Grass tile.png')
ice = pygame.image.load('Images/Ice tile.png')
brick = pygame.image.load('Images/Brick tile.png')

def setup():
    print "opened window"
    screen.blit(background, (0, 0)) 
    print 'displayed background'
    pygame.display.update()
    pygame.event.pump()

    for i in range(150):
        time.sleep(.05)
        screen.blit(background, (0,0))
        screen.blit(ice, (4*i,3*i))
        pygame.display.update()
    
    time.sleep(1)
    
setup()
