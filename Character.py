'''
Created on Aug 17, 2014

@author: Akiva and Dan(made this comment)
'''
import pygame, sys
from pygame.locals import *


class Character(pygame.sprite.Sprite):
    '''
    classdocs test
    '''


    def __init__(self, image, startX, startY):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()  # transparent image
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.speedX = 0
        self.speedY = 0
        self.land = False  # true if on a platform
        self.platformCheck = False  # used during checkOnPlatform method
        #self.direction = direction  # direction (N, S, E, W)
        
    def move(self, speed, direction):  # changes speed on key press / Call after key event is handled
        if direction == "up" and self.land == True:
            self.speedY = -1 * speed
            self.land = False
        elif direction == "right":
            self.speedX = speed
        elif direction == "left":
            self.speedX = -1 * speed
        elif direction == "horizontal stop":  # down key not needed for anything / added in case necessary
            self.speedX = 0

    def checkCollision(self, target):
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

    def checkOnPlatform(self, target):  # Checks if walked off an edge / Only call on all blocks at once / Set self.platformCheck to False before call
        if (self.rect.bottom > target.rect.top or self.rect.bottom < target.rect.top) or (self.rect.left > target.rect.right or self.rect.right < target.rect.left):
            pass
        else:
            self.platformCheck = True  # if after checking all blocks, platformCheck is still False, set land to False

    def updateSpeed(self, keyPressed):  # Causes gravitational acceleration / Causes air resistance or friction (less when not on the ground) / ADD COUNTERS TO SLOW DOWN IF TOO FAST
        if self.land == False:  #Gravity
            self.speedY += 1
        if self.speedX != 0 and keyPressed[K_LEFT] == False and keyPressed[K_RIGHT] == False:  # Air Resistance when not choosing a direction
            if self.land == True:  # If on the ground
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
        if keyPressed[K_RIGHT] == True:              # Movement Tests
            if self.land == True:
                self.move(5, "right")
            elif self.speedX <= 0:
                self.move(3, "right")
        elif keyPressed[K_LEFT] == True:
            if self.land == True:
                self.move(5, "left")
            elif self.speedX >= 0:
                self.move(3, "left")
        if keyPressed[K_UP] == True:
            self.move(10, "up")
        if self.platformCheck == False and self.speedY == 0:
            self.move(0, "up")

    def updateLocation(self):  # Handles the movement simply / Call LAST
        self.rect = self.rect.move(self.speedX, self.speedY)
