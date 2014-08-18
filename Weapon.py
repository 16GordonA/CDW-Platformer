import pygame, sys
from pygame.locals import *


class MeleeWeapon(pygame.sprite.Sprite):
    
    def __init__(self, image, startX, startY, damage, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()  # transparent image
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.startX = startX
        self.startY = startY
        self.owner = None
        self.dmg = damage
        self.timer = 0  # counts five times
        self.cooldown = 0  # counts eight times starting at same time as timer
        self.activated = False
        self.name = name
        self.dir = 'R' # direction (L, R)
    
    def updateLocation(self):  # Only used when it has an owner and is activated
        if self.owner != None:
            if self.activated:
                self.rect = self.rect.move(-1 * self.rect.x, -1 * self.rect.y)
                if(self.owner.direction == 'R'):
                    self.rect = self.rect.move(self.owner.rect.right, self.owner.rect.centery - (self.rect.height / 2))
                else:
                    self.rect = self.rect.move(self.owner.rect.left - self.rect.width, self.owner.rect.centery - (self.rect.height/2))
            if self.owner.Item != self.name:
                self.owner = None
                self.timer = 0
                self.cooldown = 0
                self.activated = False
                self.rect = self.rect.move(-1 * self.rect.x, -1 * self.rect.y)
                self.rect = self.rect.move(self.startX, self.startY)

    def contactPlayer(self, target):
        if self.rect.bottom > target.rect.top and self.rect.top < target.rect.bottom and self.rect.right > target.rect.left and self.rect.left < target.rect.right and self.owner is None:
            self.owner = target
            self.rect = self.rect.move(999, 999)
            self.owner.refreshItem(self.name)

    def activate(self):
        if self.cooldown == 0:
            self.activated = True
            self.cooldown = 8
            self.timer = 5

    def tickTimer(self):
        if self.owner is not None:
            if self.cooldown > 0:
                self.cooldown -= 1
            if self.timer > 0:
                self.timer -= 1
            if self.timer == 0 and self.activated:
                self.activated = False  # lol guys its = not ==
                if self.rect.x < 700:
                    self.rect = self.rect.move(999, 999)
    
    def setDirection(self, dir):
        if self.dir == dir:
            pass
        else:
            self.image = pygame.transform.flip(self.image, True, False) #flips weapon horizontally
            self.dir = dir
