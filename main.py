import pygame
from game import Game
from home_screen import Homescreen
from gameover_screen import GameoverScreen

if __name__ == '__main__':
    pygame.init()
    homescreen = Homescreen()
    homescreen.run()
    game = Game()
    game.run()
    goverscreen = GameoverScreen()
    goverscreen.run()


