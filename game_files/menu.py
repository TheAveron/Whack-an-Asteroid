import pygame
from .events import events
from .game import game
from .sprites import *
from .global_var import Screen, game_data, Background, B_rect

def menu()->None:
	'''Menu de démarage du jeu'''
	
	# Affichage du fond
	
	# Boucle du jeu
	while game_data['jeu_en_cours']:
		Screen.blit(Background, B_rect)
		# Affichage de tous les textes
		for Text in Texts_menu:
			Screen.blit(Text.text, Text.rect)

		# Quitte le menu si le bouton "Jouer" est cliqué
		for text in game_data['clicked_button_menu']:
			if text.text_str == 'Jouer':
				game_data['jeu_en_cours']=False
			game_data['clicked_button_menu'].remove(text)

		pygame.display.flip()
		events()

	# Lance le jeu
	game()
		