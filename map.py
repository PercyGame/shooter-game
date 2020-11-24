"""Ceci est un des sciptes utilisé par le main"""


import pygame


"""classe de la map"""
class Map(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('map.png')
        self.rect = self.image.get_rect()
        self.rect.x = -1190
        self.rect.y = -700


    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y += self.velocity

    def move_down(self):
        self.rect.y -= self.velocity
