import pygame
from random import randint
import json

with open('data.json','r') as datafile:
	game_data=json.load(datafile)

pygame.init() #lancement de pygame

# Police de caractère
maPolice = pygame.font.SysFont('arial', 30) #Chargement de la police dans la variable maPolice
texteGagne = maPolice.render("Gagné",  1, (0,255,255)) #Creation de l'étiquette "Gagné"
textePerdu = maPolice.render("Perdu",  1, (0,255,255)) #Creation de l'étiquette "Perdu"

# Création de l'environnement
monEcran=pygame.display.set_mode((game_data['width'] ,game_data['height'])) #Affichage de la fenêtre


def menu():
	pass


def game():
	while game_data['jeu_en_cours']:
		
		monEcran.fill((100,40,70))
		#génération de carré lorsque l'on a terminé un cycle
		if game_data['cycle']%game_data['cycle_lenght']==0:
			cote=randint(20,200)
			posx=randint(cote,game_data['width']-cote)
			posy=randint(cote,game_data['height'])

		pygame.draw.rect(monEcran,(240,255,240),(posx,posy,cote,cote))
		mouseX,mouseY=pygame.mouse.get_pos()
		
		if game_data['clic']:
			game_data['jeu_en_cours']=False
			if mouseX>posx and mouseX<posx+cote and mouseY>posy and mouseY<posy+cote:
				game_data["resultat"]=True
			else:
				game_data['resultat']=False

		game_data['cycle']+=1

		events()
		pygame.display.update() #Rafraichissement de la fenêtre
	
	game_data["jeu_en_cours"]=True
	while game_data['jeu_en_cours']:
		if game_data['resultat']==True:
			monEcran.blit(texteGagne, (game_data['width']*0.5,game_data['height']*0.5))
			pygame.display.update()
		elif game_data['resultat']==False:
			monEcran.blit(textePerdu, (game_data['width']*0.5,game_data['height']*0.5))
			pygame.display.update()
		
		events()

def events():
	for evenement in pygame.event.get():
		if evenement.type == pygame.QUIT:
			pygame.quit()
			game_data['jeu_en_cours']=False
		
		if evenement.type==pygame.MOUSEBUTTONDOWN: #L'evénement est un clic sur la souris
			game_data['clic']=True
		else:
			game_data['clic']=False

game()