import pygame


class Entity(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.sprite_sheet = pygame.image.load('./images/player3.png')
        self.imagesize = [64, 64]
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.direction = 'front'

        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(x, y + (self.imagesize[1]/2), self.imagesize[0], self.imagesize[1]/2)

        self.position = [x, y]
        self.old_position = self.position.copy()

        self.images = {
            'front': self.get_image(0, 0),
            'back': self.get_image(0, 64),
            'left_side': self.get_image(0, 192),
            'right_side': self.get_image(0, 128)
        }

        self.attack_images = {
            'front': self.get_image(256, 0),
            'back': self.get_image(256, 64),
            'left_side': self.get_image(256, 192),
            'right_side': self.get_image(256, 128)
        }

        self.image_dictionnary = self.images

        self.speed = 1
        self.health_max = 20
        self.health = self.health_max
        self.attack_time = pygame.time.get_ticks()
        self.attack_cooldown = 500

    def move_r(self):
        self.position[0] += self.speed
        self.direction = 'right_side'
        self.update_rect()

    def move_l(self):
        self.position[0] -= self.speed
        self.direction = 'left_side'
        self.update_rect()

    def move_d(self):
        self.position[1] += self.speed
        self.direction = 'front'
        self.update_rect()

    def move_u(self):
        self.position[1] -= self.speed
        self.direction = 'back'
        self.update_rect()

    def update_rect(self):
        self.rect = pygame.Rect(self.position[0], self.position[1], self.imagesize[0], self.imagesize[1])
        self.feet = pygame.Rect(self.position[0], self.position[1] + (self.imagesize[1]/2), self.imagesize[0], self.imagesize[1]/2)

    def save_position(self):
        self.old_position = self.position.copy()

    def move_back(self):
        self.position = self.old_position.copy()
        self.update_rect()

    def collision_test(self, t):
        if self.feet.collidelist(t) > -1:
            return True

    def collision_do(self, t):
        if self.collision_test(t):
            self.move_back()

    def get_image(self, x, y):
        image = pygame.Surface(self.imagesize)
        image.blit(self.sprite_sheet, (0, 0), (x, y, self.imagesize[0], self.imagesize[1]))

        return image

    def damage(self, amount):
        damages = amount
        if damages < 0:
            damages = 0
        self.health = self.health - damages

    def update_attackcooldown(self): self.attack_time = pygame.time.get_ticks()

    def wich_image(self):
        if pygame.time.get_ticks() - self.attack_time > self.attack_cooldown:
            self.image_dictionnary = self.images
        else:
            self.image_dictionnary = self.attack_images
        self.image = self.image_dictionnary[self.direction]