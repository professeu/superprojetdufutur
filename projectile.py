import pygame
from entity import Entity


class Projectile(Entity):

    def __init__(self, player):
        super().__init__(player.position[0], player.position[1])

        self.direction = player.direction
        self.positions = {
            'front': [player.position[0] + player.imagesize[0]/4, player.position[1] + player.imagesize[1]/2],
            'back': [player.position[0] + player.imagesize[0]/4, player.position[1]],
            'right_side': [player.position[0] + player.imagesize[0]/2, player.position[1] + player.imagesize[1]/4],
            'left_side':  [player.position[0], player.position[1] + player.imagesize[1]/4]
        }
        self.position = self.positions[self.direction]

        self.imagesize = (32, 32)
        self.sprite_sheet = pygame.image.load('images/fireball.png')
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, self.imagesize)
        self.images = {
            'front': pygame.transform.rotate(self.sprite_sheet, 90),
            'back': pygame.transform.rotate(self.sprite_sheet, 270),
            'right_side': pygame.transform.rotate(self.sprite_sheet, 180),
            'left_side': self.sprite_sheet
        }
        self.sprite_sheet = self.images[self.direction]

        self.image = self.get_image(0, 0)

        self.image.set_colorkey([0, 0, 0])

        self.speed = 1
        self.time = pygame.time.get_ticks()
        self.cooldown = 10

        self.strength = 2

        self.alive = True

    def moving(self):

        if pygame.time.get_ticks() - self.time > self.cooldown:
            self.time = pygame.time.get_ticks()
            if self.direction == 'front':
                self.move_d()
            elif self.direction == 'back':
                self.move_u()
            elif self.direction == 'right_side':
                self.move_r()
            elif self.direction == 'left_side':
                self.move_l()

    def update(self):
        self.image.set_colorkey((0, 0, 0))
        self.collision_do()
        self.moving()


    def attack(self, enemy):
        if self.rect.colliderect(enemy.rect):
            enemy.damage(self.strength)
            self.alive = False

    def collision_do(self):
        if self.collision_test(self.collision.walls):
            self.alive = False
