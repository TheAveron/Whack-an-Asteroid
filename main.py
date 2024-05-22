import sys

assert sys.version_info >= (
    3,
    10,
), "Python doit être mis à jour vers la version 3.10 ou plus pour pouvoir lancer le jeu"

import json
import pygame

# Lancement de pygame
pygame.init()

# Vérification de si c'est la première fois que le jeu est lancé
try:
    # Si ce n'est pas la première fois, un fichier "data.json" devrai exister
    f = open("data.json")
    f.close()
except FileNotFoundError:
    # Si le fichier n'existe pas, c'est que c'est la première fois que le jeu est lancé, ainsi on charge les données par défaut
    with open("Static/Base_data/data_default.json", "r") as f1:
        data = json.load(f1)
        with open("data.json", "w") as f2:
            json.dump(data, f2, indent=4)

from src import *

# Lancement du menu du jeu
from src.menu import menu

menu()
