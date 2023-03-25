import pygame
import json
from random import randint

from .events import *
from .end_screen import *
from .sprites import *
from .global_var import Screen, game_data

occ=0
def game()->None:
	'''Fonction principale du jeu, contient les cycles  de jeu, et la détection des zones cliquées'''
	global occ
	
	# Police de caractère
	CharArial= pygame.font.SysFont('arial', 30) #Chargement de la police dans la variable maPolice
	TextWin = CharArial.render("Gagné",  1, eval(game_data['text-color'])) #Creation de l'étiquette "Gagné"
	TextLose = CharArial.render("Perdu",  1, eval(game_data['text-color'])) #Creation de l'étiquette "Perdu"

	game_data['jeu_en_cours']=True
	game_data['cycle']=0 # Nombre de cycles effectués

	while game_data['jeu_en_cours']:
		Screen.fill(eval(game_data['back-color']))

		#génération de carré lorsque l'on a terminé le nombre de cycle requis
		if game_data['cycle']%game_data['cycle_lenght']==0:
			cote=randint(20,200)
			posx=randint(cote,game_data['width']-cote)
			posy=randint(cote,game_data['height'])

		pygame.draw.rect(Screen,eval(game_data['Hit_box-color']),(posx,posy,cote,cote))
		mouseX,mouseY=pygame.mouse.get_pos()
		
		# Action en fonction du clic
		if game_data['clic']:
			game_data['jeu_en_cours']=False
			if mouseX>posx and mouseX<posx+cote and mouseY>posy and mouseY<posy+cote:
				# Le joueur a bien cliqué sur une taupe
				game_data["resultat"]=True
				game_data['score']+=1
			else:
				# Le joueur à cliqué à côté d'une taupe
				game_data['resultat']=False
			

		game_data['cycle']+=1
		Screen.blit(CharArial.render(str(game_data['score']),1 , eval(game_data['text-color'])), (10,10))
		events(game_data)
		pygame.display.update()
	
	
	if game_data['resultat']==True:
		Screen.blit(TextWin, TextWin.get_rect(center = Screen.get_rect().center))
		pygame.display.update()
	elif game_data['resultat']==False:
		Screen.blit(TextLose, TextLose.get_rect(center = Screen.get_rect().center))
		pygame.display.update()
	
	game_data['resultat']=None
	pygame.time.delay(1000)
	print("waiting ! ")
	occ+=1
	if occ<100:game(Screen, game_data)
	else:end(Screen, game_data)

