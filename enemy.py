import pygame
from entity import Entity


class Enemy(Entity):
    def __init__(self, x, y):

        super().__init__(x, y)

        self.speed = 1
        self.vision = 150
        self.shield = 0

        self.fight_mod = False

        self.health_max = 20
        self.health = self.health_max

    # méthode du déplacement de l'ennemi

    def moving(self, player):
        # calcul de vecteurs déplacement en x et en y

        dx = int(player.position[0] - self.position[0])
        dy = int(player.position[1] - self.position[1])
        d = (dx**2 + dy**2)**0.5
        if d < self.vision:
            self.fight_mod = True

        if self.fight_mod:
            if pygame.time.get_ticks() - self.attack_time > self.attack_cooldown:
                if dx < 0:
                    self.move_l()
                if dx > 0:
                    self.move_r()
                if dy < 0:
                    self.move_u()
                if dy > 0:
                    self.move_d()

            if d < 100:
                self.attack(player)

    def show_health(self):
        if self.fight_mod:
            pygame.draw.rect(self.image, (26, 0, 4), pygame.Rect(17, 10, 30, 4))
            pygame.draw.rect(self.image, "red", pygame.Rect(17, 10, (self.health / self.health_max) * 30, 4))

    def attack(self, player):
        # action :
        if self.rect.colliderect(player.rect) and pygame.time.get_ticks() - self.attack_time > self.attack_cooldown:
            self.attack_time = pygame.time.get_ticks()
            self.image_dictionnary = self.attack_images
            player.damage(1)

    def update(self):
        self.wich_image()
        self.image.set_colorkey([0, 0, 0])
        self.show_health()
        self.update_rect()
        self.save_position()