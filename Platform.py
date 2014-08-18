import pygame, sys

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 450
all_plats = pygame.sprite.Group()


class Platform(pygame.sprite.Sprite):
    def __init__(self, image, x, y):  # x, y refer to location of top left corner of platform
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect().move(x, y)
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
