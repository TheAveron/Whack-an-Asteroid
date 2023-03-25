import pygame
from .sprites import *
from global_var import game_data

def events()->None:
	'''Fonction de détection des évènements'''
	for evenement in pygame.event.get():
		# Détection de la fermeture de la fenêtre
		if evenement.type == pygame.QUIT:
			pygame.quit()
			game_data['jeu_en_cours']=False
		
		# Détection du clic
		if evenement.type==pygame.MOUSEBUTTONDOWN: #L'evénement est un clic sur la souris
			pos = pygame.mouse.get_pos()
			game_data['clicked_sprites']=[s for s in sprites if s.rect.collidepoint(pos)]+[s for s in Texts_menu if s.rect.collidepoint(pos)]
