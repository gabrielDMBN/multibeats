import pygame
from menu import musica_rounds
from menu import musica_fundo
#FONTES
BIG=pygame.font.Font('fontes/ARCADE_N.TTF',46)
MED=pygame.font.Font('fontes/ARCADE_N.TTF',35)
SMALL=pygame.font.Font('fontes/ARCADE_N.TTF',20)

class GojoFinalizacao(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.frames = [
            pygame.image.load('graficos/FINALIZACOES/GOJO/1f.png').convert_alpha(),
            pygame.image.load('graficos/FINALIZACOES/GOJO/2f.png').convert_alpha(),
            pygame.image.load('graficos/FINALIZACOES/GOJO/3f.png').convert_alpha(),
            pygame.image.load('graficos/FINALIZACOES/GOJO/4f.png').convert_alpha(),
            pygame.image.load('graficos/FINALIZACOES/GOJO/5f.png').convert_alpha(),
            pygame.image.load('graficos/FINALIZACOES/GOJO/4f.png').convert_alpha(),
            pygame.image.load('graficos/FINALIZACOES/GOJO/3f.png').convert_alpha(),
            pygame.image.load('graficos/FINALIZACOES/GOJO/2f.png').convert_alpha()
        ]
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = [posX, posY]
        self.tempo_frame = 0.35  # Tempo de exibição de cada frame em segundos
        self.temp_acumulado = 0.0

    def update(self, delta_time):
        self.temp_acumulado += delta_time
        if self.temp_acumulado >= self.tempo_frame:
            self.frame_atual += 1
            self.temp_acumulado = 0.0
            if self.frame_atual >= len(self.frames):
                self.frame_atual = 0
        self.image = self.frames[self.frame_atual]

def init(game):#ANIMADO
    #SONS
    pygame.mixer.stop()
    musica_fundo('sounds/GOJO/gojobackground.ogg',0.04)# loop
    musica_rounds('sounds/Victory Sound.ogg',0.08)#som vitoria
    musica_rounds('sounds/GOJO/gojofrase.ogg',0.45)#frase

    #ANIMADO
    game.moving_finalizacao = pygame.sprite.Group()
    game.fundo = GojoFinalizacao(0, 0)
    game.moving_finalizacao.add(game.fundo)

    if game.vencedor=='Player 2':
        game.image = pygame.image.load('graficos/INTERFACE/PLAYER 2 WINf.png').convert_alpha()
    else:
        game.image = pygame.image.load('graficos/INTERFACE/PLAYER 1 WINf.png').convert_alpha()

def loop(game):
    # fundo interativo
    game.moving_finalizacao.draw(game.screen)
    game.moving_finalizacao.update(delta_time=game.delta_time)
    #texto
    game.screen.blit(game.image, (0, 0))