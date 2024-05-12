import pygame


class Screens:

    def __init__(self):

        # Hitbox du bouton
        self.play_button = pygame.Rect(300, 300, 200, 50)

        # Choix de la police et de sa taille
        self.font = pygame.font.SysFont(None, 64)

    # afficher le titre
    def titre(self, screen, caption):
        text = self.font.render(caption, True, (255, 255, 255))
        # Position du texte
        text_rect = text.get_rect(center=(400, 100))
        screen.blit(text, text_rect)

    # afficher le bouton
    def bouton(self, screen, caption):
        pygame.draw.rect(self.screen, (50, 50, 100), self.play_button)
        play_text = self.font.render(caption, True, (255, 255, 255))
        play_text_rect = play_text.get_rect(center=self.play_button.center)
        screen.blit(play_text, play_text_rect)


class Homescreen(Screens):

    def __init__(self):
        super().__init__()

        self.background = pygame.image.load('home_image.jpg')



    def run(self):

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Test si on a cliqué sur le bouton
                    if self.play_button.collidepoint(event.pos):
                        running = False

            # afficher l'image de fond
            self.screen.blit(self.background, (0, 0))

            self.titre()

            self.bouton()

            pygame.display.flip()

        pygame.quit()
