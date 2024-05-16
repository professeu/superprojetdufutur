import pygame.rect

from entity import Entity


class NPC(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.position = [x, y]
        self.save_position()
        self.move_d()
        self.direction = 'front'
        self.talk_box = pygame.image.load('./images/chest_contenu.png')
        self.discours = [
            'Bonjour',
            'Bon chance'
        ]
        self.index = 0
        self.old_key = 0

    def talk(self, game):
        if self.rect.colliderect(game.player.rect) and self.index < len(self.discours):

            game.pause = True

            game.screen.blit(self.talk_box, (230, 400))
            self.talk_box.blit(pygame.image.load('./images/chest_contenu.png'), (0, 0))
            rect = self.talk_box.get_rect()
            play_text = game.font.render(self.discours[self.index], True, (255, 255, 255))
            play_text_rect = play_text.get_rect(center=rect.center)
            self.talk_box.blit(play_text, play_text_rect)
            self.change_sentence()
            if self.index >= len(self.discours):
                game.pause = False

    def change_sentence(self):

        if pygame.key.get_pressed()[pygame.K_RETURN]:
            if not self.old_key:
                self.old_key = pygame.key.get_pressed()[pygame.K_RETURN]
                self.index += 1
        self.old_key = pygame.key.get_pressed()[pygame.K_RETURN]
