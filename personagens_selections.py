import pygame
from botoes import *
from menu import musica_fundo

def init(game):
    #valores iniciais
    game.numero_Arena = 0
    game.numero_Personagem = 0
    game.numero_PersonagemA = 0
    #musica
    mixer.stop()
    musica_fundo('musicas/selectionmusic.ogg',0.18)

    #fundo principal
    game.image = pygame.image.load('graficos/TELAS/telaselecao.png').convert_alpha()

    # definindo mapa
    def mudar_imagem_mapa(itens):
        game, nome, numero_Arena = itens
        game.ARENAselect = pygame.image.load(nome).convert()
        game.numero_Arena = numero_Arena
    #tela mapa
    game.ARENAselect = pygame.image.load('graficos/ICONS/mapSELECT.png').convert_alpha()

    #Tela de icone VERMELHO
    game.select = pygame.image.load('graficos/ICONS/SELECT.png').convert_alpha()
    #definindo personagem vermelho
    def mudar_imagem(itens):
        game, nome, numero_Personagem = itens
        game.select = pygame.image.load(nome).convert()
        game.numero_Personagem = numero_Personagem

    # TELA de icone AZUL
    game.selectA = pygame.image.load('graficos/ICONS/SELECT.png').convert_alpha()
    #definindo personagem azul
    def mudar_imagemA(itens):
        game, nome, numero_PersonagemA = itens
        game.selectA = pygame.image.load(nome).convert()
        game.numero_PersonagemA = numero_PersonagemA


    #icones vermelhos
    game.button_sukuna = Botao(108, 692, "graficos/ICONS/sukunaP.png", "graficos/ICONS/sakunaverde.png",function=mudar_imagem, arg=(game, "graficos/ICONS/sukuna2bSELECT.png",1))
    game.button_gojo = Botao(314, 692, "graficos/ICONS/gojoP.png", "graficos/ICONS/gojoverde.png",function=mudar_imagem, arg=(game, "graficos/ICONS/gojo2SELECT.jpg",2))
    game.button_tox = Botao(108, 883, "graficos/ICONS/toxP.png", "graficos/ICONS/toxverde.png", function=mudar_imagem,arg=(game, "graficos/ICONS/toxtricity2SELECT.png",3))
    game.button_reaper = Botao(314, 883, "graficos/ICONS/reaperP.png", "graficos/ICONS/reaperverde.png",function=mudar_imagem, arg=(game, "graficos/ICONS/Reaper2SELECT.png",4))

    # icones azuis
    game.image = pygame.image.load('graficos/TELAS/telaselecao.png').convert()
    game.button_sukunaA = Botao(1466, 692, "graficos/ICONS/sukunaAP.png", "graficos/ICONS/sakunaverde.png",function=mudar_imagemA, arg=(game, "graficos/ICONS/sukuna2bSELECT.png",1))
    game.button_gojoA = Botao(1672, 692, "graficos/ICONS/gojoAP.png", "graficos/ICONS/gojoverde.png",function=mudar_imagemA, arg=(game, "graficos/ICONS/gojo2SELECT.jpg",2))
    game.button_toxA = Botao(1466, 883, "graficos/ICONS/toxAP.png", "graficos/ICONS/toxverde.png",function=mudar_imagemA, arg=(game, "graficos/ICONS/toxtricity2SELECT.png",3))
    game.button_reaperA = Botao(1672, 883, "graficos/ICONS/reaperAP.png", "graficos/ICONS/reaperverde.png",function=mudar_imagemA, arg=(game, "graficos/ICONS/Reaper2SELECT.png",4))

    #botões arenas
    game.button_arenapokemon = Botao(681, 124, "graficos/ICONS/arenapokemonP.png", "graficos/ICONS/arenapokemonP2.png",function=mudar_imagem_mapa,arg=(game,"graficos/ICONS/arenapokemonSELECT.png",1))
    game.button_arenajjk = Botao(889, 124, "graficos/ICONS/arenajjkP.png", "graficos/ICONS/arenajjkP2.png",function=mudar_imagem_mapa,arg=(game,"graficos/ICONS/arenajjkSELECT.png",2))
    game.button_mapa3 = Botao(1096, 124, "graficos/ICONS/arenamineP.png", "graficos/ICONS/arenamineP2.png",function=mudar_imagem_mapa,arg=(game,"graficos/ICONS/arenamineSELECT.png",3))

    #botão de jogar
    game.button_jogar = Botao(1553, 113, "botoes/jogarMenu1.png", "botoes/jogarMenu2.png", function=lambda game: game.new_level("intervalo1"), arg=game)#################################################################


def loop(game):
    #tela de fundo
    game.screen.blit(game.image, (0, 0))

    #tela icone mapa
    game.screen.blit(game.ARENAselect, (780, 307))

    # Tela de icone VERMELHO
    game.screen.blit(game.select, (531, 703))

    #TELA de icone AZUL
    game.screen.blit(game.selectA, (1081, 703))

    #botoes vermelhos
    game.button_sukuna.update()
    game.button_sukuna.desenhar()

    game.button_gojo.update()
    game.button_gojo.desenhar()

    game.button_tox.update()
    game.button_tox.desenhar()

    game.button_reaper.update()
    game.button_reaper.desenhar()

    #botoes azuis
    game.button_sukunaA.update()
    game.button_sukunaA.desenhar()

    game.button_gojoA.update()
    game.button_gojoA.desenhar()

    game.button_toxA.update()
    game.button_toxA.desenhar()

    game.button_reaperA.update()
    game.button_reaperA.desenhar()

    #botões arenas
    game.button_arenapokemon.update()
    game.button_arenapokemon.desenhar()

    game.button_arenajjk.update()
    game.button_arenajjk.desenhar()

    game.button_mapa3.update()
    game.button_mapa3.desenhar()

    if game.numero_Arena != 0 and game.numero_Personagem !=0 and game.numero_PersonagemA != 0 :
    #jogar
        game.button_jogar.update()
        game.button_jogar.desenhar()
