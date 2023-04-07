import pygame
from ..screen import Screen

class Text(pygame.sprite.Sprite):
	def __init__(self, text:str=None, positions:tuple[int,int]=(0,0), font_size:int=30, bold:bool=False, color:tuple[int,int,int]=(255,240,0), back_col:tuple[int,int,int]=None) -> None:
		'''Permet de créer des textes
		
		text: texte à afficher
		position: décalage en pixels par rapport au milieu de l'écran
		font_size: taille de la police
		bold: gras ou pas
		color: couleur rgb du texte
		back_col: Couleur de fond du texte'''
		super().__init__()
		CharText= pygame.font.SysFont('arial', font_size, bold)
		self.text_str = text
		self.text = CharText.render(text,1 , color, back_col)
		self.rect = self.text.get_rect(center = Screen.get_rect().center)
		self.rect.x+=positions[0]
		self.rect.y+=positions[1]
	
	def show(self)-> None:
		'''Afiche le texte'''
		pygame.display.update(Screen.blit(self.text, self.rect))

	def text_Rect(self)->None:
		'''Crée la surface du texte dans le jeu'''
		Screen.blit(self.text, self.rect)