import pygame
import json
from random import randint, choice

from .Sprites import *
from .screen import *


# Récupération des valeurs de la configuration de base du jeu
with open('data.json','r') as datafile:
	game_data:dict=json.load(datafile)

pygame.display.set_caption('Jeu de la taupe') # Définition du titre de la fenêtre

Texts_menu:list[Text] = [Text('Jouer',(0,40), color=(42, 40, 57)), Text('Jeu de la taupe',(0,-200),50,True,color=(42, 40, 57))] # Crée les textes du menu du jeu
Texts_game:dict[Text] = {'Win':Text('Gagné'), 'Lose':Text('Perdu')} # Crée les textes pour les victoires et défaites
Texts_end:list[Text | dict[Text]]  = [Text('Rejouer',(0,90),60, color=(20,20,20)),{"Win":Text("Félicitation vous avez gagné !",(0,-100), bold=True, color=(20,20,20)), 'Lose':Text("C'est dommage, vous avez perdu !",(0,-100),bold=True, color=(20,20,20))}]
player = Player() # Iitialise le joueur