from .global_var import *

def events(player:Player = None) -> None:
	'''Fonction de détection des évènements'''
	for evenement in pygame.event.get():
		# Détection de la fermeture de la fenêtre
		if evenement.type == pygame.QUIT:
			game_data['jeu_en_cours'] = False
			pygame.quit()

		game_data['clicked_button_end'] = False
		game_data['sprite_clicked'] = False
		# Détection du clic de la souris
		if evenement.type == pygame.MOUSEBUTTONDOWN: #L'evénement est un clic sur la souris
			pos = pygame.mouse.get_pos() # Récupère la position de la souris
			if Texts_game['Pause'].rect.collidepoint(pos):
				# Active ou déscactive la pause quand le joueur clique dessus
				if not game_data['pause']:
					game_data['pause'] = True
					pause_text = Text('Jeu en Pause', (0,0), 50, True, (42, 40, 57))
					'''Texte de pause'''
					pause_text.show()
				else:
					game_data['pause'] = False
			
			if not game_data['pause']:
				# Effectue tous les evènements normaux du jeu si celui-ci n'est pas en pause (si oui  tout est figé)
				for sprite in Sprite.Sprites_list: # Récupère tous les sprites qui sont en contact avec la souris
					if sprite.rect.collidepoint(pos):
						# Vérifie si un sprite est touché
						Sprite.sprite_clicked(sprite, player)
						game_data['sprite_clicked'] = True
						Touch_sound.play()
						
				game_data['clicked_button_menu'] = [s for s in Texts_menu if s.rect.collidepoint(pos)] # Récupère tous les textes du menu qui sont en context avec la souris

				if Texts_end[0].rect.collidepoint(pos):
					# Stope la boucle du menu de fin ce qui relance une partie (nouvelle itération dans la boucle `while True` située dans le menu)
					game_data['jeu_en_cours']=False


			