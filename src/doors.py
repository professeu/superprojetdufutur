import pygame


class Door:
    def __init__(self, rect, destination, condition, player):

        # rect de la porte
        self.rect = rect
        # carte d'arrivée
        self.destination = destination
        # condition qui défini si la porte est ouverte
        self.opened = condition
        self.player = player
        # liste des enemis

    def change_map(self, player):

        if self.opened and pygame.Rect.colliderect(self.rect, player.rect):
            return True, self.destination
        else:
            return False, 0
