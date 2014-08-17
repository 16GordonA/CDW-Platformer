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
        self.onLand = False
        #self.direction = direction  # direction (N, S, E, W)
        
    def move(self, speed, direction):  # changes speed on key press
        if direction == "up" and self.land == True:
            self.speedY = -1 * speed
            self.land = False
        elif direction == "right":
            self.speedX = speed
        elif direction == "left":
            self.speedX = -1 * speed
        elif direction == "horizontal stop":  # down key not needed for anything
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
