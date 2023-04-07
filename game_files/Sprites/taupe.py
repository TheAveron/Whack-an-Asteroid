import pygame
from random import choice

from ..screen import Screen

SpritesImages= {'Little': ["static/Little_Ship.png",10],"Big": ['Static/Big_ship.png',-30]}


# Classe des "Taupes"
class Taupe(pygame.sprite.Sprite):
	Taupes_list:list=[]

	def __init__(self, name:str=None, cycle:int=0,type:str=choice(['Little','Big']), position:tuple[int, int]=(0,0))->None:
		'''Permet de créer une "Taupe".
		
		name: un nom décoratif
		cycle: le cycle ou à été crée le sprite
		type: le type de taupe qui doit être créé
		position: les coordonées x et y du centre du sprite qui va être créé'''
		assert type in SpritesImages.keys(), (f'type: {type} \ntype devrait être égal à une de ces valeurs : {SpritesImages.keys}')

		super().__init__()

		self.name:str = name
		self.cycle:int = cycle
		self.type:str = type
		self.image:pygame.Surface = pygame.image.load(SpritesImages[self.type][0])
		self.rewards:int = SpritesImages[self.type][1]
		self.rect:pygame.Rect = self.image.get_rect(center = Screen.get_rect().center)
		self.rect.x, self.rect.y = position
		
		Taupe.taupe_add(self)
	
	def show(self):
		'''Affiche la taupe'''
		pygame.display.update(Screen.blit(self.image, self.rect))

	def __repr__(self)->str:
		'''représentation dans la console de l'objet'''
		return f"Taupe(\n\tname: {self.name}\n\tcycle: {self.cycle}\n\ttype: {self.type}\n\tposition: {self.rect.x,self.rect.y}\n)"
	
	def taupe_clicked(self, player)->None:
		'''Ajoute un taupe à la liste des taupes actuellement clickées'''
		Taupe.taupe_remove(self)
		player.score_add(self.rewards)
	
	@classmethod
	def taupe_add(cls, taupe)->None:
		'''Ajoute un taupe à la liste des taupes actuellement affichées'''
		cls.Taupes_list.append(taupe)
	
	@classmethod
	def taupe_remove(cls, taupe)->None:
		'''Enlève un taupe à la liste des taupes actuellement affichées'''
		cls.Taupes_list.remove(taupe)
		del taupe


