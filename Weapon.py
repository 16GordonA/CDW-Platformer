import pygame, sys
from pygame.locals import *


class Fist(pygame.sprite.Sprite):
    
    def __init__(self, image, startX, startY, damage):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()  # transparent image
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.owner = None
        self.dmg = damage
    
    def updateLocation(self):  # Only used when it has an owner
        if self.owner != None:
            self.rect = self.rect.move(-1 * self.rect.x, -1 * self.rect.y)
            self.rect = self.rect.move(self.owner.rect.right, self.owner.rect.centery - (self.rect.height / 2))

    def contactPlayer(self, target):
        if self.rect.bottom > target.rect.top and self.rect.top < target.rect.bottom and self.rect.right > target.rect.left and self.rect.left < target.rect.right and self.owner == None:
            self.owner = target
