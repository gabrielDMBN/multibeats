import pygame
from botoes import *
from menu import  *

class RegrasInterativo(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.frames = []
        self.frames.append(pygame.image.load('graficos/TELAS/tela regras/regras1.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/TELAS/tela regras/regras2.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/TELAS/tela regras/regras3.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/TELAS/tela regras/regras4.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/TELAS/tela regras/regras4.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/TELAS/tela regras/regras4.png').convert_alpha())
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect= self.image.get_rect()
        self.rect.topleft = [posX,posY]

    def update (self):
        self.frame_atual += 0.04
        self.image = self.frames[int(self.frame_atual)]
        if self.frame_atual >= 5:
            self.frame_atual = 0

def init(game):
    game.pylogo2 = pygame.image.load('graficos/INTERFACE/pygame3.png').convert_alpha()
    game.moving_regras = pygame.sprite.Group()
    game.mregras = RegrasInterativo(0, 0)
    game.moving_regras.add(game.mregras)



def loop(game):
    #fundo interativo
    game.moving_fundo.draw(game.screen)
    game.moving_fundo.update()
    #logo pygame
    game.screen.blit(game.pylogo2, (1, 2))
    #regras animacao
    game.moving_regras.draw(game.screen)
    game.moving_regras.update()



