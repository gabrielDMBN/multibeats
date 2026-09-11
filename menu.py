import pygame
from pygame import mixer
import sys
from botoes import *

def musica_fundo(musica,volume):
    ambiente = mixer.Sound(musica)
    ambiente.play(-1)
    ambiente.set_volume(volume)

def musica_rounds(musica,volume):
    ambiente = mixer.Sound(musica)
    ambiente.play(0)
    ambiente.set_volume(volume)

class MenuInterativo(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.frames = []
        self.frames.append(pygame.image.load('graficos/TELAS/tela menu/1.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/TELAS/tela menu/2.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/TELAS/tela menu/3.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/TELAS/tela menu/4.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/TELAS/tela menu/5.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/TELAS/tela menu/6.png').convert_alpha())
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect= self.image.get_rect()
        self.rect.topleft = [posX,posY]

    def update (self):
        self.frame_atual += 0.06
        self.image = self.frames[int(self.frame_atual)]
        if self.frame_atual >= 5:
            self.frame_atual = 0

def init(game):
    mixer.stop()
    musica_fundo('musicas/menu.ogg',0.18)

    #interface
    game.logo = pygame.image.load('graficos/INTERFACE/multibeats.png').convert_alpha()
    game.pylogo = Botao(1780, 940, 'graficos/INTERFACE/pygame.png', 'graficos/INTERFACE/pygame2.png',function=lambda game: game.new_level("creditos"), arg=game)###################
    game.rasgos = pygame.image.load('graficos/INTERFACE/rasgos.png').convert_alpha()
    game.pylogo2 = pygame.image.load('graficos/INTERFACE/pygame3.png').convert_alpha()

    #FUNDO ANIMADO
    game.moving_fundo = pygame.sprite.Group()
    game.fundo = MenuInterativo(0, 0)
    game.moving_fundo.add(game.fundo)
    #BOTOES:
    game.button_jogar = Botao(77, 471, "botoes/jogarMenu1.png", "botoes/jogarMenu2.png",function=lambda game: game.new_level("personagens_selections"), arg=game)
    game.button_regras = Botao(77, 670, "botoes/regrasMenu1.png", "botoes/regrasMenu2.png",function=lambda game: game.new_level("regras"), arg=game )
    game.button_sair = Botao(77, 867, "botoes/sairMenu1.png", "botoes/sairMenu2.png",function=exit)

def loop(game):

    game.moving_fundo.draw(game.screen)
    game.moving_fundo.update()


    game.screen.blit(game.logo, (0, 0))

    game.screen.blit(game.rasgos, (1000, 0))
    game.screen.blit(game.pylogo2, (1, 2))

    #BOTOES
    game.pylogo.update()
    game.pylogo.desenhar()

    game.button_jogar.update()
    game.button_jogar.desenhar()

    game.button_regras.update()
    game.button_regras.desenhar()

    game.button_sair.update()
    game.button_sair.desenhar()
