"""Ceci est le Main de Z-Kill
Il fait appele à tout les scripts présent dans
importation pour le programme"""
from game import Game

"""importations pour le programme"""
import pygame
import sys
from player import *
from map import *
from ClassMurSpawn import *
from game import *

"""attribution:"""
"""Icons made by <a href="https://www.flaticon.com/authors/surang" title="surang">surang</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>"""


def attribution():
    print("")
    print("""Attribution:""")
    print(
        """Icons made by <a href="https://www.flaticon.com/authors/surang" title="surang">surang</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>""")
    print("")


pygame.init()
pygame.mixer.init()

"""Variable et fonction qui joue la musique de fond du jeu"""

mus = pygame.mixer.music.load('Barge.wav')
pygame.mixer.music.rewind()
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(1000000000, 0.0)

"""créer le fenêtre"""
x = 1200
y = 700
fenetre = pygame.display.set_mode((x, y))
"""renome la fenêtre"""
pygame.display.set_caption("Shooter Game")
"""change l'icon de la fenêtre"""
icon = pygame.image.load("shooter.ico")
pygame.display.set_icon(icon)

# Coordoné de base du joueur
x_joueur = 574
y_joueur = 324
x_base_joueur = 574
y_base_joueur = 324

game = Game()

# groupe de sprit pour les collision entre le joueur et les murs
mur = pygame.sprite.Group()
mur.add(game.mur_sud_spawn, game.mur_nord_spawn, game.mur_ouest_spawn, game.mur_est_superieur_spawn)

font_texte = pygame.font.Font("Font/D Day Stencil.ttf", 25)
font_texte2 = pygame.font.Font("Font/D Day Stencil.ttf", 75)
txt_health = font_texte.render("Health", 1, (255, 255, 255))
txt_bullet = font_texte.render("Bullet", 1, (255, 255, 255))
txt_reload = font_texte2.render("Reload", 1, (200, 0, 0))
player_heath_barre = pygame.Color(15, 255, 0)
player_bullet_barre = pygame.Color(15, 255, 0)
gris = pygame.Color(113, 113, 113)
gris_foncé = pygame.Color(93, 93, 93)
tire = pygame.mixer.Sound("Rifle_Shot_Echo.wav")

# variable pour les munition
weapon_charged: bool = True

# variable pour le déplacement spécial du joueur
player_move_y: bool = False
player_move_x: bool = False

"""variable de la boucle de jeu"""
run: bool = True

"""Boucle de jeu"""
while run:

    co_mouse = pygame.mouse.get_pos()

    taille_barre_de_vie = game.player.health * 2
    taille_barre_de_munition = game.player.bullet * 6

    if game.map.rect.y != 0:
        y_0_map = True
    else:
        y_0_map = False

    if game.map.rect.y != -1400:
        y_1400_map = True
    else:
        y_1400_map = False

    if game.map.rect.x != 0:
        x_0_map = True
    else:
        x_0_map = False

    if game.map.rect.x != -2400:
        x_2400_map = True
    else:
        x_2400_map = False

    if game.pressed.get(pygame.K_w) and y_0_map == True and player_move_y == False:
        game.map.move_up()
        game.mur_nord_spawn.move_up()
        game.mur_ouest_spawn.move_up()
        game.mur_est_superieur_spawn.move_up()
        game.mur_sud_spawn.move_up()
    elif game.pressed.get(pygame.K_w) and y_0_map == False and y_joueur >= 0:
        y_joueur -= game.player.velocity
        player_move_y = True
    if game.pressed.get(pygame.K_s) and y_0_map == False and y_joueur >= 0 and y_joueur <= y_base_joueur and player_move_y == True:
        y_joueur += game.player.velocity
        if y_joueur == y_base_joueur:
            player_move_y = False

    if game.pressed.get(pygame.K_s) and y_1400_map == True and player_move_y == False:
        game.map.move_down()
        game.mur_nord_spawn.move_down()
        game.mur_ouest_spawn.move_down()
        game.mur_est_superieur_spawn.move_down()
        game.mur_sud_spawn.move_down()
    elif game.pressed.get(pygame.K_s) and y_1400_map == False and y_joueur <= 648:
        y_joueur += game.player.velocity
        player_move_y = True
    if game.pressed.get(pygame.K_w) and y_1400_map == False and y_joueur <= 648 and y_joueur >= y_base_joueur and player_move_y == True:
        y_joueur -= game.player.velocity
        if y_joueur == y_base_joueur:
            player_move_y = False

    if game.pressed.get(pygame.K_a) and x_0_map == True and player_move_x == False:
        game.map.move_right()
        game.mur_nord_spawn.move_right()
        game.mur_ouest_spawn.move_right()
        game.mur_est_superieur_spawn.move_right()
        game.mur_sud_spawn.move_right()
    elif game.pressed.get(pygame.K_a) and x_0_map == False and x_joueur >= 0:
        x_joueur -= game.player.velocity
        player_move_x = True
    if game.pressed.get(pygame.K_d) and x_0_map == False and x_joueur >= 0 and x_joueur <= x_base_joueur and player_move_x == True:
        x_joueur += game.player.velocity
        if x_joueur == x_base_joueur:
            player_move_x = False

    if game.pressed.get(pygame.K_d) and x_2400_map == True and player_move_x == False:
        game.map.move_left()
        game.mur_nord_spawn.move_left()
        game.mur_ouest_spawn.move_left()
        game.mur_est_superieur_spawn.move_left()
        game.mur_sud_spawn.move_left()
    elif game.pressed.get(pygame.K_d) and x_2400_map == False and x_joueur <= 1149:
        x_joueur += game.player.velocity
        player_move_x = True
    if game.pressed.get(pygame.K_a) and x_2400_map == False and x_joueur <= 1149 and x_joueur >= x_base_joueur and player_move_x == True:
        x_joueur -= game.player.velocity
        if x_joueur == x_base_joueur:
            player_move_x = False

    """Pour fermer le jeu"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # appel attribution qui gère le attibution du programme
            pygame.quit()
            attribution()
            sys.exit()


        # Pour bouger le joueur
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # pour que le joueur tire

        elif pygame.mouse.get_pressed() == (1, 0, 0):
            if weapon_charged:
                pygame.mixer.Sound.play(tire)
                game.player.bullet -= 1
            else:
                pass

    """applique l'image de la map"""
    fenetre.blit(game.map.image, game.map.rect)

    """applique l'image du joueur"""
    fenetre.blit(game.player.image, (x_joueur, y_joueur))

    """appliquer l'image du mur nord spawn"""
    fenetre.blit(game.mur_nord_spawn.image, game.mur_nord_spawn.rect)

    """appliquer l'image du mur ouest spawn"""
    fenetre.blit(game.mur_ouest_spawn.image, game.mur_ouest_spawn.rect)

    """appliquer l'image du mur est superieur spawn"""
    fenetre.blit(game.mur_est_superieur_spawn.image, game.mur_est_superieur_spawn.rect)

    """appliquer l'image du mur sud spawn"""
    fenetre.blit(game.mur_sud_spawn.image, game.mur_sud_spawn.rect)

    # dessiner la barre de vie du joueur
    pygame.draw.rect(fenetre, gris, ((0, 0), (250, 175)))
    pygame.draw.rect(fenetre, gris_foncé, ((24, 49), (202, 27)))
    pygame.draw.rect(fenetre, player_heath_barre, ((25, 50), (taille_barre_de_vie, 25)))
    fenetre.blit(txt_health, (25, 25))

    # dessiner la barre de munition du joueur
    pygame.draw.rect(fenetre, gris_foncé, ((24, 99), (182, 27)))
    pygame.draw.rect(fenetre, player_bullet_barre, ((25, 100), (taille_barre_de_munition, 25)))
    fenetre.blit(txt_bullet, (25, 75))

    if game.player.bullet == 0:
        weapon_charged = False
        fenetre.blit(txt_reload, (574, 150))
        game.player.reloading = game.player.reloading + 1
        if game.player.reloading == 150:
            weapon_charged = True
            game.player.bullet = game.player.max_bullet
            game.player.reloading = 0

    if game.player.health == 50:
        player_heath_barre = pygame.Color(255, 150, 0)
    elif game.player.health == 20:
        player_heath_barre = pygame.Color(255, 0, 0)
    # couper le jeu si le joueur n'a plus de vie
    elif game.player.health <= 0:
        # appel attribution qui gère le attibution du programme
        pygame.quit()
        attribution()
        sys.exit()




    """met à jour l'affichage de l'écran"""
    pygame.display.flip()
