import pygame
from .global_var import Screen, game_data
from random import choice

SpritesImages= {'Little': ["static/Little_Ship.png",10],"Big": ['Static/Big_ship.png',30]}
# Classe des "Taupes"
class Taupe(pygame.sprite.Sprite):
	Taupes_list:list=[]
	Taupes_clicked_list:list=[]

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
	
	@classmethod
	def taupe_add(cls, taupe):
		'''Ajoute un taupe à la liste des taupes actuellement affichées'''
		cls.Taupes_list.append(taupe)
	
	@classmethod
	def taupe_remove(cls, taupe):
		'''Enlève un taupe à la liste des taupes actuellement affichées'''
		cls.Taupes_list.remove(taupe)
	
	@classmethod
	def taupe_clicked(cls, taupe):
		'''Ajoute un taupe à la liste des taupes actuellement clickées'''
		cls.Taupes_clicked_list.append(taupe)
		player.score_add(taupe.rewards)
		print(player.score)
	
	@classmethod
	def taupe_unclicked(cls, taupe):
		'''Enlève un taupe à la liste des taupes actuellement clickées'''
		cls.Taupes_clicked_list.remove(taupe)

class Text(pygame.sprite.Sprite):
	def __init__(self, text:str=None, positions:tuple=(0,0), font_size:int=30, bold:bool=False, color:tuple=(255,240,0), back_col:tuple=(0,0,0)) -> None:
		'''Permet de créer des boutons'''
		super().__init__()
		CharText= pygame.font.SysFont('arial', font_size, bold)
		self.text_str = text
		self.text = CharText.render(text,1 , color)
		self.rect = self.text.get_rect(center = Screen.get_rect().center)
		self.rect.x+=positions[0]
		self.rect.y+=positions[1]
	
	def show(self)-> None:
		'''Afiche le texte'''
		pygame.display.update(Screen.blit(self.text, self.rect))
		pygame.time.wait(300)


class Player:
	def __init__(self, score:int=0) -> None:
		'''initialise le score'''
		self.score_var=score
		self.level_var=0

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
		return str(self.level)

Texts_menu = [Text('Jouer',(0,40), color=(42, 40, 57)), Text('Jeu de la taupe',(0,-200),50,True,color=(42, 40, 57))]
Texts_game = {'Win':Text('Gagné'), 'Lose':Text('Perdu')}
player = Player()
