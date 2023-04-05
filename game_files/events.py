import pygame
from .sprites import *
from .global_var import game_data

def events()->None:
	'''Fonction de détection des évènements'''
	for evenement in pygame.event.get():
		# Détection de la fermeture de la fenêtre
		if evenement.type == pygame.QUIT:
			game_data['jeu_en_cours']=False
			pygame.quit()
		
		game_data['clic']=False
		# Détection du clic de la souris
		if evenement.type==pygame.MOUSEBUTTONDOWN: #L'evénement est un clic sur la souris
			pos = pygame.mouse.get_pos() # Récupère la position de la souris
			for taupe in Taupe.Taupes_list: # Récupère tous les sprites qui sont en contact avec la souris
				if taupe.rect.collidepoint(pos):
					Taupe.taupe_clicked(taupe)
					
			game_data['clicked_button_menu']=[s for s in Texts_menu if s.rect.collidepoint(pos)] # Récupère tous les text qui sont en context avec la souris
			if game_data['clicked_button_menu']==[]:
				game_data['clic']=True