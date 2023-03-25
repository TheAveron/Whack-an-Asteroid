import pygame
from .global_var import Screen


SpritesImages= {'Little': "static/Little_Ship.png","Big": 'Static/Big_ship.png'}
# Classe des "Taupes"
class Taupe(pygame.sprite.Sprite):
	def __init__(self, type:str, name:str, position:tuple=(0,0))->None:
		'''Permet de créer une "Taupe" '''
		super().__init__()

		self.rewards=int()
		self.type = type
		self.image = pygame.image.load(SpritesImages[type])
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = position
		print(self.rect)
		self.name = name
	
	def __repr__(self)->str:
		return f"Taupe {self.name}, type: {self.type}"
		

class Text(pygame.sprite.Sprite):
	def __init__(self, text:str, positions:tuple=(0,0), font_size:int=30, bold:bool=False) -> None:
		'''Permet de créer des boutons'''
		super().__init__()
		CharText= pygame.font.SysFont('arial', font_size, bold)
		self.text_str = text
		self.text = CharText.render(text,1 , (255,240,0))
		self.rect = self.text.get_rect(center = Screen.get_rect().center)
		self.rect.x+=positions[0]
		self.rect.y+=positions[1]

sprites = []
Texts_menu = [Text('Jouer',(0,40)), Text('Jeu de la taupe',(0,-200),50,True)]

