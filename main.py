import pygame
from random import randint
import time

game_data={'width':800,'height':600,'jeu_en_cours':True,'clic':False, 'cycle':0,'cycle_lenght':600,'resultat':None}

pygame.init() #lancement de pygame

maPolice = pygame.font.SysFont('arial', 30) #Chargement de la police dans la variable maPolice
texteGagne = maPolice.render("Gagné",  1, (0,255,255))#Creation de l'étiquette "Gagné"
textePerdu = maPolice.render("Perdu",  1, (0,255,255))#Creation de l'étiquette "Perdu"

monEcran=pygame.display.set_mode((game_data['width'] ,game_data['height'])) #Affichage de la fenêtre

while game_data['jeu_en_cours']==True:
	
	if game_data['resultat']==None:
		pygame.display.update()
	#Rafraichissement de la fenêtre
	monEcran.fill((100,40,70))

	
	if game_data['cycle']%game_data['cycle_lenght']==0:
		cote=randint(20,200)
		posx=randint(cote,game_data['width']-cote)# width est la largeur de la fenétre
		posy=randint(cote,game_data['height']-cote)# height est la hauteur de la fenetre

	pygame.draw.rect(monEcran,(240,255,240),(posx,posy,cote,cote))
	
	mouseX,mouseY=pygame.mouse.get_pos()
	if game_data["clic"]:
		if mouseX>posx and mouseX<posx+cote and mouseY>posy and mouseY<posy+cote:
			game_data['resultat']=True
		else:
			game_data['resultat']=False

	#else:
	#	monEcran.blit(textePerdu,(game_data['width']%,game_data['height']%2))

	game_data['cycle']+=1 # Icrément de 1 à chaque itération du while

	# Gestions des évènements
	for evenement in pygame.event.get():
		if evenement.type == pygame.QUIT:
			pygame.quit()
			game_data['jeu_en_cours']=False
		
		if evenement.type==pygame.MOUSEBUTTONDOWN:#L'evénement est un clic sur la souris
			game_data['clic']=True
		else:
			game_data['clic']=False

	if game_data['resultat']==True:
		monEcran.blit(texteGagne, (game_data['width']*0.5,game_data['height']*0.5))
		pygame.display.update()
	elif game_data['resultat'] == False:
		monEcran.blit(textePerdu, (game_data['width']*0.5,game_data['height']*0.5))