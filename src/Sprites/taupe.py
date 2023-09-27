from __future__ import annotations
import pygame
from random import choice

from .player import Player
from ..screen import Screen

SpritesImages: dict[str, tuple[str, int]] = {
    "Little_ship": ("Static/Images/Little_Ship.png", -10),
    "Big_ship": ("Static/Images/Big_ship.png", -30),
    "Little_asteroid": ("Static/Images/Little_Asteroid.png", 60),
    "Medium_asteroid": ("Static/Images/Medium_Asteroid.png", 30),
    "Big_Asteroid": ("Static/Images/Big_Asteroid.png", 15),
}
"""Dictionnaire de tous les types de sprites, leurs images et les points de base qui leurs sont attribués"""
Pause_button = "Static/Images/Pause.png"
"""Chemin d'accès de l'image du boutton de pause"""


# Classe des "sprites"
class Sprite(pygame.sprite.Sprite):
    Sprites_list: list[Sprite] = []
    """Liste des sprites actifs"""

    def __init__(
        self,
        name: str = "",
        cycle: int = 0,
        type: str = choice(list(SpritesImages.keys())),
        position: tuple[int, int] = (0, 0),
        indexage: bool = True,
    ) -> None:
        """Permet de créer un nouveau sprite

        name: le nom du sprite (non obligatoire et décoratif)
        cycle: le cycle ou à été crée le sprite
        type: le type de sprite qui doit être créé
        position: les coordonées x et y du centre du sprite qui va être créé
        indexage: défini si le sprite doit être ajouté à la liste"""

        # Vérifie si le type du sprite est correct
        assert (type == "Pause") | (
            type in SpritesImages.keys()
        ), f'type: {type} \ntype devrait être égal à une de ces valeurs : {list(SpritesImages.keys())} ou "Pause"'
        super().__init__()

        self.name: str = name
        """Nom du sprite"""
        self.cycle: int = cycle
        """Cycle auquel le sprite est créé"""
        self.type: str = type
        """Type du sprite"""

        if self.type != "Pause":
            self.rewards: int = SpritesImages[self.type][1]
            """Récompense positive ou négative en points lorsque l'on cliquera sur le sprite"""
            self.image: pygame.Surface = pygame.image.load(SpritesImages[self.type][0])
            """L'image du sprite"""
        else:
            self.image: pygame.Surface = pygame.image.load(Pause_button)

        self.rect: pygame.Rect = self.image.get_rect(center=Screen.get_rect().center)
        """Rectangle du sprite"""
        self.rect.x, self.rect.y = position

        if indexage:
            Sprite.sprite_add(self)

    def show(self) -> None:
        """Ajoute le sprite à l'écran"""
        Screen.blit(self.image, self.rect)

    def __repr__(self) -> str:
        """Représentation dans la console de l'objet"""
        return f"Sprite(\n\tname: {self.name}\n\tcycle: {self.cycle}\n\ttype: {self.type}\n\tposition: {self.rect.x,self.rect.y}\n)"

    def sprite_clicked(self, player: Player) -> None:
        """Suprime le sprite et ajoute le nombre de points qui lui correspondent, multiplié par le multiplicateur du niveau"""
        Sprite.sprite_remove(self)

        level_multiplier: float = float(
            ((4.3**player.level_var) * (1 / (player.level_var + 1))) ** (1 / 6)
        )
        """multiplicateur de points en fonction du niveau du jeu"""

        player.score_add(int(self.rewards * level_multiplier))

    @classmethod
    def sprite_add(cls, sprite: Sprite) -> None:
        """Ajoute la sprite à la liste des sprites"""
        cls.Sprites_list.append(sprite)

    @classmethod
    def sprite_remove(cls, sprite: Sprite) -> None:
        """Enlève la sprite de la liste des sprites et surpime définitivement l'objet"""
        cls.Sprites_list.remove(sprite)
        del sprite
