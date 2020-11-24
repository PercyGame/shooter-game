"""Ceci est un des sciptes utilisé par le main"""


import pygame

from ClassMurSpawn import MurEstSuperieurSpawn
from player import *
from map import *
from ClassMurSpawn import *



"""Class du jeu"""
class Game:


    def __init__(self):
        self.player = Player()
        self.map = Map()
        self.mur_nord_spawn = MurNordSpawn()
        self.mur_ouest_spawn = MurOuestSpawn()
        self.mur_est_superieur_spawn = MurEstSuperieurSpawn()
        self.mur_sud_spawn = MurSudSpawn()
        self.pressed = {}
