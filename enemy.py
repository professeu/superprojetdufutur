import pygame
from entity import Entity


class Enemy(Entity):
    def __init__(self, x, y):

        super().__init__(x, y)

        self.sprite_sheet = pygame.image.load('images/player3.png')
        self.image = self.get_image(0, 0, self.imagesize)
        self.image.set_colorkey([0, 0, 0])

        # self.rect = self.image.get_rect()
        # self.feet = pygame.Rect(x, y - (self.imagesize / 2), self.imagesize, self.imagesize / 2)

        self.images = {
            'front': self.get_image(0, 0, self.imagesize),
            'back': self.get_image(0, 64, self.imagesize),
            'left_side': self.get_image(0, 192, self.imagesize),
            'right_side': self.get_image(0, 128, self.imagesize)
        }
        self.speed = 1
        # cest arbitraire

    # méthode du déplacement de l'ennemi

    def move_enemy_towards_player(self, player):
        # calcul de vecteurs déplacement en x et en y

        dx = int(player.position[0] - self.position[0])
        dy = int(player.position[1] - self.position[1])

        if dx < 0:
            self.move_l()
        if dx > 0:
            self.move_r()
        if dy < 0:
            self.move_u()
        if dy > 0:
            self.move_d()