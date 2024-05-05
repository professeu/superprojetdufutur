import pygame
from collision import Collision


class Entity(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.sprite_sheet = pygame.image.load('images/player3.png')
        self.imagesize = 64
        self.image = self.get_image(0, 0, self.imagesize)
        self.image.set_colorkey([0, 0, 0])

        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(x, y + (self.imagesize/2), self.imagesize, self.imagesize/2)

        self.collision = Collision()

        self.position = [x, y]
        self.old_position = self.position.copy()

        self.images = {
            'front': self.get_image(0, 0, self.imagesize),
            'back': self.get_image(0, 16, self.imagesize),
            'left_side': self.get_image(16, 0, self.imagesize),
            'right_side': self.get_image(16, 16, self.imagesize)
        }

        self.speed = 1

    def collision_test(self, t):
        if self.feet.collidelist(t) >-1:
            return True

    def move_r(self):

        self.position[0] += self.speed
        self.image = self.images['right_side']
        self.update_rect()

    def move_l(self):

        self.position[0] -= self.speed
        self.image = self.images['left_side']
        self.update_rect()

    def move_d(self):

        self.position[1] += self.speed
        self.image = self.images['front']
        self.update_rect()

    def move_u(self):

        self.position[1] -= self.speed
        self.image = self.images['back']
        self.update_rect()

    def save_position(self):
        self.old_position = self.position.copy()

    def update_rect(self):
        self.rect = pygame.Rect(self.position[0], self.position[1], self.imagesize, self.imagesize)
        self.feet = pygame.Rect(self.position[0], self.position[1] + (self.imagesize/2), self.imagesize, self.imagesize/2)

    def move_back(self):
        self.position = self.old_position.copy()
        self.update_rect()

    def collision_do(self):
        if self.collision_test(self.collision.walls):
            self.move_back()

    def get_image(self, x, y, size):
        image = pygame.Surface([size, size])
        image.blit(self.sprite_sheet, (0, 0), (x, y, size, size))

        return image
