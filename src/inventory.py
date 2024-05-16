import pygame


class Item:

    def __init__(self, name):
        self.name = name
        self.image = pygame.image.load('./images/'+name+'.png')
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.descriptions = {
            'journal': 'Un vieux journal',
            'sword': 'Une épée rouillée',
            'shield': 'De ce bouclier émane une aura qui semble...',
            'amulette': 'blabla',
            'potion_soin': 'Boire cette potion vous rendra de la vie',
            'key': 'Clé'
        }

        self.description = self.descriptions[self.name]


class Inventaire:

    def __init__(self):

        self.show_active = False

        self.image = pygame.image.load('./images/inventory.png')
        self.length = 9
        self.slots = []

        self.current_slot = 0
        self.font = pygame.font.SysFont(None, 64)

        self.old_key = 0
        self.time = pygame.time.get_ticks()
        self.cooldown = 500

    def ramasser_obj(self, item):
        self.slots.append(item)

    def parcourir_inventaire(self):

        if pygame.key.get_pressed()[pygame.K_q] and self.current < self.lenght:
            self.current_slot = + 1

        if pygame.key.get_pressed()[pygame.K_d] and self.current > 0:
            self.current_slot = -1

    def item_position(self, i):
        length = 3
        x = i
        y = 0
        while x >= length:
            y += 1
            x -= 3
        x = 120*x + 20
        y = 120*y + 20
        return x, y

    def draw(self, game):
        self.open_or_close(game)
        if self.show_active:
            game.pause = True
            pygame.Surface.blit(game.screen, self.image, (230, 130))
            for i in range(len(self.slots)):
                item = self.slots[i]
                if item:
                    x, y = self.item_position(i)
                    self.image.blit(item.image, (x, y))

    def open_or_close(self, game):

        if pygame.key.get_pressed()[pygame.K_i]:
            if not self.old_key:
                self.old_key = pygame.key.get_pressed()[pygame.K_i]
                if self.show_active:
                    self.show_active = False
                    game.pause = False
                else:
                    self.show_active = True
                    game.pause = True
        self.old_key = pygame.key.get_pressed()[pygame.K_i]



