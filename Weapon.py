import pygame, sys
from pygame.locals import *


class Fist(pygame.sprite.Sprite):
    
    def __init__(self, image, startX, startY, damage):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()  # transparent image
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.target = None
        self.dmg = damage
    
    
