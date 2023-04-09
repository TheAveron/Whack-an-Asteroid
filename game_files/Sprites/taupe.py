import pygame
from random import choice

from ..screen import Screen

SpritesImages= {'Little_ship': ["Static/Little_Ship.png",-10],"Big_ship": ['Static/Big_ship.png',-30],'Little_asteroid':["Static/Little_Asteroid.png",60],'Medium_asteroid':["Static/Medium_Asteroid.png",30], 'Big_Asteroid':["Static/Big_Asteroid.png",15]}
Pause_button="Static/Pause.png"


# Classe des "Taupes"
class Taupe(pygame.sprite.Sprite):
	Taupes_list:list=[]

	def __init__(self, name:str=None, cycle:int=0,type:str=choice(list(SpritesImages.keys())), position:tuple[int, int]=(0,0), indexage:bool=True)->None:
		'''Permet de créer une "Taupe".
		
		name: un nom décoratif
		cycle: le cycle ou à été crée le sprite
		type: le type de taupe qui doit être créé
		position: les coordonées x et y du centre du sprite qui va être créé'''
		
		assert (type=="Pause") | (type in SpritesImages.keys()), (f'type: {type} \ntype devrait être égal à une de ces valeurs : {list(SpritesImages.keys())} ou "Pause"')
		super().__init__()
		
		self.name:str = name
		self.cycle:int = cycle
		
		self.type:str = type
		
		
		if self.type!="Pause":
			self.rewards:int = SpritesImages[self.type][1]
			self.image:pygame.Surface = pygame.image.load(SpritesImages[self.type][0])
		else:
			self.image:pygame.Surface = pygame.image.load(Pause_button)
		
		self.rect:pygame.Rect = self.image.get_rect(center = Screen.get_rect().center)
		self.rect.x, self.rect.y = position
		
		if indexage:
			Taupe.taupe_add(self)
	
	def show(self)->None:
		'''Affiche la taupe'''
		Screen.blit(self.image, self.rect)

	def __repr__(self)->str:
		'''représentation dans la console de l'objet'''
		return f"Taupe(\n\tname: {self.name}\n\tcycle: {self.cycle}\n\ttype: {self.type}\n\tposition: {self.rect.x,self.rect.y}\n)"
	
	def taupe_clicked(self, player)->None:
		'''Ajoute un taupe à la liste des taupes actuellement clickées'''
		Taupe.taupe_remove(self)
		level_multiplier = ((4.3**player.level_var ) * (1/(player.level_var+1)))**(1/6)
		player.score_add(int(self.rewards*level_multiplier))
	
	@classmethod
	def taupe_add(cls, taupe)->None:
		'''Ajoute un taupe à la liste des taupes actuellement affichées'''
		cls.Taupes_list.append(taupe)
	
	@classmethod
	def taupe_remove(cls, taupe)->None:
		'''Enlève un taupe à la liste des taupes actuellement affichées'''
		cls.Taupes_list.remove(taupe)
		del taupe


