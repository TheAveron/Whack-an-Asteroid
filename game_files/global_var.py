import pygame
import json
from random import randint, choice

from .Sprites import *
from .screen import *


# Récupération des valeurs de la configuration de base du jeu
with open('data.json','r') as datafile:
	game_data:dict=json.load(datafile)

pygame.display.set_caption('Whack an asteroid') # Définition du titre de la fenêtre
pygame.display.set_icon(pygame.image.load('Static/Big_Asteroid.png')) # Définition de l'icone de la fenêtre

Texts_menu:list[Text] = [Text('Jouer',(0,40), color=(42, 40, 57)), Text('Whack an Asteroid',(0,-200),50,True,color=(42, 40, 57))] # Crée les textes du menu du jeu
Texts_game:dict[Text] = {'Win':Text('Gagné'), 'Lose':Text('Perdu'),"Pause":Taupe("Pause",type='Pause',position=(game_data['width']-66,20),indexage=False)} # Crée les textes pour les victoires et défaites
Texts_end:list[Text | dict[Text]]  = [Text('Restart',(0,90),60, color=(42, 40, 57)),{"Win":Text("Congratulation you win !",(0,-100), bold=True,  color=(42, 40, 57)), 'Lose':Text("You lose ! !",(0,-100),bold=True,  color=(42, 40, 57))}] # Crée les textes du menu de fin