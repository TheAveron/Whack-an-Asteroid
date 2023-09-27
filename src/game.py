from .screen import *
from .global_var import *
from .events import events
from .end_screen import end

occ = 0

def game() -> None:
    """Fonction principale du jeu"""
    global occ
    pygame.display.flip()

    game_data["jeu_en_cours"] = True
    player = Player()
    """Joueur"""

    # Chargment et lancement de la musique
    pygame.mixer.music.load("Static/Sounds/fight.mp3")
    pygame.mixer.music.play(-1)

    while game_data["jeu_en_cours"]:
        if not game_data["pause"]:
            player.back_show()
            player.check_level()

            # génération d'un nouveau sprite lorsque l'on a terminé le nombre de cycles requis
            if player.cycle % player.cycle_lenght == 0:
                for sprite in Sprite.Sprites_list:
                    if sprite.cycle == player.cycle - player.cycle_lenght:
                        Sprite.sprite_remove(sprite)
                Sprite(
                    type=choice(list(SpritesImages.keys())),
                    cycle=player.cycle,
                    position=(randint(0, 1700), randint(0, 800)),
                )

            # Affichage de tous les sprites de la liste de ceux qui doivent être affichés
            for sprite in Sprite.Sprites_list:
                sprite.show()

            Texts_game["Pause"].show()

            player.cycle += 1

            score_text = Text(
                f"Score : {player.score()}", positions=(20, 20), fixed=True
            )
            """Texte du score"""
            Screen.blit(score_text.text, score_text.rect)

            level_text = Text(
                f"Level : {player.level()}", positions=(20, 50), fixed=True
            )
            """texte du niveau"""
            Screen.blit(level_text.text, level_text.rect)

            pygame.display.update()

        events(player)

        if player.score_var < 0:
            # Si le joueur à moins de 0 points, il perd
            game_data["resultat"] = False
            game_data["jeu_en_cours"] = False
        elif player.level_var == game_data["win_level"]:
            # S'il a atteint le niveau requis, il gagne
            game_data["resultat"] = True
            game_data["jeu_en_cours"] = False

    pygame.mixer.music.stop()  # Stope la musique

    
    try:
        end(player)
    except:
        pass
