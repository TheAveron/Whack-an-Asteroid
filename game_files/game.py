import pygame
from random import randint, choice

from .events import events
from .end_screen import end
from .sprites import *
from .global_var import Screen, game_data, Background, B_rect

occ=0
def game()->None:
	'''Fonction principale du jeu'''
	global occ
	pygame.display.flip()
	
	game_data['jeu_en_cours']=True
	game_data['cycle']=0 # Nombre de cycles effectués
	while game_data['jeu_en_cours']:
		Screen.blit(Background, B_rect)
		#génération de carré lorsque l'on a terminé le nombre de cycle requis
		if game_data['cycle']%game_data['cycle_lenght']==0:
			for sprite in Taupe.Taupes_list:
				if sprite.cycle == game_data['cycle']-game_data['cycle_lenght']:
					Taupe.taupe_remove(sprite)
			Taupe(type=choice(list(SpritesImages.keys())), cycle=game_data['cycle'], position=(randint(0,1700), randint(0,800)))
		
		for sprite in Taupe.Taupes_list:
			sprite.show()

		if Taupe.Taupes_clicked_list == [] and game_data['clic']:
			Texts_game['Lose'].show()
			game_data['cycle']+=game_data['cycle']%game_data['cycle_lenght']
			player.score_var-=10

		for sprite in Taupe.Taupes_clicked_list:
			Taupe.taupe_unclicked(sprite)
			Taupe.taupe_remove(sprite)
			Texts_game['Win'].show()

		game_data['cycle']+=1
		score_text=Text(player.score(), positions=(-850,-480))
		Screen.blit(score_text.text, score_text.rect)
		
		print(game_data['cycle'])
		pygame.display.update()
		events()

		if player.score_var<0:
			break

	end()

