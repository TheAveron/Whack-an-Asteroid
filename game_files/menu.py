import pygame
from .events import events
from .game import game

from .global_var import *

def menu()->None:
	'''Menu de démarage du jeu'''
	
	# Boucle d'affichage du menu
	while game_data['jeu_en_cours']:
		# Affichage du fond
		player.back_show()
		
		# Affichage de tous les textes
		for Text in Texts_menu:
			Screen.blit(Text.text, Text.rect)

		# Quitte le menu si le bouton "Jouer" est cliqué
		for text in game_data['clicked_button_menu']:
			if text.text_str == 'Jouer':
				game_data['jeu_en_cours']=False
			game_data['clicked_button_menu'].remove(text)

		pygame.display.update()
		events()

	# Lance le jeu
	while True:
		pygame.display.update()
		game()