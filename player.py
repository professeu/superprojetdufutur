import pygame
from entity import Entity
from projectile import Projectile


class Player(Entity):
    def __init__(self, x, y):

        super().__init__(x, y)

        self.speed = 2

        self.health_max = 30
        self.health = self.health_max
        self.shield = 0

        self.projectiles = []

    def moving_player(self):

        pressed = pygame.key.get_pressed()
        if pygame.time.get_ticks() - self.attack_time > self.attack_cooldown:
            if pressed[pygame.K_z]:
                self.move_u()

            if pressed[pygame.K_s]:
                self.move_d()

            if pressed[pygame.K_d]:
                self.move_r()

            if pressed[pygame.K_q]:
                self.move_l()

    def update(self):
        self.wich_image()
        self.image.set_colorkey([0, 0, 0])
        self.update_rect()
        self.save_position()

        for proj in self.projectiles:
            proj.moving()

    def attack(self, enemy):
        # affichage :
        # action :
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_k] and pygame.time.get_ticks() - self.attack_time > self.attack_cooldown:
            self.attack_time = pygame.time.get_ticks()
            if self.rect.colliderect(enemy.rect):
                enemy.damage(1)

        if pressed[pygame.K_o] and pygame.time.get_ticks() - self.attack_time > self.attack_cooldown:
            self.attack_time = pygame.time.get_ticks()
            self.projectiles.append(Projectile(self))
