#importation des modules nécessaires
import pygame
import pytmx
import pyscroll
#importation des classes contenus dans les autres fichiers .py
from player import Player
from enemy import Enemy

#Création classe game
class Game:

    def __init__(self):
    #self represente l'instance de la classe a laquelle on attribuera les attributs

        # creation fenetre : taille et nom

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('le labyrinthe mysterieux')

        # charger la carte qui est sous format tmx

        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2


        # generer un joueur sur la carte
        """position initiale du joueur dans la variable player_position
        'playerspawn' étant resneigné dans map.tmx"""
        player_position = tmx_data.get_object_by_name('playerspawn')
        #Création de l'objet player en appelant la classe Player
        self.player = Player(player_position.x, player_position.y)


        # generer un ennemi sur la map
        #Même chose que pour le joueur
        enemy_position = tmx_data.get_object_by_name('enemyspawn')
        self.enemy = Enemy(enemy_position.x, enemy_position.y)


        # liste dobjets qui font des collisions

        self.walls = []
        """l'attribut objects de l'objet tmx_data est une liste d'objets, obj
        est successivement chacun des objets de la liste, ces objets correspondants
        à une case/tuile"""
        for obj in tmx_data.objects:
            """l'attribut type contient le type de la case, qui est un str,
            si la case doit déclencher une collision, on met un rect
            correspondant dans self.walls"""
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))



        # dessiner le groupe de claques

        #dans l'attribut group chaque couche de la map tiled
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        #on rajoute les objets pour quils apparaissent au dessus des default layers
        self.group.add(self.player)
        self.group.add(self.enemy)

    def collision(self):
       for obj in self.walls:
           if pygame.Rect.colliderect(obj,self.player.rect):
               return True

    #moving() deplace le joueur
    def moving(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_u()
            if self.collision():
                self.player.move_d()
        if pressed[pygame.K_DOWN]:
            self.player.move_d()
            if self.collision():
                self.player.move_u()
        if pressed[pygame.K_RIGHT]:
            self.player.move_r()
            if self.collision():
                self.player.move_l()
        if pressed[pygame.K_LEFT]:
            self.player.move_l()
            if self.collision():
                self.player.move_r()



    #fonction déterminant le déplacement de l'ennemi
    def move_enemy_towards_player(self):
        """

        #calcul de svecteurs déplacements en x et en y
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

        """




    def run(self):

        clock = pygame.time.Clock()


        running = True
        # boucle du jeu
        while running:

            self.move_enemy_towards_player()
            self.moving()

            self.player.image.set_colorkey([0, 0, 0])
            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()