import pygame
from ..screen import Screen

class Player:
	def __init__(self, score:int=0) -> None:
		'''initialise le score'''
		self.score_var=score
		self.level_var=0

		# Récupération de l'image de fond
		self.game_back_img=pygame.image.load('Static/earth_pix2.jpg')
		self.game_back_rect=self.game_back_img.get_rect(center=Screen.get_rect().center)

		# Récupération de l'image de défaite
		self.game_lose_img=pygame.image.load('Static/earth_lose_pix.jpg')
		self.game_lose_rect=self.game_lose_img.get_rect(center=Screen.get_rect().center)

	def score_add(self, amout:int=10)->None:
		'''Ajoute amout à la valeur du score'''
		self.score_var+=amout

	def score_sub(self, amout:int=10)->None:
		'''Soustrait amout à la valeur du score'''
		self.score_var-=amout

	def score(self)->str:
		'''Retourne la valeur du score sous forme de str'''
		return str(self.score_var)
	
	def level(self)->str:
		'''Retourne la valeur du niveau sous forme de str'''
		return str(self.level_var)

	def back_show(self)->None:
		'''Retourne le fond du jeu'''
		Screen.blit(self.game_back_img, self.game_back_rect)
	
	def lose_show(self)->None:
		'''Retourne le fond de défaite'''
		Screen.blit(self.game_lose_img, self.game_lose_rect)

