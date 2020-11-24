"""Ceci est un des sciptes utilisé par le main"""


import pygame

"""class du mur nord du spawn"""
class MurNordSpawn(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('mur nord spawn.png')
        self.rect = self.image.get_rect()
        self.rect.x = 517
        self.rect.y = 309

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y += self.velocity

    def move_down(self):
        self.rect.y -= self.velocity



class MurOuestSpawn(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('mur ouest spawn.png')
        self.rect = self.image.get_rect()
        self.rect.x = 517
        self.rect.y = 312

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y += self.velocity

    def move_down(self):
        self.rect.y -= self.velocity



class MurEstSuperieurSpawn(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('mur est superieur spawn.png')
        self.rect = self.image.get_rect()
        self.rect.x = 624
        self.rect.y = 312

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y += self.velocity

    def move_down(self):
        self.rect.y -= self.velocity

class MurSudSpawn(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('mur sud spawn.png')
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 416

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y += self.velocity

    def move_down(self):
        self.rect.y -= self.velocity