import pygame
import json

# Récupération de la configuration de base du jeu
with open('data.json','r') as datafile:
	game_data=json.load(datafile)

# Création de l'environnement
Screen = pygame.display.set_mode((game_data['width'] ,game_data['height'])) # Définition de la taille de la fenêtre
pygame.display.set_caption('Jeu de la taupe') # Définition du titre de la fenêtre