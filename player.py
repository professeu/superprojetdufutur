import pygame
from entity import Entity


class Player(Entity):
    def __init__(self, x, y):

        super().__init__(x, y)

        self.sprite_sheet = pygame.image.load('images/player3.png')
        self.imagesize = 64
        self.image = self.get_image(0, 0, self.imagesize)
        self.image.set_colorkey([0, 0, 0])

        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(x, y - (self.imagesize / 2), self.imagesize, self.imagesize / 2)

        self.images = {
            'front': self.get_image(0, 0, self.imagesize),
            'back': self.get_image(0, 64, self.imagesize),
            'left_side': self.get_image(0, 192, self.imagesize),
            'right_side': self.get_image(0, 128, self.imagesize)
        }
        self.speed = 3

    def moving_player(self):

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.move_u()

        if pressed[pygame.K_DOWN]:
            self.move_d()

        if pressed[pygame.K_RIGHT]:
            self.move_r()

        if pressed[pygame.K_LEFT]:
            self.move_l()
