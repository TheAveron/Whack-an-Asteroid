import pygame

def events(game_data):
	for evenement in pygame.event.get():
		if evenement.type == pygame.QUIT:
			pygame.quit()
			game_data['jeu_en_cours']=False
		
		if evenement.type==pygame.MOUSEBUTTONDOWN: #L'evénement est un clic sur la souris
			game_data['clic']=True
		else:
			game_data['clic']=False
