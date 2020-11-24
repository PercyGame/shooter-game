"""Ceci est un des sciptes utilisé par le main"""


import pygame


"""classe du joueur"""
class Player(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('player1.png')
        self.rect = self.image.get_rect()
        self.bullet = 30
        self.max_bullet = 30
        self.reloading = 0