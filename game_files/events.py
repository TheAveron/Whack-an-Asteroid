from .global_var import *

def events()->None:
	'''Fonction de détection des évènements'''
	for evenement in pygame.event.get():
		# Détection de la fermeture de la fenêtre
		if evenement.type == pygame.QUIT:
			game_data['jeu_en_cours']=False
			pygame.quit()
		
		game_data['clic_not_button']=False
		game_data['clicked_button_end']=False
		game_data['taupe_clicked']=False
		# Détection du clic de la souris
		if evenement.type==pygame.MOUSEBUTTONDOWN: #L'evénement est un clic sur la souris
			pos = pygame.mouse.get_pos() # Récupère la position de la souris
			for taupe in Taupe.Taupes_list: # Récupère tous les sprites qui sont en contact avec la souris
				if taupe.rect.collidepoint(pos):
					Taupe.taupe_clicked(taupe, player)
					game_data['taupe_clicked']=True
					
			game_data['clicked_button_menu']=[s for s in Texts_menu if s.rect.collidepoint(pos)] # Récupère tous les Text du menu qui sont en context avec la souris

			if Texts_end[0].rect.collidepoint(pos):
				game_data['clicked_button_end']=True

			if game_data['clicked_button_menu']==[] and game_data['taupe_clicked']==False:
				game_data['clic_not_button']=True