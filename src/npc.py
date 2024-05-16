import pygame.rect

from entity import Entity


class NPC(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.direction = 'front'
        self.talk_box = pygame.image.load('./images/chest_contenu.png')

    def talk(self, game):
        if self.rect.colliderect(game.player.rect):
            game.pause = True

            game.screen.blit(self.talk_box, (230, 400))
            rect = self.talk_box.get_rect()
            play_text = game.font.render('Play', True, (255, 255, 255))
            play_text_rect = play_text.get_rect(center=rect.center)
            game.screen.blit(play_text, play_text_rect)