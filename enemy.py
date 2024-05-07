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
        self.vision = 100
        self.attack_mod = False
        self.jauge = pygame.image.load('images/PV_vide.png')
        self.health_max = 20
        self.health = self.health_max

    # méthode du déplacement de l'ennemi

    def moving(self, player):
        # calcul de vecteurs déplacement en x et en y

        dx = int(player.position[0] - self.position[0])
        dy = int(player.position[1] - self.position[1])
        d = (dx**2 + dy**2)**0.5
        if d < self.vision:
            self.attack_mod = True

        if self.attack_mod:
            if dx < 0:
                self.move_l()
            if dx > 0:
                self.move_r()
            if dy < 0:
                self.move_u()
            if dy > 0:
                self.move_d()
            if d < 20:
                self.attack(player)

    def show_health(self):
        if self.attack_mod:
            pygame.draw.rect(self.image, (26, 0, 4), pygame.Rect(17, 10, 30, 4))
            pygame.draw.rect(self.image, "red", pygame.Rect(17, 10, (self.health / self.health_max) * 30, 4))

    def attack(self, player):
        # affichage :
        # action :
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_k]:
            if self.rect.colliderect(player.rect):
                player.health -= 1

    def update(self):
        self.image.set_colorkey([0, 0, 0])
        self.show_health()
        self.update_rect()
        self.save_position()