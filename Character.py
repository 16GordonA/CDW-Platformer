'''
Created on Aug 17, 2014

@author: Akiva and Dan(made this comment)
'''

class Character(pygame.sprite.Sprite):
    '''
    classdocs test
    '''


    def __init__(self, image, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()  # transparent image
        self.rect = self.image.get_rect().move(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # rect is for blitting
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
        if speedY > 0:  # if going down
            if self.rect.bottom < target.rect.top and self.rect.bottom + self.speedY + 1 > target.rect.top and self.rect.right > target.rect.left and self.rect.left < target.rect.right:
                self.speedY = target.rect.top - self.rect.bottom
            elif self.rect.bottom == target.rect.top and self.rect.right > target.rect.left and self.rect.left < target.rect.right:
                self.land = True
                self.speedY = 0
        if speedY < 0:  # if going up
            if self.rect.top > target.rect.bottom and self.rect.top + self.speedY - 1 < target.rect.bottom and self.rect.right > target.rect.left and self.rect.left < target.rect.right:
                self.speedY = target.rect.bottom - self.rect.top
            elif self.rect.top == target.rect.bottom and self.rect.right > target.rect.left and self.rect.left < target.rect.right:
                self.speedY = 1
        if speedX > 0:  # if going right
            if self.rect.bottom > target.rect.top and self.rect.top < self.rect.bottom and self.rect.right + self.speedX > target.rect.left and self.rect.right < target.rect.left:
                self.speedX = 0:
        if speedX < 0:  # if going left
            if self.rect.bottom > target.rect.top and self.rect.top < self.rect.bottom and self.rect.left + self.speedX < target.rect.right and self.rect.left > target.rect.right:

    def checkOnPlatform(self, target):  # Checks if walked off an edge / Only call if land is True and call on all blocks at once / Set self.platformCheck to False before call
        if (self.rect.bottom > target.rect.top or self.rect.bottom < target.rect.top) or (self.rect.left > target.rect.right or self.rect.right < target.rect.left):
            pass
        else:
            self.platformCheck = True  # if after checking all blocks, platformCheck is still False, set land to False

    def updateSpeed(self):  # Causes gravitational acceleration / Causes air resistance or friction (less when not on the ground) / ADD COUNTERS TO SLOW DOWN IF TOO FAST
        if self.land == False:  #Gravity
            self.speedY += 1
        if self.speedX != 0 and key[K_LEFT] == False and key[K_RIGHT] == False:  # Air Resistance when not choosing a direction
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

    def updateLocation(self):  # Handles the movement simply / Call LAST
        self.rect.move(self.speedX, self.speedY)
