import pygame
import json
from random import randint, choice

from .Sprites import *
from .screen import *


# Récupération des valeurs de la configuration de base du jeu
with open('data.json','r') as datafile:
	game_data:dict[bool | dict | int]=json.load(datafile)


pygame.display.set_caption('Whack an asteroid') # Définition du titre de la fenêtre

Texts_menu:list[Text] = [Text('Play',(0,40), color=(42, 40, 57)), Text('Whack an Asteroid',(0,-200),50,True,color=(42, 40, 57))] # Crée les textes du menu du jeu
Texts_game:dict[Text] = {'Win':Text('Gagné'), 'Lose':Text('Perdu'),"Pause":Taupe("Pause",type='Pause',position=(game_data['width']-66,20),indexage=False)} # Crée les textes pour les victoires et défaites
Texts_end:list[Text | dict[Text]]  = [Text('Restart',(0,110),60, color=(42, 40, 57)),{"Win":Text("Congratulation you win !",(0,-100),30,True,(42, 40, 57)), 'Lose':Text("You lose !",(0,-100), 50,True,(42, 40, 57))}] # Crée les textes du menu de fin


Touch_sound=pygame.mixer.Sound('Static/Sounds/touch.wav')
Lose_sound=pygame.mixer.Sound('Static/Sounds/lose.wav')
Win_sound=pygame.mixer.Sound('Static/Sounds/Win.wav')