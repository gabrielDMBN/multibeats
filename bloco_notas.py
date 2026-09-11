import pygame
from pygame import mixer

pontuacaoE=0
pontuacaoD=0
Tipo_Image = (
    pygame.image.load("graficos\BLOCOS DE NOTA\A2.png ").convert_alpha(),
    pygame.image.load("graficos\BLOCOS DE NOTA\S2.png ").convert_alpha(),
    pygame.image.load("graficos\BLOCOS DE NOTA\D2.png ").convert_alpha(),
    pygame.image.load("graficos\BLOCOS DE NOTA\L2.png ").convert_alpha(),
    pygame.image.load("graficos\BLOCOS DE NOTA\BAIXO2.png ").convert_alpha(),
    pygame.image.load("graficos\BLOCOS DE NOTA\R2.png ").convert_alpha()
)
PosX = (
    200,
    370,
    534,
    1255,
    1426,
    1590
)


class Input:
    def __init__(self):
        self.keys = pygame.key.get_pressed()
        self.last_keys = self.keys

    def update(self):
        self.last_keys = self.keys
        self.keys = pygame.key.get_pressed()

    def is_pressed(self, key_id) -> bool:
        return self.keys[key_id]

    def start_pressed(self, key_id) -> bool:
        return self.keys[key_id] and not self.last_keys

input_handler = Input()
class BlocoNotas:
    def __init__(self, tipo, key_id, game,altura, velocidade):
      #  self.input = input_handler
        self.img: pygame.Surface = Tipo_Image[tipo - 1].copy()
        self.aparecer= True
        self.pressed= True
        self.x = PosX[tipo - 1]
        self.y = -altura
        self.vel = velocidade
        self.alpha = 255
        self.key_id = key_id
        self.game=game

    def update(self):
        if self.aparecer:
            #perfect 60 gap / 266 -> 326
            if 296 - 30 <= self.y < 296 + 30:
                pressed= pygame.key.get_pressed()[self.key_id]
                if pressed and not self.pressed:
                    if self.key_id == pygame.K_a or self.key_id == pygame.K_s or self.key_id == pygame.K_d:
                        self.game.pontuacaoE += 100
                        #print("Ponto Esquerda: ", self.game.pontuacaoE)
                    elif self.key_id == pygame.K_LEFT or self.key_id == pygame.K_DOWN or self.key_id == pygame.K_RIGHT:
                        self.game.pontuacaoD += 100
                        #print("Ponto Direita: ", self.game.pontuacaoD)
                    self.aparecer = False
                self.pressed = pressed

            # good 60 gap / 236 -> 266
            elif 296 - 30 > self.y >= 296 - 30 - 30 :
                pressed= pygame.key.get_pressed()[self.key_id]
                if pressed and not self.pressed:
                    if self.key_id == pygame.K_a or self.key_id == pygame.K_s or self.key_id == pygame.K_d:
                        self.game.pontuacaoE += 50
                        #print("Ponto Esquerda: ", self.game.pontuacaoE)
                    elif self.key_id == pygame.K_LEFT or self.key_id == pygame.K_DOWN or self.key_id == pygame.K_RIGHT:
                        self.game.pontuacaoD += 50
                        #print("Ponto Direita: ", self.game.pontuacaoD)
                    self.aparecer = False
                self.pressed = pressed

            # bad 60 gap / 206 -> 236
            elif 296 - 30 - 30 > self.y > 296 - 30 - 30 - 30:
                pressed = pygame.key.get_pressed()[self.key_id]
                if pressed and not self.pressed:
                    if self.key_id == pygame.K_a or self.key_id == pygame.K_s or self.key_id == pygame.K_d:

                        self.game.pontuacaoE += 25
                        #print("Ponto Esquerda: ", self.game.pontuacaoE)
                    elif self.key_id == pygame.K_LEFT or self.key_id == pygame.K_DOWN or self.key_id == pygame.K_RIGHT:

                        self.game.pontuacaoD += 25
                        #print("Ponto Direita: ", self.game.pontuacaoD)
                    self.aparecer = False
                self.pressed = pressed

            # ERROU
            if self.y > 296 + self.img.get_height():
                self.img.set_alpha(self.alpha)
                self.alpha -= 9

            pygame.display.get_surface().blit(self.img, (self.x, self.y))
            self.y += self.vel * self.game.delta_time

