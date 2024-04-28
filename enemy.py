import pygame
from entity import Entity


class Enemy(Entity):
    def __init__(self, x, y):

        super().__init__(x, y)

        self.sprite_sheet = pygame.image.load('images/player3.png')
        self.image = self.get_image(0, 0, self.imagesize)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.images = {
            'front': self.get_image(0, 0, self.imagesize),
            'back': self.get_image(0, 64, self.imagesize),
            'left_side': self.get_image(0, 192, self.imagesize),
            'right_side': self.get_image(0, 128, self.imagesize)
        }
        self.speed = 1
        # cest arbitraire
