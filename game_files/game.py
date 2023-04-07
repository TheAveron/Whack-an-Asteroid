from .screen import *
from .global_var import *
from .events import events
from .end_screen import end

occ=0
def game()->None:
	'''Fonction principale du jeu'''
	global occ
	pygame.display.flip()
	
	game_data['jeu_en_cours']=True
	game_data['cycle']=0 # Nombre de cycles effectués

	while game_data['jeu_en_cours']:
		player.back_show()
		#génération de carré lorsque l'on a terminé le nombre de cycle requis
		if game_data['cycle']%game_data['cycle_lenght']==0:
			for sprite in Taupe.Taupes_list:
				if sprite.cycle == game_data['cycle']-game_data['cycle_lenght']:
					Taupe.taupe_remove(sprite)
			Taupe(type=choice(list(SpritesImages.keys())), cycle=game_data['cycle'], position=(randint(0,1700), randint(0,800)))
		
		for sprite in Taupe.Taupes_list:
			sprite.show()

		if game_data['clic_not_button'] and Taupe.Taupes_list!=[]:
			Texts_game['Lose'].show()
			game_data['cycle']+=game_data['cycle']%game_data['cycle_lenght']
			player.score_var-=10

		game_data['cycle']+=1
		print(game_data['cycle'])


		score_text=Text(player.score(), positions=(-850,-480))
		Screen.blit(score_text.text, score_text.rect)

		events()
		pygame.display.update()

		if player.score_var<0:
			game_data['resultat']=False
			game_data['jeu_en_cours']=False
		elif player.level_var==20:
			game_data['resultat']=True
			game_data['jeu_en_cours']=False

	end()

