from .global_var import *
from .events import *

def end(player:Player)->None:
	'''Ecran d'affichage de fin'''


	with open("data.json","r") as f:
		data=json.load(f)
	with open('data.json','w') as f:
		if data['best_score']<player.score_max:
			data['best_score']=player.score_max
		json.dump(data, f , indent=4)

	game_data['jeu_en_cours']=True
	while game_data['jeu_en_cours']:
		if player.score_var < 0:
			player.lose_show()
		else:
			player.back_show()

		score_text=Text(f"meilleur score : {data['best_score']}",(0,-40),color=(20,20,20),bold=(True))
		score_text.text_Rect()

		score_text=Text(f"level : {player.level_var}",(0,0),color=(20,20,20),bold=(True))
		score_text.text_Rect()

		for text in Texts_end:
			if type(text)==dict:
				if game_data['resultat']==True: text['Win'].text_Rect()
				else: text['Lose'].text_Rect()
			else: text.text_Rect()

		pygame.display.update()
		events()
