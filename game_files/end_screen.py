from .global_var import *
from .events import *
def end(ecran:pygame.surface, game_data):
    ecran.fill(eval(game_data['back-color']))
    game_data['jeu_en_cours']=True
    while game_data['jeu_en_cours']:
        textePoints=maPolice.render(str(game_data['score']),1 , eval(game_data['text-color']))
        ecran.blit(textePoints, textePoints.get_rect(center = ecran.get_rect().center))
        events(game_data)
        pygame.display.update()

