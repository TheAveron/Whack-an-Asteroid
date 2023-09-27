import pygame
from ..screen import Screen


class Text(pygame.sprite.Sprite):
    def __init__(
        self,
        text: str = "",
        positions: tuple[int, int] = (0, 0),
        font_size: int = 30,
        bold: bool = False,
        color: tuple[int, int, int] = (255, 240, 0),
        back_col: tuple[int, int, int] | None = None,
        fixed: bool = False,
    ) -> None:
        """Permet de créer des textes

        text: texte à afficher
        position: décalage en pixels par rapport au milieu de l'écran
        font_size: taille de la police
        bold: gras ou pas
        color: couleur rgb du texte
        back_col: Couleur de fond du texte
        fixed: détermine si le texte doit se en fonction du centre de la fenêtre ou le bord haut gauche
        """

        super().__init__()  # Iitialise la classe parente
        CharText = pygame.font.SysFont("arial", font_size, bold)
        """Police de caractère du texte"""

        self.text_str: str = text
        """Le text sous forme de str"""
        self.text: pygame.Surface = CharText.render(text, 1, color, back_col)
        """Le contenu qui sera affiché"""
        self.rect = self.text.get_rect(center=Screen.get_rect().center)
        """Le positionnement du texte et sa taille"""

        if fixed:
            self.rect.x = positions[0]
            self.rect.y = positions[1]
        else:
            self.rect.x += positions[0]
            self.rect.y += positions[1]

    def show(self) -> None:
        """Afiche le texte"""
        pygame.display.update(Screen.blit(self.text, self.rect))

    def text_Rect(self) -> None:
        """Ajoute la surface du text à l'écran"""
        Screen.blit(self.text, self.rect)
