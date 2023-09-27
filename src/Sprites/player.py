import pygame
from ..screen import Screen


class Player:
    def __init__(self, score: int = 0) -> None:
        """initialise le joueur

        score: score de départ"""

        self.score_var: int = score
        """Score du joueur"""
        self.score_max: int = score
        """Score maximal atteint par le joueur lors de la partie en cours"""
        self.level_var: int = 0
        """niveau du joureur"""
        self.cycle: int = 0
        """Cycle de jeu"""
        self.cycle_lenght: int = int(round(400 * (0.94**self.level_var)))
        """Longueur d'un cycle de jeu avant l'appartition d'un nouveau sprite"""

        # Récupération de l'image de fond
        self.game_back_img: pygame.Surface = pygame.image.load(
            "Static/Images/earth_pix2.jpg"
        )
        """Image du fond du jeu"""
        self.game_back_rect: pygame.Rect = self.game_back_img.get_rect(
            center=Screen.get_rect().center
        )
        """Rectangle de l'image du fond"""

        # Récupération de l'image de défaite
        self.game_lose_img: pygame.Surface = pygame.image.load(
            "Static/Images/earth_lose_pix.jpg"
        )
        """Image du fond de défaite du jeu"""
        self.game_lose_rect: pygame.Rect = self.game_lose_img.get_rect(
            center=Screen.get_rect().center
        )
        """Rectangle de l'image de fond de défaite"""

    def score_add(self, amout: int = 10) -> None:
        """Ajoute amout à la valeur du score"""
        self.score_var += amout
        if self.score_var > self.score_max:
            self.score_max = self.score_var

    def score_sub(self, amout: int = 10) -> None:
        """Soustrait amout (nombre de points) à la valeur du score"""
        self.score_var -= amout

    def score(self) -> str:
        """Retourne la valeur du score sous forme de str"""
        return str(self.score_var)

    def check_level(self) -> None:
        """vérifie et met à jour le niveau du jeu"""
        if 4.3**self.level_var < self.score_var:
            self.level_var += 1
            self.cycle_lenght = int(round(400 * (0.94**self.level_var)))

    def level(self) -> str:
        """Retourne la valeur du niveau sous forme de str"""
        return str(self.level_var)

    def back_show(self) -> None:
        """Initialise le fond du jeu dans l'affichage"""
        Screen.blit(self.game_back_img, self.game_back_rect)

    def lose_show(self) -> None:
        """Initialise le fond de défaite dans l'affichage"""
        Screen.blit(self.game_lose_img, self.game_lose_rect)
