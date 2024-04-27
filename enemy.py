import pygame

# sous classe qui herite des caractéristiques de la classe pygame qui fait des sprites
class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        #super(). appelle les caractéristiques de l'__init__ de la classe parente
        super().__init__()
        #ennemy.png est un tilest, on utilisera ensuite les différentes images
        self.sprite_sheet = pygame.image.load('ennemy2.png')
        self.image = self.get_image(0, 0)
        #self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            'front': self.get_image(0, 0),
            'back': self.get_image(0, 68),
            'left_side': self.get_image(0, 136),
            'right_side': self.get_image(0, 204)
        }
        self.speed = 1 # cest arbitraire

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

    def get_image(self, x, y):
        image = pygame.Surface([46, 68])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 46, 68))
        return image
