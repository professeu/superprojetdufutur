import pygame

pygame.init()

class GameoverScreen():

    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        self.background = pygame.image.load("images/gameover_image.jpg")
        pygame.display.set_caption('Le Labyrinthe Mystérieux')
        self.play_button = pygame.Rect(300, 300, 200, 50)

    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                 # Check if the mouse click is inside the play button area
                    running = False
                if self.play_button.collidepoint(event.pos):
                    running = False

        self.screen.blit(self.background, (0, 0))

        font = pygame.font.SysFont(None, 64)  # Choose your font and size
        text = font.render('Game Over', True, (255, 255, 255))  # White color
        text_rect = text.get_rect(center=(400, 100))  # Position the text at the center top of the screen
        self.screen.blit(text, text_rect)

        pygame.draw.rect(self.screen, (50, 50, 100), self.play_button)  # Green button color
        play_text = font.render('Rejouer', True, (255, 255, 255))  # White text color
        play_text_rect = play_text.get_rect(center=self.play_button.center)
        self.screen.blit(play_text, play_text_rect)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    gameoverscreen = GameoverScreen()
    gameoverscreen.run()
