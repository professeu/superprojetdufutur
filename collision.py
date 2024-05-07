import pygame
from map import Map


class Collision:
    def __init__(self):

        carte = Map()

        self.walls = []

        for obj in carte.tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
