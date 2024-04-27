import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('player2.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            'down' : self.get_image(0, 0),
            'left' : self.get_image(0, 64),
            'right' : self.get_image(0, 128),
            'up' : self.get_image(0, 192)
        }
        self.speed = 3

    def move_r(self):
        self.position[0] += self.speed
        self.image = self.images['right']

    def move_l(self):
        self.position[0] -= self.speed
        self.image = self.images['left']

    def move_u(self):
        self.position[1] -= self.speed
        self.image = self.images['up']

    def move_d(self):
        self.position[1] += self.speed
        self.image = self.images['down']



    def update(self):
        self.rect.topleft = self.position

    def get_image(self, x, y):
        image = pygame.Surface([49, 64])
        image.blit(self.sprite_sheet, (0,0), (x, y, 49, 64))
        return image


