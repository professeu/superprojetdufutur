import pygame.image
from inventory import Item


class Chest:
    def __init__(self, screen, rect, name_item, player):

        self.image = pygame.image.load('./images/chest_contenu.png')
        self.screen = screen
        self.content = Item(name_item)
        self.alive = True
        self.opened = False
        self.rect = rect

        self.player = player

    def open(self):
        if self.alive:
            if self.rect.colliderect(self.player.rect):
                self.opened = True

    def draw(self, game):
        if self.opened:
            game.pause = True
            self.screen.blit(self.image, (230, 280))
            self.image.blit(self.content.image, (0, 0))

    def ramasse_obj(self, game):
        if self.opened:
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                self.player.inventory.slots.append(self.content)
                self.opened = False
                self.alive = False
                game.pause = False
                
    def update(self, game):
        self.open()
        self.draw(game)
        self.ramasse_obj(game)
