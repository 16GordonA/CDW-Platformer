import pygame, sys, random, time, pygame.mixer, pygame.font
'''
main.py

Creates the outermost frame for the world

@authors: Dan Dangond, Akiva Gordon, Pravina Samaratunga
'''
def setup():
    size = 600, 450
    background = pygame.image.load("Images/background.png")
    print "hi"
    screen = pygame.display.set_mode(size) #not working?
    print "opened window"
    screen.blit(background, (0, 0))
    print 'displayed background'
    pygame.display.update()
    pygame.event.pump()
    print 'huh'
    #time.sleep(1000)
    
    
setup()