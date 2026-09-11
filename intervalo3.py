import pygame
from botoes import *
from bloco_notas import  *
from menu import musica_rounds
from personagens import *
from importlib import import_module



#FONTES
BIG=pygame.font.Font('fontes/ARCADE_N.TTF',46)
MED=pygame.font.Font('fontes/ARCADE_N.TTF',35)
SMALL=pygame.font.Font('fontes/ARCADE_N.TTF',20)

Mapas = (
    'graficos/MAPAS/arenahud2.png',
    'graficos/MAPAS/arenajjkHUD.png',
    'graficos/MAPAS/arenamineHUD.png'
)
PersonagensE=(
    SukunaE(590, 565),
    GojoE(590, 565),
    ToxE(580, 565),
    ReaperE(570, 565)
)
PersonagensD=(
    SukunaD(941, 565),
    GojoD(941, 565),
    ToxD(961, 565),
    ReaperD(961, 565)
)
BarravidaE=(
    'graficos\INTERFACE\BARRAVIDA\LIFE0E.png',
    'graficos\INTERFACE\BARRAVIDA\LIFE1E.png',
    'graficos\INTERFACE\BARRAVIDA\LIFE2E.png',
    'graficos\INTERFACE\BARRAVIDA\LIFE3E.png'
)

BarravidaD=(
    'graficos\INTERFACE\BARRAVIDA\LIFE0D.png',
    'graficos\INTERFACE\BARRAVIDA\LIFE1D.png',
    'graficos\INTERFACE\BARRAVIDA\LIFE2D.png',
    'graficos\INTERFACE\BARRAVIDA\LIFE3D.png'
)

Icon=(
    'graficos/ICONS/sukunaSELECTED.png',
    'graficos/ICONS/gojoSELECTED.png',
    'graficos/ICONS/toxtricitySELECTED.png',
    'graficos/ICONS/reaperSELECTED.png'
)

TelasVitoria=(
    'vitoriaSukuna',
    'vitoriaGojo',
    'vitoriaTox',
    'vitoriaReaper'
)
def init(game):
    #timer
    game.tempo=6
    #mixer.stop()
    dano = mixer.Sound('sounds/damage.ogg')
    dano.play(0)
    dano.set_volume(0.1)
    #INICIALIZANDO PONTUAÇÃO
    game.pontuacaoE = 0
    game.pontuacaoD = 0

    #musica_rounds('musicas/round1.ogg',0.08)
    game.image = pygame.image.load(Mapas[game.numero_Arena-1]).convert_alpha()
    #PERSONAGENS
    game.moving_sprite2 = pygame.sprite.Group()
    game.msprite2 = PersonagensE[game.numero_Personagem-1]
    game.moving_sprite2.add(game.msprite2)

    game.moving_sprite = pygame.sprite.Group()
    game.msprite = PersonagensD[game.numero_PersonagemA-1]
    game.moving_sprite.add(game.msprite)
    #BORDA
    game.bordaE = pygame.image.load('graficos\INTERFACE\BARRAVIDA\PLAYER1P.png').convert_alpha()
    game.bordaD  = pygame.image.load('graficos\INTERFACE\BARRAVIDA\PLAYER2P.png').convert_alpha()
    # ICONS
    game.iconE = pygame.image.load(Icon[game.numero_Personagem-1]).convert_alpha()
    game.iconD = pygame.image.load(Icon[game.numero_PersonagemA-1]).convert_alpha()


def loop(game):
    #Fim de jogo
    if game.tempo>1:
        #progressão do relogio
        game.tempo -= game.delta_time
    else:
        if game.HPE == 0:
            game.vencedor='Player 2'
            game.new_level(TelasVitoria[game.numero_PersonagemA - 1])
        elif game.HPD == 0:
            game.vencedor='Player 1'
            game.new_level(TelasVitoria[game.numero_Personagem - 1])
        else:
            game.new_level('jogo3')

    game.screen.blit(game.image, (0, 0))
    #VIDA
    game.vidaE = pygame.image.load(BarravidaE[game.HPE]).convert_alpha()
    game.vidaD = pygame.image.load(BarravidaD[game.HPD]).convert_alpha()
    #PERSONAGENS
    game.moving_sprite2.draw(game.screen)
    game.moving_sprite2.update()
    game.moving_sprite.draw(game.screen)
    game.moving_sprite.update()
    #BARRA DE VIDA
    game.screen.blit(game.vidaE,(262,973))
    game.screen.blit(game.bordaE,(0,1080-257))
    game.screen.blit(game.vidaD,(1097,973))
    game.screen.blit(game.bordaD,(1920-257,1080-257))
    #ICONS
    game.screen.blit(game.iconE,(0,1080-231))
    game.screen.blit(game.iconD,(1920-231,1080-231))

    #TEXTS

    #definindo rounds
    rounds = BIG.render('Intervalo', False, ('White')).convert_alpha()
    roundsHB = rounds.get_rect(center=(1920 / 2, 60))
    roundtimer = BIG.render(f'{int(game.tempo//1)}', False, ('White')).convert_alpha()
    roundtimerHB = roundtimer.get_rect(center=(1920 / 2, 120))


    #definindo player1
    player1 = MED.render('Player 1', False, ('Black')).convert_alpha()
    player1HB = player1.get_rect(center=(410, 900))
    player1points = MED.render(f'{game.pontuacaoE} P', False, ('Black')).convert_alpha()
    player1pointsHB = player1points.get_rect(center=(410, 950))
    #definindo player2
    player2 = MED.render('Player 2', False, ('Black')).convert_alpha()
    player2HB = player2.get_rect(center=(1510, 900))
    player2points = MED.render(f'{game.pontuacaoD} P', False, ('Black')).convert_alpha()
    player2pointsHB = player2points.get_rect(center=(1510, 950))

    #DESENHANDO TEXTOS
    #rounds
    game.screen.blit(rounds,(roundsHB.topleft,roundsHB.bottomright))
    game.screen.blit(roundtimer,(roundtimerHB.topleft,roundtimerHB.bottomright))
    #player1
    game.screen.blit(player1,(player1HB.topleft,player1HB.bottomright))
    game.screen.blit(player1points,(player1pointsHB.topleft,player1pointsHB.bottomright))
    #player2
    game.screen.blit(player2,(player2HB.topleft,player2HB.bottomright))
    game.screen.blit(player2points,(player2pointsHB.topleft,player2pointsHB.bottomright))

