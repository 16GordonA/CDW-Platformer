'''
Created on Aug 18, 2014

@author: Akiva 
'''
import pygame, sys
from pygame.locals import *
from Weapon import *
from Character import *


class Character(pygame.sprite.Sprite):
    def __init__(self, image, startX, startY, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()  # transparent image
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.speedX = 0
        self.speedY = 0
        self.land = False  # true if on a platform
        self.platformCheck = False  # used during checkOnPlatform method
        self.item = None
        self.direction = 'R'  # direction (L,R)
        self.alive = True
        self.HP = 100
    
    def setHP(self, newHP):
        self.HP = newHP
        if(self.HP <= 0):
            self.alive = False
            
    
    def move(self, speed, direction):  # changes speed on key press / Call after key event is handled
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
        if (self.rect.bottom > target.rect.top or self.rect.bottom < target.rect.top) or (self.rect.left > target.rect.right or self.rect.right < target.rect.left):
            pass
        else:
            self.platformCheck = True  # if after checking all blocks, platformCheck is still False, set land to False

    def updateSpeed(self, player): #name saved from Character class, can be changed later
        if not self.land:  # Gravity
            self.speedY += 1
        if self.speedX != 0:  # Air Resistance when not choosing a direction
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
        
        if(player.rect.bottom > enemy.rect.top):
            self.move(10, "up")
        if (player.rect.left > enemy.rect.right):  #player to enemy's right
            self.move(5, "right")
        elif (player.rect.right < enemy.rect.left): #player to enemy's left
            self.move(5, "left")
        if (player.rect.bottom > enemy.rect.top):
            self.move(10, "up")
        if not self.platformCheck and self.speedY == 0:
            self.move(0, "up")
        #gets to same level as player, then walks towards player and attacks

    def updateLocation(self):  # Handles the movement simply / Call LAST
        self.rect = self.rect.move(self.speedX, self.speedY)

    def refreshItem(self, itemName):
        self.Item = itemName
