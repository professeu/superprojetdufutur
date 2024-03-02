import pygame
import pytmx
import pyscroll
from pythonProjectJEU.player import Player


class Game:
    def __init__(self):

        # creation fenetre

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('le labyrinthe mysterieux')

        # charger la carte

        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # generer un joueur sur la carte
        player_position = tmx_data.get_object_by_name('playerspawn')
        self.player = Player(player_position.x, player_position.y)

        #liste dobjets qui font des collisions

        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))


        # dessiner le groupe de claques

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

    def moving(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_u()
        if pressed[pygame.K_DOWN]:
            self.player.move_d()
        if pressed[pygame.K_RIGHT]:
            self.player.move_r()
        if pressed[pygame.K_LEFT]:
            self.player.move_l()

    def run(self):

        clock = pygame.time.Clock()

        # boucle du jeu ( fermer le jeu )
        running = True

        while running:

            self.moving()
            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
