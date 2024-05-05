import pygame
import pyscroll
import pytmx


class Map:

    def __init__(self):
        self.tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        self.map_data = pyscroll.TiledMapData(self.tmx_data)
