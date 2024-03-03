import pygame
# jexplique?

class Enemy(pygame.sprite.Sprite): # cest une sous classe , elle herite des caracteristiques dune classe de pygame qui fait des sprites
    #avec tu ca tu vois on va plus facilement faire un objet que dhab
    def __init__(self, x, y):
        super().__init__() # on est obliges car cest une sous-classe
        self.sprite_sheet = pygame.image.load('enemy.png')# tu vois limage de l'ennemi? on en fait un attribut "sprite sheet" , comme ca on peut interagir avec , et la decouper en fonction des mouvemets du joeur
        self.image = self.get_image(0, 0) # tu comprendras mieux avec la fonction plus bas
        self.image.set_colorkey([0, 0, 0]) # ca marche pas on a pas de png potable
        self.rect = self.image.get_rect()  # tu comprendras avec la fonction
        self.position = [x, y] # c dans la nom
        self.images = {
            'front': self.get_image(0, 0),
            'back': self.get_image(0, 68),
            'left_side': self.get_image(0, 136),
            'right_side': self.get_image(0, 204)
        }  # donc , a travers un dictionnaire jai donne a des clef des images comme ca lors des mvt jai juste a dire le nom l'image que je veux
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

    def get_image(self, x, y): #en vrai tas capte , allez
        image = pygame.Surface([46, 68])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 46, 68))
        return image
