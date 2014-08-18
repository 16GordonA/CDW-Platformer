import pygame, sys
from pygame.locals import *

all_weapons = pygame.sprite.Group()
all_projs = pygame.sprite.Group()


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
        self.cooldownMax = 8
        self.floatcount = 0
        self.floatcountMax = 1000
        self.activated = False
        self.name = name
        self.dir = 'R'  # direction (L, R)
        pygame.sprite.Sprite.__init__(self, all_weapons)

    def updateLocation(self):  # Only used when it has an owner and is activated
        if self.owner is not None:
            if self.activated:
                self.rect = self.rect.move(-1 * self.rect.x, -1 * self.rect.y)
                if(self.owner.direction == 'R'):
                    self.rect = self.rect.move(self.owner.rect.right, self.owner.rect.centery - (self.rect.height / 2))
                else:
                    self.rect = self.rect.move(self.owner.rect.left - self.rect.width, self.owner.rect.centery - (self.rect.height / 2))
            if self.owner.item != self.name:
                self.owner = None
                self.timer = 0
                self.cooldown = 0
                self.activated = False
                self.rect = self.rect.move(-1 * self.rect.x, -1 * self.rect.y)
                self.rect = self.rect.move(self.startX, self.startY)
        """
        else:
            if self.floatcount == self.floatcountMax:
                self.floatcount = -self.floatcountMax * 2
            elif self.floatcount < -self.floatcountMax:
                pass
            elif self.floatcount < 0 and self.floatcount > -10:
                self.rect = self.rect.move(self.rect.x, self.rect.y - 1)  # assumes not at the top
            elif self.floatcount >= 0 and self.floatcount < 10:
                self.rect = self.rect.move(self.rect.x, self.rect.y + 1)  # assumes not at the top
                self.floatcount += 1
        """

    def contactPlayer(self, target):
        if self.rect.bottom > target.rect.top and self.rect.top < target.rect.bottom and self.rect.right > target.rect.left and self.rect.left < target.rect.right and self.owner is None:
            if self.owner is not None and self.owner != target:
                "hyah"
                target.setHP(target.HP - self.dmg)
                self.rect = self.rect.move(999, 999)
            else:
                self.owner = target
                self.rect = self.rect.move(999, 999)
                self.owner.refreshItem(self.name)

    def setOwner(self, target):  # for gaining weapons without going near them
        self.owner = target
        self.rect = self.rect.move(999, 999)
        self.owner.refreshItem(self.name)

    def activate(self):
        if self.cooldown == 0:
            self.activated = True
            self.cooldown = self.cooldownMax
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
            self.image = pygame.transform.flip(self.image, True, False)  # flips weapon horizontally
            self.dir = dir


class RangeWeapon(MeleeWeapon):
    def __init__(self, image, p_image, startX, startY, damage, name, p_name, CDMax):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()  # transparent image
        self.damage = 0
        self.p_image = p_image  # projectile pic
        self.p_name = p_name  # name of projectile e.g. "arrow"
        self.p_damage = damage  # impact of projectile
        self.projectile = Projectile(p_image, startX, startY, damage, p_name)  # projectile does its own stuff
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.startX = startX
        self.startY = startY
        self.owner = None
        self.dmg = damage
        self.timer = 0  # counts five times
        self.cooldown = 0  # counts eight times starting at same time as timer
        self.activated = False
        self.name = name
        self.dir = 'R'  # direction (L, R)
        self.p_array = []  # set of projectiles
        self.cooldownMax = CDMax
        pygame.sprite.Sprite.__init__(self, all_weapons)
        
    def updateLocation(self):  # Only used when it has an owner and is activated
        if self.owner is not None:
            if self.activated:
                self.rect = self.rect.move(-1 * self.rect.x, -1 * self.rect.y)
                if self.owner.direction == 'R':
                    self.rect = self.rect.move(self.owner.rect.right, self.owner.rect.centery - (self.rect.height / 2))
                    if self.timer > 4:
                        p = Projectile(self.p_image, self.rect.x, self.rect.centery - (self.p_image.get_rect().height / 2), self.p_damage, self.p_name)
                        p.setDirection(self.dir)
                        self.p_array.append(p)
                else:
                    self.rect = self.rect.move(self.owner.rect.left - self.rect.width, self.owner.rect.centery - (self.rect.height / 2))
                    if self.timer > 4:
                        p = Projectile(self.p_image, self.rect.x, self.rect.centery - (self.p_image.get_rect().height / 2), self.p_damage, self.p_name)
                        p.setDirection(self.dir)
                        self.p_array.append(p)
            if self.owner.item != self.name:
                self.owner = None
                self.timer = 0
                self.cooldown = 0
                self.activated = False
                self.rect = self.rect.move(-1 * self.rect.x, -1 * self.rect.y)
                self.rect = self.rect.move(self.startX, self.startY)
        for i in range(len(self.p_array)):
            self.p_array[i].updateLocation()
            
    def tickTimer(self):
        if self.owner is not None:
            if self.cooldown > 0:
                self.cooldown -= 1
            if self.timer > 0:
                self.timer -= 1
            if self.timer == 0 and self.activated:
                self.activated = False
                if self.rect.x < 700:
                    self.rect = self.rect.move(999, 999)


class Projectile(MeleeWeapon):
    def updateLocation(self):  # moves
        if self.dir == 'R':
            self.rect = self.rect.move(5, 0)
        else:
            self.rect = self.rect.move(-5, 0)
        pygame.sprite.Sprite.__init__(self, all_projs)

    def contactPlayer(self, target):
        if self.rect.bottom > target.rect.top and self.rect.top < target.rect.bottom and self.rect.right > target.rect.left and self.rect.left < target.rect.right and self.owner is None:
            target.setHP(target.HP - self.dmg)
            self.rect = self.rect.move(999, 999)
