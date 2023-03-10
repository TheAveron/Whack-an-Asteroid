import pygame
import json
from random import randint

from .events import *
from global_var import texteGagne, textePerdu

with open('data.json','r') as datafile:
	game_data=json.load(datafile)

def game(ecran:pygame.Surface):
	while game_data['jeu_en_cours']:
		
		ecran.fill(eval(game_data['back-color']))
		#génération de carré lorsque l'on a terminé un cycle
		if game_data['cycle']%game_data['cycle_lenght']==0:
			cote=randint(20,200)
			posx=randint(cote,game_data['width']-cote)
			posy=randint(cote,game_data['height'])

		pygame.draw.rect(ecran,eval(game_data['Hit_box-color']),(posx,posy,cote,cote))
		mouseX,mouseY=pygame.mouse.get_pos()
		
		if game_data['clic']:
			game_data['jeu_en_cours']=False
			if mouseX>posx and mouseX<posx+cote and mouseY>posy and mouseY<posy+cote:
				game_data["resultat"]=True
			else:
				game_data['resultat']=False

		game_data['cycle']+=1

		events(game_data)
		pygame.display.update() #Rafraichissement de la fenêtre
	
	game_data["jeu_en_cours"]=True
	while game_data['jeu_en_cours']:
		if game_data['resultat']==True:
			ecran.blit(texteGagne, (game_data['width']*0.5,game_data['height']*0.5))
			pygame.display.update()
		elif game_data['resultat']==False:
			ecran.blit(textePerdu, (game_data['width']*0.5,game_data['height']*0.5))
			pygame.display.update()
		
		events(game_data)

