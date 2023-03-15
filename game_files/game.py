import pygame
import json
from random import randint

from .events import *
from .global_var import texteGagne, textePerdu
from .end_screen import *

occ=0
def game(ecran:pygame.Surface, game_data):
	global occ
	
	game_data['jeu_en_cours']=True
	game_data['cycle']=0
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
				game_data['score']+=1
			else:
				game_data['resultat']=False
			

		game_data['cycle']+=1
		ecran.blit(maPolice.render(str(game_data['score']),1 , eval(game_data['text-color'])), (10,10))
		events(game_data)
		pygame.display.update() #Rafraichissement de la fenêtre
	
	
	if game_data['resultat']==True:
		ecran.blit(texteGagne, texteGagne.get_rect(center = ecran.get_rect().center))
		pygame.display.update()
	elif game_data['resultat']==False:
		ecran.blit(textePerdu, textePerdu.get_rect(center = ecran.get_rect().center))
		pygame.display.update()
	
	pygame.time.delay(10)
	print("waiting ! ")
	occ+=1
	if occ<100:game(ecran, game_data)
	else:end(ecran, game_data)

