import pygame
import json
from random import randint, choice

from .Sprites import *
from .screen import *


# Récupération des valeurs de la configuration du jeu
with open('data.json','r') as datafile:
	game_data:dict[bool | dict | int] = json.load(datafile)
	'''Données de configuation du jeu'''


Texts_menu:list[Text] = [Text('Play', (0,40), color = (42, 40, 57)), Text('Whack an Asteroid', (0,-200), 50, True, color = (42, 40, 57))]
'''Textes du menu de démarage'''
Texts_game:dict[Text] = {'Win':Text('Gagné'), 'Lose':Text('Perdu'),"Pause":Sprite("Pause", type ='Pause', position = (game_data['width']-66, 20), indexage = False)}
'''Textes de la partie'''
Texts_end:list[Text | dict[Text]] = [Text('Restart',(0,110),60, color=(42, 40, 57)),{"Win":Text("Congratulation you win !", (0,-100), 30, True, (42, 40, 57)), 'Lose':Text("You lose !", (0,-100), 50,True, (42, 40, 57))}]
'''Textes du menu de fin de jeu'''


Touch_sound = pygame.mixer.Sound('Static/Sounds/touch.wav')
'''Son de touche des sprites'''
Lose_sound = pygame.mixer.Sound('Static/Sounds/lose.wav')
'''Son de défaite'''
Win_sound = pygame.mixer.Sound('Static/Sounds/Win.wav') 
'''Son de victoire'''