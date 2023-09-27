import pygame
from .events import events
from .game import game

from .global_var import *


def menu() -> None:
    """Menu de démarage du jeu"""

    # Boucle d'affichage du menu
    while game_data["jeu_en_cours"]:
        # Affichage du fond
        Screen.blit(
            pygame.image.load("Static/Images/earth_pix.jpg"),
            pygame.image.load("Static/Images/earth_pix.jpg").get_rect(
                center=Screen.get_rect().center
            ),
        )

        # Affichage de tous les textes du menu
        for Text in Texts_menu:
            Screen.blit(Text.text, Text.rect)

        # Quitte le menu si le bouton "Play" est cliqué
        for text in game_data["clicked_button_menu"]:
            if text.text_str == "Play":
                # Permet de quitter la boucle while parente
                game_data["jeu_en_cours"] = False
            game_data["clicked_button_menu"].remove(text)

        pygame.display.update()  # Actualise l'affichage
        events()

    # Lance le jeu
    while True:
        # Vérifie si pygame est toujours en cours de fonctionnement
        try:
            game()
        except:
            break
