import pygame, sys
from pygame.locals import *

all_hats = pygame.sprite.Group()


class Hat(pygame.sprite.Sprite):
    def __init__(self, image, owner):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()  # transparent image
        self.rect = self.image.get_rect().move(owner.rect.centerx - 6, owner.rect.top - 12)  # rect is for blitting
        self.owner = owner
        pygame.sprite.Sprite.__init__(self, all_hats)
        
    def updateLocation(self):
        self.rect = self.rect.move(-1 * self.rect.x, -1 * self.rect.y)
        self.rect = self.rect.move(self.owner.rect.centerx - 6, self.owner.rect.top - 12)
    
