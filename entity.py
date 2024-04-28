import pygame


class Entity(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.sprite_sheet = pygame.image.load('images/player3.png')
        self.imagesize = 64
        self.image = self.get_image(0, 0, self.imagesize)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            'front': self.get_image(0, 0, self.imagesize),
            'back': self.get_image(0, 16, self.imagesize),
            'left_side': self.get_image(16, 0, self.imagesize),
            'right_side': self.get_image(16, 16, self.imagesize)
        }
        self.speed = 1
        # cest arbitraire

    def move_r(self):
        self.position[0] += self.speed
        self.image = self.images['right_side']

    def move_l(self):
        self.position[0] -= self.speed
        self.image = self.images['left_side']

    def move_d(self):
        self.position[1] += self.speed
        self.image = self.images['front']

    def move_u(self):
        self.position[1] -= self.speed
        self.image = self.images['back']

    def update(self):
        self.rect.topleft = self.position

    def get_image(self, x, y, size):
        image = pygame.Surface([size, size])
        image.blit(self.sprite_sheet, (0, 0), (x, y, size, size))

        return image
