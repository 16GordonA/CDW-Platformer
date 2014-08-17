import pygame, sys, random, time, pygame.mixer, pygame.font
from pygame.locals import *
'''
main.py

Creates the outermost frame for the world

@authors: Dan Dangond, Akiva Gordon, Pravina Samaratunga
'''
white = 255, 255, 255

def setup():
    size = 600, 450
    background = pygame.image.load('Images/background.png')
    grass = pygame.image.load('Images/Grass tile.png')
    ice = pygame.image.load('Images/Ice tile.png')
    brick = pygame.image.load('Images/Brick tile.png')
    screen = pygame.display.set_mode(size) #works
    print "opened window"
    pygame.draw.rect(
                screen, white, pygame.Rect(
                    20, 20, 20,
                    20)) #test draws rectangle
    screen.blit(background, (0, 0)) 
    print 'displayed background'
    pygame.display.update()
    #pygame.event.pump()

    for i in range(150):
        time.sleep(.05)
        screen.blit(background, (0,0))
        screen.blit(ice, (4*i,3*i))
        pygame.display.update()
    
    time.sleep(1)
    
setup()