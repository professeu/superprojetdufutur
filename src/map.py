import pygame, pyscroll, pytmx
from doors import Door
from chest import Chest
from npc import NPC
from enemy import Enemy


class Map:
    def __init__(self, name, player, screen):

        self.name = name
        self.screen = screen
        self.player = player

        self.tmx_data = pytmx.util_pygame.load_pygame('./map/' + name + ".tmx")
        self.map_data = pyscroll.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(self.map_data, self.screen.get_size())
        self.map_layer.zoom = 2

        self.walls = []
        self.chests = []
        self.doors = []
        self.enemies = []
        self.npcs = []
        for obj in self.tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.name == 'coffre':
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                self.chests.append(Chest(self.screen, rect, obj.type, self.player))
            if obj.name == 'enemy':
                self.enemies.append(Enemy(obj.x, obj.y))
            elif obj.name == 'door':
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                self.doors.append(Door(rect, obj.type, True, self.player))
                self.walls.append(rect)
            elif obj.name == 'NPC':
                self.npcs.append(NPC(obj.x, obj.y))

            self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=5)
            for enemy in self.enemies:
                self.group.add(enemy)
            for npc in self.npcs:
                self.group.add(npc)
            self.group.add(self.player)


class MapManager:
    def __init__(self, screen, player):

        self.maps = []
        self.screen = screen
        self.player = player

        self.current_map = "start_room"
        self.old_map = self.current_map
        self.register_all()
        self.teleport_player()
        self.other_map = False

    def register_map(self, name):
        self.maps.append(Map(name, self.player, self.screen))

    def register_all(self):
        self.register_map("start_room")
        self.register_map("mapA")
        self.register_map("mapA1")
        self.register_map("mapB")
        self.register_map("mapB1")
        self.register_map("mapC")
        self.register_map("mapD")

    def get_map(self, name):
        for i in self.maps:
            if i.name == name:
                return i

    def get_currentmap(self):
        for i in self.maps:
            if i.name == self.current_map:
                return i

    def get_walls(self):
        return self.get_currentmap().walls

    def get_group(self):
        return self.get_currentmap().group

    def get_object(self, name):
        for obj in self.get_currentmap().tmx_data.objects:
            if obj.name == name and obj.type == self.old_map:
                return obj

    def teleport_player(self):
        spawnpoint = self.get_object("playerspawn")
        self.player.position = [spawnpoint.x, spawnpoint.y]
        self.player.save_position()

    def update_map(self):
        for door in self.get_currentmap().doors:
            if door.change_map(self.player)[0]:
                self.old_map = self.current_map
                self.current_map = door.change_map(self.player)[1]
                self.maps.remove(self.get_currentmap())
                self.register_map(self.current_map)
                self.other_map = True
                self.teleport_player()
