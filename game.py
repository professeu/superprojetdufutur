import pygame
import pytmx
import pyscroll
# importation des classes contenus dans les autres fichiers python
from player import Player
from enemy import Enemy
from Screens import Homescreen


class Game:

    def __init__(self):

        # creation fenetre : taille et nom
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('le labyrinthe mysterieux')

        # police d'écriture utilsée
        self.font = pygame.font.SysFont(None, 64)

        # ecran d'accueil
        self.play_button = pygame.Rect(300, 300, 200, 50)
        self.home_background = pygame.image.load('home_image.jpg')

        # écran défaite
        self.gameover_background = pygame.image.load("images/gameover_image.jpg")
        self.gameover_background = pygame.transform.scale(self.gameover_background, self.screen_size)

        # booléens pour les différentes boucles
        self.running = True
        self.playing = False

        # image des infos du joueur qui sera placée en haut à droite
        self.player_infowindow = pygame.image.load('images/player_info.png')

        # charger la carte sous format tmx
        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        map_data = pyscroll.TiledMapData(tmx_data)
        map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # generer un joueur sur la carte
        player_position = tmx_data.get_object_by_name('playerspawn')

        # Création de l'objet player
        self.player = Player(player_position.x, player_position.y)

        # generer des ennemis sur la map
        self.enemies = []
        for obj in tmx_data.objects:
            if obj.name == "enemy":
                self.enemies.append(Enemy(obj.x, obj.y))

        # liste de rect qui génèrent des collisions
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de claques

        # dans group chaque couche de la map tiled
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)

        # ajout du joueur et des ennemis
        self.group.add(self.player)

        for enemy in self.enemies:
            self.group.add(enemy)

    def collision_all(self):

        self.player.collision_do()
        for enemy in self.enemies:
            enemy.collision_do()

    def show_health_player(self):
        pv_rect = pygame.Rect(80, 10, (self.player.health / self.player.health_max) * 110, 20)
        pygame.Surface.blit(self.screen, self.player_infowindow, (0, 0))
        pygame.draw.rect(self.player_infowindow, (26, 0, 4), pygame.Rect(80, 10, 110, 20))
        pygame.draw.rect(self.player_infowindow, "green", pv_rect)

    def update_all(self):
        for proj in self.player.projectiles:
            self.group.add(proj)
            proj.update()
            if not proj.alive:
                self.group.remove(proj)
                self.player.projectiles.remove(proj)
            for enemy in self.enemies:
                proj.attack(enemy)
        self.player.update()
        self.show_health_player()
        for enemy in self.enemies:
            enemy.update()
            if enemy.health <= 0:
                self.group.remove(enemy)
                self.enemies.remove(enemy)

    # Gérer l'écran d'accueil:
    def titre(self, titre):
        text = self.font.render(titre, True, (255, 255, 255))
        # Position du texte
        text_rect = text.get_rect(center=(400, 100))
        self.screen.blit(text, text_rect)

    def bouton(self):
        pygame.draw.rect(self.screen, (50, 50, 100), self.play_button)
        play_text = self.font.render('Play', True, (255, 255, 255))  # White text color
        play_text_rect = play_text.get_rect(center=self.play_button.center)
        self.screen.blit(play_text, play_text_rect)

    def homescreen_run(self):

        while self.running and not self.playing:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Test si on a cliqué sur le bouton
                    if self.play_button.collidepoint(event.pos):
                        self.playing = True

            # afficher l'image de fond
            self.screen.blit(self.home_background, (0, 0))

            self.titre('Le labyrinthe')

            self.bouton()

            pygame.display.flip()

    def play(self):

        clock = pygame.time.Clock()

        # boucle du jeu
        while self.running and self.playing:

            self.player.moving_player()

            for enemy in self.enemies:
                enemy.moving(self.player)
                self.player.attack(enemy)
            self.collision_all()

            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)

            self.update_all()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.player.health <= 0:
                self.playing = False

            clock.tick(60)

    def gameover(self):

        while self.running and not self.playing:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Test si on a cliqué sur le bouton
                    if self.play_button.collidepoint(event.pos):
                        self.playing = True

            # afficher l'image de fond
            self.screen.blit(self.gameover_background, (0, 0))

            self.titre('Game Over')

            self.bouton()

            pygame.display.flip()

    def run(self):
        self.homescreen_run()
        self.play()
        self.gameover()
        pygame.quit()
