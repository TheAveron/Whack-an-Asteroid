from game_files import *

with open('data.json','r') as datafile:
	game_data=json.load(datafile)

game(monEcran, game_data)