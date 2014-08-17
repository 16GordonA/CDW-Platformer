import pygame, sys
'''
Created on Aug 17, 2014

@author: Akiva 
'''

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 450
class Platform(pygame.sprite.Sprite):
    '''
    Character can stand on this
    '''


    def __init__(self, image, x, y): #x,y refer to location of top left corner of platform
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect().move(x, y)
        self.x = x
        self.y = y
