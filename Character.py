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
        #self.direction = direction  # direction (N, S, E, W)
        
    def moveLR(self, direction): #controls movement side to side
          for i in range(10): #needs to be updated for pixel sizes
            if (self.canMove()):
                #test for determining if runs off platform?
                self.rect = self.rect.move(1)
                pygame.time.delay(5)
