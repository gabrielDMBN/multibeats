from menu import *

def init(game):
    game.pylogo1 = pygame.image.load('graficos/INTERFACE/pygame3.png').convert_alpha()
    game.creditos = pygame.image.load('graficos/TELAS/tela creditos/creditos.png').convert_alpha()



def loop(game):
    #fundo interativo
    game.moving_fundo.draw(game.screen)
    game.moving_fundo.update()
    #logo pygame
    game.screen.blit(game.pylogo1, (1, 2))
    #creditos
    (game.screen.blit(game.creditos, (0, 0)))

