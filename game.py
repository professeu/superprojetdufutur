# importation des modules nécessaires
import pygame
import pytmx
import pyscroll
# importation des classes contenus dans les autres fichiers .py
from player import Player
from enemy import Enemy


# Création classe game
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

        # generer un ennemi sur la map

        enemy_position = tmx_data.get_object_by_name('enemyspawn')
        self.enemy = Enemy(enemy_position.x, enemy_position.y)

        # liste de rect qui génèrent des collisions

        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de claques

        # dans l'attribut group chaque couche de la map tiled
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        # on rajoute les objets pour quils apparaissent au dessus des default layers
        self.group.add(self.player)
        self.group.add(self.enemy)

    # moving() deplace le joueur

    def moving_player(self):

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            # self.player.save_position()
            self.player.move_u()

        if pressed[pygame.K_DOWN]:
            # self.player.save_position()
            self.player.move_d()

        if pressed[pygame.K_RIGHT]:
            # self.player.save_position()
            self.player.move_r()

        if pressed[pygame.K_LEFT]:
            # self.player.save_position()
            self.player.move_l()

    # fonction déterminant le déplacement de l'ennemi
    """
    def move_enemy_towards_player(self):
        # calcul de vecteurs déplacement en x et en y
    
        dx = int(self.player.position[0] - self.enemy.position[0])
        dy = int(self.player.position[1] - self.enemy.position[1])
    
        if dx < 0:
            self.enemy.move_l()
    
        if dx > 0:
            self.enemy.move_r()
    
        if dy < 0:
            self.enemy.move_u()
    
        if dy > 0:
            self.enemy.move_d()
        """

    def collision_player(self):
        if self.player.collision_test(self.walls):
            self.player.move_back()

    def run(self):

        clock = pygame.time.Clock()

        running = True
        # boucle du jeu
        while running:

            self.player.save_position()
            self.moving_player()
            self.collision_player()
            # self.move_enemy_towards_player()

            self.player.image.set_colorkey([0, 0, 0])
            self.enemy.image.set_colorkey([0, 0, 0])
            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()

