import pygame, json

with open('data.json','r') as datafile:
	game_data=json.load(datafile)

Screen = pygame.display.set_mode((game_data['width'] ,game_data['height'])) # Création de la fenêtre