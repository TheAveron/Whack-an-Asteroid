import pygame, json

# récupération des données du jeu
with open("data.json", "r") as datafile:
    game_data = json.load(datafile)

Screen: pygame.Surface = pygame.display.set_mode(
    (game_data["width"], game_data["height"])
)
"""Fenêtre du jeu"""
pygame.display.set_caption("Whack an asteroid")  # Définition du titre de la fenêtre
