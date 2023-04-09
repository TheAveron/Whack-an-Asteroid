import pygame, json
# Lancement de pygame
pygame.init()

try:
	f=open('data.json')
	f.close()
except FileNotFoundError:
	with open('Static/Base_data/data_default.json',"r") as f1:
		data=json.load(f1)
		with open('data.json','w') as f2:
			json.dump(data, f2, indent=4)
from game_files import *

# Lancement du menu du jeu
menu()

