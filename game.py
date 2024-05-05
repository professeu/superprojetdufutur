import pygame
import pytmx
import pyscroll
# importation des classes contenus dans les autres fichiers python
from player import Player
from enemy import Enemy


class Game:

    def __init__(self):

        # creation fenetre : taille et nom

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('le labyrinthe mysterieux')

        # charger la carte sous format tmx

        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        map_data = pyscroll.TiledMapData(tmx_data)
        map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # generer un joueur sur la carte, playerspawn renseigné sur fichier tmx

        player_position = tmx_data.get_object_by_name('playerspawn')
        # Création de l'objet player en appelant la classe Player
        self.player = Player(player_position.x, player_position.y)
        print(self.player.position)

        # generer un ennemi sur la map

        enemy_position = tmx_data.get_object_by_name('enemyspawn')
        self.enemy = Enemy(enemy_position.x, enemy_position.y)

        self.entities = [self.player, self.enemy]

        # liste de rect qui génèrent des collisions

        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de claques

        # dans l'attribut group chaque couche de la map tiled
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        # ajout des objets au dessus des default layers
        self.group.add(self.player)
        self.group.add(self.enemy)

    def collision_all(self):

        self.player.collision_do()
        self.enemy.collision_do()

    def update(self):
        self.player.image.set_colorkey([0, 0, 0])
        self.enemy.image.set_colorkey([0, 0, 0])
        self.player.update_rect()
        self.enemy.update_rect()
        self.player.save_position()
        self.enemy.save_position()

    def run(self):

        clock = pygame.time.Clock()

        running = True
        # boucle du jeu
        while running:

            self.player.moving_player()
            self.enemy.move_enemy_towards_player(self.player)
            self.collision_all()

            self.update()

            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
