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
    print "hi"
    screen = pygame.display.set_mode(size) #works
    print "opened window"
    pygame.draw.rect(
                screen, white, pygame.Rect(
                    20, 20, 20,
                    20)) #test draws rectangle
    screen.blit(background, (0, 0)) 
    print 'displayed background'
    pygame.display.update()
    pygame.event.pump()
    print 'huh'
    time.sleep(1000)
    
    
setup()