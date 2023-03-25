from .global_var import Screen, game_data
from .events import *

def end()->None:
    '''Ecran d'affichage de fin'''
    Screen.fill(eval(game_data['back-color']))
    pygame.display.flip()

    CharArial= pygame.font.SysFont('arial', 30)
    game_data['jeu_en_cours']=True
    while game_data['jeu_en_cours']:
        textePoints=CharArial.render(str(game_data['score']),1 , eval(game_data['text-color']))
        Screen.blit(textePoints, textePoints.get_rect(center = Screen.get_rect().center))
        events(game_data)
        pygame.display.update()