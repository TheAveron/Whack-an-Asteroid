from .global_var import *
from .events import *

def end()->None:
	'''Ecran d'affichage de fin'''

	game_data['jeu_en_cours']=True
	while game_data['jeu_en_cours']:
		if player.score_var < 0:
			player.lose_show()
		else:
			player.back_show()

		score_text=Text(player.score(),(0,-60),color=(20,20,20),bold=(True))
		score_text.text_Rect()

		for text in Texts_end:
			if type(text)==dict:
				if game_data['resultat']==True: text['Win'].text_Rect()
				else: text['Lose'].text_Rect()
			else: text.text_Rect()

		"""if game_data['clicked_button_end']:
			game_data['jeu_en_cours']=False"""

		pygame.display.update()
		events()
