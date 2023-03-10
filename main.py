import pygame
import json

with open('data.json','r') as datafile:
	game_data=json.load(datafile)

pygame.init() #lancement de pygame

# Police de caractère
maPolice = pygame.font.SysFont('arial', 30) #Chargement de la police dans la variable maPolice
texteGagne = maPolice.render("Gagné",  1, eval(game_data['text-color'])) #Creation de l'étiquette "Gagné"
textePerdu = maPolice.render("Perdu",  1, eval(game_data['text-color'])) #Creation de l'étiquette "Perdu"

# Création de l'environnement
monEcran=pygame.display.set_mode((game_data['width'] ,game_data['height'])) #Affichage de la fenêtre
