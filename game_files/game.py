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
	player=Player() # initialise le joueur

	while game_data['jeu_en_cours']:
		if not game_data['pause']:
			player.back_show()
			player.check_level()

			#génération de carré lorsque l'on a terminé le nombre de cycles requis
			if player.cycle%player.cycle_lenght==0:
				for sprite in Taupe.Taupes_list:
					if sprite.cycle == player.cycle-player.cycle_lenght:
						Taupe.taupe_remove(sprite)
				Taupe(type=choice(list(SpritesImages.keys())), cycle=player.cycle, position=(randint(0,1700), randint(0,800)))
			
			for sprite in Taupe.Taupes_list:
				sprite.show()


			Texts_game['Pause'].show()

			player.cycle+=1

			score_text=Text(f'Score : {player.score()}', positions=(-850,-480))
			Screen.blit(score_text.text, score_text.rect)

			score_text=Text(f'Level : {player.level()}', positions=(-860,-450))
			Screen.blit(score_text.text, score_text.rect)

			pygame.display.update()

		events(player)
		
		if player.score_var<0:
			game_data['resultat']=False
			game_data['jeu_en_cours']=False
		elif player.level_var==20:
			game_data['resultat']=True
			game_data['jeu_en_cours']=False

	try:
		end(player)
	except:
		pass

