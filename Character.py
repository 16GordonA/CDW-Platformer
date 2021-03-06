import pygame, sys
from pygame.locals import *
all_chars = pygame.sprite.Group()


class Character(pygame.sprite.Sprite):
    def __init__(self, image, fimage, startX, startY, lives, name):
        pygame.sprite.Sprite.__init__(self)
        self.nimage = image.convert_alpha()  # transparent image
        self.flicker = fimage
        self.image = self.nimage
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.speedX = 0
        self.speedY = 0
        self.land = False  # true if on a platform
        self.platformCheck = False  # used during checkOnPlatform method
        self.item = None
        self.direction = 'R'  # direction (L,R)
        self.alive = True
        self.lives = lives
        self.HP = 0
        self.time = 0
        self.name = name
        pygame.sprite.Sprite.__init__(self, all_chars)

    def setHP(self, hp):
        if(self.time > 60):
            self.HP = hp
        if(self.HP >= 100) or self.alive == False:
            self.HP = 0
            if self.lives > 1:
                self.alive = True
                self.lives -= 1
                self.HP = 0
                self.item = None
                self.rect = self.rect.move(285-self.rect.left, 390 - self.rect.top)
                self.time = 0
            else:
                self.lives = 0
                self.alive = False
                poof = pygame.image.load('Images/Poof.png')
                self.image = poof.convert_alpha()
                
            self.speedX = 0
            self.speedY = 0

    def update(self, keyPressed, all_plats):
        self.updateSpeed(keyPressed)
        if(self.time < 60 and self.time%15 > 7):
            self.image = self.flicker
        elif self.alive:
            self.image = self.nimage
        for p in all_plats:
            self.checkCollision(p)
            self.platformCheck = False
            self.checkOnPlatform(p)
            if self.platformCheck:
                self.land = True
        self.updateLocation()
        self.updateItem(keyPressed)
        self.time = self.time + 1

    #probably something else should go in here too about removing sprite from game or changing image
    def move(self, speed, direction):  # changes speed on key press / Call after key event is handled
        if self.alive:
            if direction == "up" and self.land:
                self.speedY = -1 * speed
                self.land = False
            elif direction == "right":
                self.speedX = speed
                self.direction = 'R'
            elif direction == "left":
                self.speedX = -1 * speed
                self.direction = 'L'
            elif direction == "horizontal stop":  # down key not needed for anything / added in case necessary
                self.speedX = 0

    def checkCollision(self, target):
        if self.alive:
            if self.speedY > 0:  # if going down
                if self.rect.bottom < target.rect.top and self.rect.bottom + self.speedY + 1 > target.rect.top and self.rect.right > target.rect.left and self.rect.left < target.rect.right:
                    self.speedY = target.rect.top - self.rect.bottom
                elif self.rect.bottom == target.rect.top and self.rect.right > target.rect.left and self.rect.left < target.rect.right:
                    self.land = True
                    self.speedY = 0
            if self.speedY < 0:  # if going up
                if self.rect.top > target.rect.bottom and self.rect.top + self.speedY - 1 < target.rect.bottom and self.rect.right > target.rect.left and self.rect.left < target.rect.right:
                    self.speedY = target.rect.bottom - self.rect.top
                elif self.rect.top == target.rect.bottom and self.rect.right > target.rect.left and self.rect.left < target.rect.right:
                    self.speedY = 1
            if self.speedX > 0:  # if going right
                if self.rect.bottom > target.rect.top and self.rect.top < self.rect.bottom and self.rect.right + self.speedX > target.rect.left and self.rect.right < target.rect.left:
                    self.speedX = target.rect.left - self.rect.right
            if self.speedX < 0:  # if going left
                if self.rect.bottom > target.rect.top and self.rect.top < self.rect.bottom and self.rect.left + self.speedX < target.rect.right and self.rect.left > target.rect.right:
                    self.speedX = target.rect.right - self.rect.left
            if (self.rect.right == target.rect.left and self.rect.top < target.rect.bottom and self.rect.bottom > target.rect.top):
                self.speedX = -1
            if (self.rect.left == target.rect.right and self.rect.top < target.rect.bottom and self.rect.bottom > target.rect.top):
                self.speedX = 1

    def checkOnPlatform(self, target):  # Checks if walked off an edge / Only call on all blocks at once / Set self.platformCheck to False before call
        if self.alive:
            if (self.rect.bottom > target.rect.top or self.rect.bottom < target.rect.top) or (self.rect.left > target.rect.right or self.rect.right < target.rect.left):
                pass
            else:
                self.platformCheck = True  # if after checking all blocks, platformCheck is still False, set land to False
            return True

    def updateSpeed(self, keyPressed):  # Causes gravitational acceleration / Causes air resistance or friction (less when not on the ground) / ADD COUNTERS TO SLOW DOWN IF TOO FAST
        if self.alive:
            if not self.land:  # Gravity
                self.speedY += 1
            if self.speedX != 0 and not keyPressed[K_LEFT] and not keyPressed[K_RIGHT]:  # Air Resistance when not choosing a direction
                if self.land:  # If on the ground
                    if self.speedX > 0:  # If going right originally
                        self.speedX /= 2
                    else:  # If going left originally
                        self.speedX /= 2
                        self.speedX += 1
                else:  # If in the air
                    if self.speedX > 0:  # If going right originally
                        self.speedX = 3 * self.speedX / 4
                    else:  # If going left originally
                        self.speedX /= 3 * self.speedX / 4
                        self.speedX += 1
            if keyPressed[K_RIGHT]:  # Movement Tests
                self.move(5, "right")
            elif keyPressed[K_LEFT]:
                self.move(5, "left")
            if keyPressed[K_UP]:
                self.move(12, "up")
            if not self.platformCheck and self.speedY == 0:
                self.move(0, "up")

    def updateLocation(self):  # Handles the movement simply / Call LAST
        self.rect = self.rect.move(self.speedX, self.speedY)
        if self.rect.top > 500:
            self.alive = False
            self.setHP(999)

    def updateItem(self, keyPressed):
        pass

    def refreshItem(self, nm):
        self.item = nm
        
class Player2(Character):
    def updateSpeed(self, keyPressed):  # Causes gravitational acceleration / Causes air resistance or friction (less when not on the ground) / ADD COUNTERS TO SLOW DOWN IF TOO FAST
        if self.alive:
            if not self.land:  # Gravity
                self.speedY += 1
            if self.speedX != 0 and not keyPressed[K_a] and not keyPressed[K_d]:  # Air Resistance when not choosing a direction
                if self.land:  # If on the ground
                    if self.speedX > 0:  # If going right originally
                        self.speedX /= 2
                    else:  # If going left originally
                        self.speedX /= 2
                        self.speedX += 1
                else:  # If in the air
                    if self.speedX > 0:  # If going right originally
                        self.speedX = 3 * self.speedX / 4
                    else:  # If going left originally
                        self.speedX /= 3 * self.speedX / 4
                        self.speedX += 1
            if keyPressed[K_d]:  # Movement Tests
                self.move(5, "right")
            elif keyPressed[K_a]:
                self.move(5, "left")
            if keyPressed[K_w]:
                self.move(12, "up")
            if not self.platformCheck and self.speedY == 0:
                self.move(0, "up")
                
class ThirdPlayer(Character):
    def updateSpeed(self, keyPressed):  # Causes gravitational acceleration / Causes air resistance or friction (less when not on the ground) / ADD COUNTERS TO SLOW DOWN IF TOO FAST
        if self.alive:
            if not self.land:  # Gravity
                self.speedY += 1
            if self.speedX != 0 and not keyPressed[K_h] and not keyPressed[K_k]:  # Air Resistance when not choosing a direction
                if self.land:  # If on the ground
                    if self.speedX > 0:  # If going right originally
                        self.speedX /= 2
                    else:  # If going left originally
                        self.speedX /= 2
                        self.speedX += 1
                else:  # If in the air
                    if self.speedX > 0:  # If going right originally
                        self.speedX = 3 * self.speedX / 4
                    else:  # If going left originally
                        self.speedX /= 3 * self.speedX / 4
                        self.speedX += 1
            if keyPressed[K_k]:  # Movement Tests
                self.move(5, "right")
            elif keyPressed[K_h]:
                self.move(5, "left")
            if keyPressed[K_u]:
                self.move(12, "up")
            if not self.platformCheck and self.speedY == 0:
                self.move(0, "up")
