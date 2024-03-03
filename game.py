import pygame
import pytmx
import pyscroll
from player import Player
from enemy import Enemy
# ici nous avons importé les modules pygame, pytmx , et pyscroll. pygame aide pour la creation du jeu en soit ,
# pytmx pour la carte , afin de la modeliser plus facilement et enfin pyscrollsert a se deplacer dans la carte
# ces trois modules sont tres connus dans le monde du jeu video sur python

class Game: #ici nous avons cree un classe game , ainsi on peut lui donner des attributs et on poirra aussi l'appeler
    #fichier main.py , cest une convention de codage de tout coder a lexterieur du fichier main et de tout appeler dans ce meme fichier
    def __init__(self):#La méthode __init__ sert à attribuer à chaque objet de la classe une valeur d'attribut qui lui est propre
    #self represente l'instance de la classe a laquelle on attribuera les attributs

        # creation fenetre

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('le labyrinthe mysterieux')

        # charger la carte

        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        #En gros , on a créé notre carte sous un format tmx et tout ca ca sert a representer la carte , regarde sur internet
        #l'interet de chaque fonction si ca te chante

        # generer un joueur sur la carte

        player_position = tmx_data.get_object_by_name('playerspawn')
        self.player = Player(player_position.x, player_position.y)
        # la premiere ligne cest pour dire cest quoi la position du joueur au tt debut , je montrerai sur tiled ou je lai mis pour mieux comprendre
        # et la deuxieme on a créé lobjet player

        # generer un ennemi sur la map
        enemy_position = tmx_data.get_object_by_name('enemyspawn')
        self.enemy = Enemy(enemy_position.x, enemy_position.y)
        # la meme que au dessus

        # liste dobjets qui font des collisions

        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        # "che ne compwends paww" booba


        # dessiner le groupe de claques

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        #on a mis dans un group , en anglais biensur, chaque couche de la map tiled
        self.group.add(self.player)
        self.group.add(self.enemy)
        #la on rajoute les objets en tant que layer comme ca il peuvent apparaitre au dessus des default layers
        # dommage de bigflo et oli m'a fait pleurer

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

    def move_enemy_towards_player(self):
        # Calculate the vector from enemy to player
        dx = self.player.position[0] - self.enemy.position[0]
        dy = self.player.position[1] - self.enemy.position[1]

        if dx < 0:
            self.enemy.move_l()

        if dx > 0:
            self.enemy.move_r()

        if dy < 0:
            self.enemy.move_u()

        if dy > 0:
            self.enemy.move_d()

        # je texplique meme pas tas compris


    def run(self):

        clock = pygame.time.Clock()

        # boucle du jeu ( fermer le jeu )
        running = True

        while running:

            self.move_enemy_towards_player()
            self.moving()
            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()
            # les methodes elle vont pas vivre seule hein LOOL , dcp on les appelles tout le long , tu veux que je te les explique?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()