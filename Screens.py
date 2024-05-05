import pygame


class Screens:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('le labyrinthe mysterieux')


class Homescreen(Screens):

    def __init__(self):
        super().__init__()

        # background, pas la bonne taile de photo
        self.background = pygame.image.load('home_image.jpg')
        pygame.display.set_caption('Le labyrinthe')
        # Hitbox du bouton
        self.play_button = pygame.Rect(300, 300, 200, 50)
        # Choix de la police et de sa taille
        self.font = pygame.font.SysFont(None, 64)

    # afficher le titre
    def titre(self):
        text = self.font.render('Le Labyrinthe Mystérieux', True, (255, 255, 255))
        # Position du texte
        text_rect = text.get_rect(center=(400, 100))
        self.screen.blit(text, text_rect)

    # afficher le bouton
    def bouton(self):
        pygame.draw.rect(self.screen, (50, 50, 100), self.play_button)
        play_text = self.font.render('Play', True, (255, 255, 255))  # White text color
        play_text_rect = play_text.get_rect(center=self.play_button.center)
        self.screen.blit(play_text, play_text_rect)

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


if __name__ == "__main__":
    homescreen = Homescreen()
    homescreen.run()
