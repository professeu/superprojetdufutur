import pygame
from game import Game
from ScreensClass import Homescreen


if __name__ == '__main__':
    pygame.init()
    homescreen = Homescreen()
    homescreen.run()
    game = Game()
    game.run()



