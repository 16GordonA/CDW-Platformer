import pygame, sys
from pygame.locals import *


class MeleeWeapon(pygame.sprite.Sprite):
    
    def __init__(self, image, startX, startY, damage):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()  # transparent image
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.owner = None
        self.dmg = damage
        self.timer = 0  # counts five times
        self.cooldown = 0  # counts eight times starting at same time as timer
        self.activated = False
    
    def updateLocation(self):  # Only used when it has an owner and is activated
        if self.owner is not None and self.activated:
            self.rect = self.rect.move(-1 * self.rect.x, -1 * self.rect.y)
            self.rect = self.rect.move(self.owner.rect.right, self.owner.rect.centery - (self.rect.height / 2))

    def contactPlayer(self, target):
        if self.rect.bottom > target.rect.top and self.rect.top < target.rect.bottom and self.rect.right > target.rect.left and self.rect.left < target.rect.right and self.owner is None:
            self.owner = target
            self.rect = self.rect.move(999, 999)

    def activate(self):
        if self.cooldown == 0:
            self.activated = True
            self.cooldown = 8
            self.timer = 5

    def tickTimer(self):
        if self.owner is None:
            if self.cooldown > 0:
                self.cooldown -= 1
            if self.timer > 0:
                self.timer -= 1
            if self.timer == 0 and self.activated:
                self.activated = False  # lol you guys had == here before
                if self.rect.x < 700:
                    self.rect = self.rect.move(999, 999)
