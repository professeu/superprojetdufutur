import pygame

pygame.init()


class Homescreen:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600)) # l'attribut qui fait un ecran quon va donner au homescreen de la page main
        self.background = pygame.image.load('home_image.jpg') #alors avec ca on met un background , g pas la bonne taile de photo
        pygame.display.set_caption('Game Over')
        self.play_button = pygame.Rect(300, 300, 200, 50)

    def run(self):
        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mouse click is inside the play button area
                    if self.play_button.collidepoint(event.pos):
                        running = False

            # Draw the background image
            self.screen.blit(self.background, (0, 0))

            # Draw title text
            font = pygame.font.SysFont(None, 64)  # Choose your font and size
            text = font.render('Le Labyrinthe Mystérieux', True, (255, 255, 255))  # White color
            text_rect = text.get_rect(center=(400, 100))  # Position the text at the center top of the screen
            self.screen.blit(text, text_rect)

            # Draw the play button
            pygame.draw.rect(self.screen, (50, 50, 100), self.play_button)  # Green button color
            play_text = font.render('Play', True, (255, 255, 255))  # White text color
            play_text_rect = play_text.get_rect(center=self.play_button.center)
            self.screen.blit(play_text, play_text_rect)

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    homescreen = Homescreen()
    homescreen.run()

