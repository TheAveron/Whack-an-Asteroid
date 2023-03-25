import pygame
from .events import *
from .game import *

def menu(game_data:dict)->None:
	'''Menu de démarage du jeu'''
	
	Background = pygame.image.load('Static/earth2.jpg')

	while game_data['jeu_en_cours']:
		Screen.blit(Background,(0,0))
		
		for sprite in sprites:
			Screen.blit(sprite.image, sprite.rect)
		for Text in Texts_menu:
			Screen.blit(Text.text, Text.rect)

		for text in game_data['clicked_sprites']:
			print('1')
			try:
				if text.text_str == 'Jouer':
					print('2')
					game_data['jeu_en_cours']=False
			except:
				print("2.5")
				pass

		pygame.display.update()
		events(game_data)

	game(Screen, game_data)
		