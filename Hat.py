import pygame, sys
from pygame.locals import *


class Hat(pygame.sprite.Sprite):
    def __init__(self, image, target):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()  # transparent image
        self.rect = self.image.get_rect().move(target.rect.centerx - 6, target.rect.top - 12)  # rect is for blitting
        self.target = target
        
    def updateLocation(self):
        self.rect = self.rect.move(-1 * self.rect.x, -1 * self.rect.y)
        self.rect = self.rect.move(self.target.rect.centerx - 6, self.target.rect.top - 12)
    
