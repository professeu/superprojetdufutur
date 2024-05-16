import pygame

# importation des classes contenus dans les autres fichiers python
from player import Player
from enemy import Enemy
from map import MapManager


class Game:

    def __init__(self):

        # creation fenetre, taille et nom
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('le labyrinthe mysterieux')

        # police d'écriture utilsée pour tout le jeu
        self.font = pygame.font.SysFont(None, 64)

        # ecran d'accueil :
        # hitbox du bouton
        self.play_button = pygame.Rect(300, 300, 200, 50)
        # image de fond
        self.home_background = pygame.image.load('./images/home_image.jpg')

        # écran de défaite :
        # l'image de fond est redimensionnée pour correspondre à la taille de l'écran
        self.gameover_background = pygame.image.load("./images/gameover_image.jpg")
        self.gameover_background = pygame.transform.scale(self.gameover_background, self.screen_size)

        # booléens pour les différentes boucles

        # si on affiche la fenêtre
        self.running = True
        # si on est dans la boucle de jeu
        self.playing = False

        self.pause = False

        # image des infos du joueur, placée en haut à droite
        self.player_infowindow = pygame.image.load('./images/player_info.png')

        self.player = Player(0, 0)
        self.enemies = []

        self.map_manager = MapManager(self.screen, self.player)
        for enemy in self.map_manager.get_currentmap().enemies:
            self.enemies.append(Enemy(enemy[0], enemy[1]))

        self.group = self.map_manager.get_group()

        for npc in self.map_manager.get_currentmap().npcs:
            self.group.add(npc)

        for enemy in self.enemies:
            self.group.add(enemy)
        self.walls = self.map_manager.get_walls()

    def collision_all(self):
        # l'action des collisions sur les entités
        self.player.collision_do(self.walls)
        for proj in self.player.projectiles:
            proj.collision_do(self.walls)
        for enemy in self.enemies:
            enemy.collision_do(self.walls)

    def show_health_player(self):
        # dessine un rectangle noir puis un rectangle vers au-dessus, dont la longueur varie en fonction des pv
        pv_rect = pygame.Rect(80, 10, (self.player.health / self.player.health_max) * 110, 20)
        pygame.Surface.blit(self.screen, self.player_infowindow, (0, 0))
        pygame.draw.rect(self.player_infowindow, (26, 0, 4), pygame.Rect(80, 10, 110, 20))
        pygame.draw.rect(self.player_infowindow, "green", pv_rect)

    def show_inventory(self):
        self.player.inventory.draw(self)

    def update_all(self):
        # met à jour tous les éléments visuels des entités

        self.player.update()
        self.show_health_player()

        for door in self.map_manager.get_currentmap().doors:
            if door.opened and door.rect in self.map_manager.get_currentmap().walls:
                self.map_manager.get_currentmap().walls.remove(door.rect)

        for proj in self.player.projectiles:
            self.group.add(proj)
            proj.update()
            # retire le projectile des attributs group et enemies s'il n'est plus "en vie"
            if not proj.alive:
                self.group.remove(proj)
                self.player.projectiles.remove(proj)
            # test l'attaque sur tous les enemis
            for enemy in self.enemies:
                proj.attack(enemy)

        self.map_manager.update_map()
        if self.map_manager.other_map:
            self.enemies = []
            for enemy in self.map_manager.get_currentmap().enemies:
                self.enemies.append(Enemy(enemy[0], enemy[1]))
            self.map_manager.other_map = False
            self.group = self.map_manager.get_group()

            for enemy in self.enemies:
                self.group.add(enemy)
            self.walls = self.map_manager.get_walls()

        for enemy in self.enemies:
            enemy.update()
            # retire l'ennemi s'il est mort
            if enemy.health <= 0:
                self.group.remove(enemy)
                self.enemies.remove(enemy)

    # Gérer l'écran d'accueil:
    def titre(self, titre):
        text = self.font.render(titre, True, (255, 255, 255))
        # Position du texte
        text_rect = text.get_rect(center=(400, 100))
        # affichage du texte
        self.screen.blit(text, text_rect)

    def bouton(self):
        # affiche le bouton
        pygame.draw.rect(self.screen, (50, 50, 100), self.play_button)
        play_text = self.font.render('Play', True, (255, 255, 255))
        # création d'un nouveau rect en fonction du texte souhaité qui permet de centrer celui-ci
        play_text_rect = play_text.get_rect(center=self.play_button.center)
        # affiche le texte
        self.screen.blit(play_text, play_text_rect)

    def homescreen_run(self):
        # boucle de l'écran d'accueil

        while self.running and not self.playing:

            # si la croix est cliquée, on n'affiche plus la fenêtre
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # si click de la souris: test si la position touche le bouton
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Test si on a cliqué sur le bouton
                    if self.play_button.collidepoint(event.pos):
                        self.playing = True

            # afficher l'image de fond
            self.screen.blit(self.home_background, (0, 0))

            # afficher le titre
            self.titre('Le labyrinthe')

            # afficher le bouton
            self.bouton()

            # actualiser l'écran
            pygame.display.flip()

    def play(self):

        # gestion des fps
        clock = pygame.time.Clock()

        # boucle du jeu
        while self.running and self.playing:
            if not self.pause:

                self.player.moving_player()
                self.player.attack(self.enemies)

                for enemy in self.enemies:
                    enemy.moving(self.player)
                self.collision_all()

                for npc in self.map_manager.get_currentmap().npcs:
                    npc.talk(self)

                self.update_all()

            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)

            self.show_inventory()
            for chest in self.map_manager.get_currentmap().chests:
                chest.update(self)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # fin du jeu si le joueur a perdu
            if self.player.health <= 0:
                self.playing = False

            clock.tick(60)

    def gameover(self):
        # boucle de l'écran de game over

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
        # on sort de ces boucles ssi self.running = False donc on ferme ensuite la fenêtre
        pygame.quit()
