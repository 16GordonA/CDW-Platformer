import pygame, sys, random
from pygame.locals import *


all_weapons = pygame.sprite.Group()
all_projs = pygame.sprite.Group()


class MeleeWeapon(pygame.sprite.Sprite):
    def __init__(self, image, startX, startY, damage, name, speed, plats):
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
        self.speed = speed
        self.all_plats = plats
        self.speedy = -12
        self.land = False
        self.boomed = False
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
            if self.owner is not None and self.owner is not target: #melee damage does not work
                print "hyah"
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
                self.activated = False 
                if self.rect.x < 700:
                    self.rect = self.rect.move(999, 999)
    
    def setDirection(self, dir):
        if self.dir == dir:
            pass
        else:
            self.image = pygame.transform.flip(self.image, True, False)  # flips weapon horizontally
            self.dir = dir


class RangeWeapon(MeleeWeapon):
    def __init__(self, image, p_image, startX, startY, damage, name, p_name, CDMax, spread, pcount, pspeed, plats, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()  # transparent image
        self.damage = 0
        self.p_image = p_image  # projectile pic
        self.p_name = p_name  # name of projectile e.g. "arrow"
        self.p_damage = damage  # impact of projectile
        #self.projectile = Projectile(p_image, startX, startY, damage, p_name, pspeed)  # projectile does its own stuff
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
        self.spread = spread
        self.p_count = pcount
        self.pspeed = pspeed
        self.all_plats = plats
        self.type = type
        pygame.sprite.Sprite.__init__(self, all_weapons)
        
    def updateLocation(self):  # Only used when it has an owner and is activated
        if self.owner is not None:
            if self.activated:
                self.rect = self.rect.move(-1 * self.rect.x, -1 * self.rect.y)
                if self.owner.direction == 'R':
                    self.rect = self.rect.move(self.owner.rect.right, self.owner.rect.centery - (self.rect.height / 2))
                    if self.timer > 4 and self.type == 'P':
                        for i in range(self.p_count):
                            p = Projectile(self.p_image, self.rect.x, self.rect.centery - (self.p_image.get_rect().height / 2 + random.randint(-self.spread, self.spread)), self.p_damage, self.p_name, self.pspeed, self.all_plats)
                            p.setDirection(self.dir)
                            self.p_array.append(p)
                    elif self.timer > 4 and self.type == 'E':
                        for i in range(self.p_count):
                            p = ExplosiveP(self.p_image, self.rect.x, self.rect.centery - (self.p_image.get_rect().height / 2 + random.randint(-self.spread, self.spread)), self.p_damage, self.p_name, self.pspeed, self.all_plats) 
                            p.setDirection(self.dir)
                            self.p_array.append(p)
                else:
                    self.rect = self.rect.move(self.owner.rect.left - self.rect.width, self.owner.rect.centery - (self.rect.height / 2))
                    if self.timer > 4 and self.type == 'P':
                        for i in range(self.p_count):
                            p = Projectile(self.p_image, self.rect.x, self.rect.centery - (self.p_image.get_rect().height / 2 + random.randint(-self.spread, self.spread)), self.p_damage, self.p_name, self.pspeed, self.all_plats)
                            p.setDirection(self.dir)
                            self.p_array.append(p)
                    if self.timer > 4 and self.type == 'E':
                        for i in range(self.p_count):
                            p = ExplosiveP(self.p_image, self.rect.x, self.rect.centery - (self.p_image.get_rect().height / 2 + random.randint(-self.spread, self.spread)), self.p_damage, self.p_name, self.pspeed, self.all_plats)
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


class ThrowWeapon(RangeWeapon):
    def updateLocation(self):  # Only used when it has an owner and is activated
        if self.owner is not None:
            if self.activated:
                self.rect = self.rect.move(-1 * self.rect.x, -1 * self.rect.y)
                if self.owner.direction == 'R':
                    self.rect = self.rect.move(self.owner.rect.right, self.owner.rect.centery - (self.rect.height / 2))
                    if self.timer > 4:
                        for i in range(self.p_count):
                            p = Throwable(self.p_image, self.rect.x, self.rect.centery - (self.p_image.get_rect().height / 2 + random.randint(-self.spread, self.spread)), self.p_damage, self.p_name, self.pspeed, self.all_plats)
                            p.setDirection(self.dir)
                            self.p_array.append(p)
                else:
                    self.rect = self.rect.move(self.owner.rect.left - self.rect.width, self.owner.rect.centery - (self.rect.height / 2))
                    if self.timer > 4:
                        for i in range(self.p_count):
                            p = Throwable(self.p_image, self.rect.x, self.rect.centery - (self.p_image.get_rect().height / 2 + random.randint(-self.spread, self.spread)), self.p_damage, self.p_name, self.pspeed, self.all_plats)
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

class Projectile(MeleeWeapon):
    def updateLocation(self):  # moves
        if self.dir == 'R':
            self.rect = self.rect.move(self.speed, 0)
        elif self.dir == 'UR' or self.dir == 'RU':
            self.rect = self.rect.move(self.speed, -self.speed)
        elif self.dir == 'U':
            self.rect = self.rect.move(0, -self.speed)
        elif self.dir == 'LU' or self.dir == 'UL':
            self.rect = self.rect.move(-self.speed, -self.speed)
        elif self.dir == 'L':
            self.rect = self.rect.move(-self.speed, 0)
        elif self.dir == 'LD' or self.dir == 'DL':
            self.rect = self.rect.move(-self.speed, self.speed)
        elif self.dir == 'D':
            self.rect = self.rect.move(0, self.speed)
        elif self.dir == 'DR' or self.dir == 'RD':
            self.rect = self.rect.move(self.speed, self.speed)
        else:
            self.rect = self.rect.move(0, 0)
        if self.rect.left > 700 or self.rect.right < -100:
            self.name = "gone"
        
            all_projs.remove(self)
            all_weapons.remove(self)
 

    def contactPlayer(self, target):
        if self.rect.bottom > target.rect.top and self.rect.top < target.rect.bottom and self.rect.right > target.rect.left and self.rect.left < target.rect.right and self.owner is None:
            target.setHP(target.HP + self.dmg)
            if self.dir == 'R' or self.dir == 'UR' or self.dir == 'RU' or self.dir == 'RD' or self.dir == 'DR':
                target.rect = target.rect.move(int(self.dmg),0)
            elif self.dir.find('L') >= 0:
                target.rect = target.rect.move(-int(self.dmg), 0)
            self.rect = self.rect.move(999, 999)

class Throwable(Projectile):
    def updateLocation(self):  # moves
        self.update()
        if self.land:
            if self.speed > 0:
                self.speed = self.speed - 1
            self.speedy = 0
        else:
            self.speedy = self.speedy + 1
        if self.dir == 'R':
            self.rect = self.rect.move(self.speed, self.speedy)
        else:
            self.rect = self.rect.move(-self.speed, self.speedy)
        if self.rect.left > 700 or self.rect.right < -100:
            if self.dir == 'R':
                self.rect = self.rect.move(-self.speed, 0) #moves backwards so net movement = 0
                self.name = "gone"
            elif self.dir == 'L':
                self.rect = self.rect.move(self.speed, 0)
                self.name = "gone"
        
            all_projs.remove(self)
            all_weapons.remove(self)
        if self.speed == 0 and self.speedy == 0:
            self.boom()
    
    def update(self):
        self.land = False
        for p in self.all_plats:
            self.checkCollision(p)
            self.platformCheck = False
            self.checkOnPlatform(p)
            if self.platformCheck:
                self.land = True
        
    def checkCollision(self, target):
        if self.speedy > 0:  # if going down
            if self.rect.bottom < target.rect.top and self.rect.bottom + self.speedy + 1 > target.rect.top and self.rect.right > target.rect.left and self.rect.left < target.rect.right:
                self.speedy = target.rect.top - self.rect.bottom - 1
            elif self.rect.bottom == target.rect.top and self.rect.right > target.rect.left and self.rect.left < target.rect.right:
                self.land = True
                self.speedy = 0
        if self.speedy < 0:  # if going up
            if self.rect.top > target.rect.bottom and self.rect.top + self.speedy - 1 < target.rect.bottom and self.rect.right > target.rect.left and self.rect.left < target.rect.right:
                self.speedy = target.rect.bottom - self.rect.top
            elif self.rect.top == target.rect.bottom and self.rect.right > target.rect.left and self.rect.left < target.rect.right:
                self.speedy = 1
        if self.dir == 'R':  # if going right
            if self.rect.bottom > target.rect.top and self.rect.top < self.rect.bottom and self.rect.right + self.speed > target.rect.left and self.rect.right < target.rect.left:
                self.speed = target.rect.left - self.rect.right
        if self.dir == 'L':  # if going left
            if self.rect.bottom > target.rect.top and self.rect.top < self.rect.bottom and self.rect.left + self.speed < target.rect.right and self.rect.left > target.rect.right:
                self.speed = target.rect.right - self.rect.left
        if (self.rect.right == target.rect.left and self.rect.top < target.rect.bottom and self.rect.bottom > target.rect.top):
            self.dir = 'L'
        if (self.rect.left == target.rect.right and self.rect.top < target.rect.bottom and self.rect.bottom > target.rect.top):
            self.dir = 'R'
            
    def checkOnPlatform(self, target):  # Checks if walked off an edge / Only call on all blocks at once / Set self.platformCheck to False before call
        if (self.rect.bottom > target.rect.top or self.rect.bottom < target.rect.top) or (self.rect.left > target.rect.right or self.rect.right < target.rect.left):
            pass
        else:
            self.platformCheck = True  # if after checking all blocks, platformCheck is still False, set land to False
        return True
    
    def boom(self):
        self.rect = self.rect.move(0,0)

class ExplodeWeapon(ThrowWeapon):
    
    def updateLocation(self):  # Only used when it has an owner and is activated
        if self.owner is not None:
            if self.activated:
                self.rect = self.rect.move(-1 * self.rect.x, -1 * self.rect.y)
                if self.owner.direction == 'R':
                    self.rect = self.rect.move(self.owner.rect.right, self.owner.rect.centery - (self.rect.height / 2))
                    if self.timer > 4:
                        for i in range(self.p_count):
                            p = Explosive(self.p_image, self.rect.x, self.rect.centery - (self.p_image.get_rect().height / 2 + random.randint(-self.spread, self.spread)), self.p_damage, self.p_name, self.pspeed, self.all_plats)
                            p.setDirection(self.dir)
                            self.p_array.append(p)
                else:
                    self.rect = self.rect.move(self.owner.rect.left - self.rect.width, self.owner.rect.centery - (self.rect.height / 2))
                    if self.timer > 4:
                        for i in range(self.p_count):
                            p = Explosive(self.p_image, self.rect.x, self.rect.centery - (self.p_image.get_rect().height / 2 + random.randint(-self.spread, self.spread)), self.p_damage, self.p_name, self.pspeed, self.all_plats)
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
            
class Explosive(Throwable):
    def contactPlayer(self, target):
        if self.rect.bottom > target.rect.top and self.rect.top < target.rect.bottom and self.rect.right > target.rect.left and self.rect.left < target.rect.right and self.owner is None:
            self.boom()
    
    def boom(self):
        if self.boomed == False:
            self.boomed = True
            frag = pygame.image.load('Weapon Pics/frag.png')
            dirs = ['U','UL','L','DL','D','RD','R','UR']
            for dir in dirs:
                p = Projectile(frag, self.rect.centerx - frag.get_rect().width/2, self.rect.centery - frag.get_rect().height/2, 3, 'shrapnel', 8, self.all_plats)
                p.setDirection(dir)
            all_projs.remove(self)
            all_weapons.remove(self)
class ExplosiveP(Explosive):
    def contactPlayer(self, target):
        if self.rect.bottom > target.rect.top and self.rect.top < target.rect.bottom and ((self.rect.right > target.rect.left and self.rect.right < target.rect.right) or (self.rect.left < target.rect.right and self.rect.left > target.rect.left)) and self.owner is None:
            target.setHP(target.HP + self.dmg)
            self.boom()
            
    def updateLocation(self):  # moves
        if self.dir == 'R':
            self.rect = self.rect.move(self.speed, 0)
        elif self.dir == 'UR' or self.dir == 'RU':
            self.rect = self.rect.move(self.speed, -self.speed)
        elif self.dir == 'U':
            self.rect = self.rect.move(0, -self.speed)
        elif self.dir == 'LU' or self.dir == 'UL':
            self.rect = self.rect.move(-self.speed, -self.speed)
        elif self.dir == 'L':
            self.rect = self.rect.move(-self.speed, 0)
        elif self.dir == 'LD' or self.dir == 'DL':
            self.rect = self.rect.move(-self.speed, self.speed)
        elif self.dir == 'D':
            self.rect = self.rect.move(0, self.speed)
        elif self.dir == 'DR' or self.dir == 'RD':
            self.rect = self.rect.move(self.speed, self.speed)
        else:
            self.rect = self.rect.move(0, 0)
        if self.rect.left > 700 or self.rect.right < -100:
            self.name = "gone"
        
            all_projs.remove(self)
            all_weapons.remove(self)