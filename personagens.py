import pygame

Vel_Sprites = 0.05
class GojoD(pygame.sprite.Sprite): #posicao (1171, 565)
    def __init__(self, posX, posY):
        super().__init__()
        self.frames = []
        self.frames .append(pygame.image.load('graficos/PERSONAGENS/GOJOD/1f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/GOJOD/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/GOJOD/3f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/GOJOD/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/GOJOD/2f.png').convert_alpha())

        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect= self.image.get_rect()
        self.rect.topleft = [posX,posY]

    def update (self):
        self.frame_atual += Vel_Sprites
        self.image = self.frames[int(self.frame_atual)]
        if self.frame_atual >= 4:
            self.frame_atual = 0
class GojoE(pygame.sprite.Sprite): #posicao (1171, 565)
    def __init__(self, posX, posY):
        super().__init__()
        self.frames = []
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/GOJOE/1f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/GOJOE/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/GOJOE/3f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/GOJOE/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/GOJOE/2f.png').convert_alpha())

        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect= self.image.get_rect()
        self.rect.topleft = [posX,posY]

    def update (self):
        self.frame_atual += Vel_Sprites
        self.image = self.frames[int(self.frame_atual)]
        if self.frame_atual >= 4:
            self.frame_atual = 0
class SukunaE(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.frames = []
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/SUKUNAE/1f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/SUKUNAE/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/SUKUNAE/3f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/SUKUNAE/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/SUKUNAE/2f.png').convert_alpha())
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect= self.image.get_rect()
        self.rect.topleft = [posX,posY]

    def update (self):
        self.frame_atual += Vel_Sprites
        self.image = self.frames[int(self.frame_atual)]
        if self.frame_atual >= 4:
            self.frame_atual = 0
class SukunaD(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.frames = []
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/SUKUNAD/1f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/SUKUNAD/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/SUKUNAD/3f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/SUKUNAD/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/SUKUNAD/2f.png').convert_alpha())
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect= self.image.get_rect()
        self.rect.topleft = [posX,posY]

    def update (self):
        self.frame_atual += Vel_Sprites
        self.image = self.frames[int(self.frame_atual)]
        if self.frame_atual >= 4:
            self.frame_atual = 0
class ToxD(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.frames = []
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/TOXD/1f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/TOXD/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/TOXD/3f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/TOXD/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/TOXD/2f.png').convert_alpha())
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect= self.image.get_rect()
        self.rect.topleft = [posX,posY]

    def update (self):
        self.frame_atual += Vel_Sprites
        self.image = self.frames[int(self.frame_atual)]
        if self.frame_atual >= 4:
            self.frame_atual = 0
class ToxE(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.frames = []
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/TOXE/1f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/TOXE/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/TOXE/3f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/TOXE/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/TOXE/2f.png').convert_alpha())
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect= self.image.get_rect()
        self.rect.topleft = [posX,posY]

    def update (self):
        self.frame_atual += Vel_Sprites
        self.image = self.frames[int(self.frame_atual)]
        if self.frame_atual >= 4:
            self.frame_atual = 0
class ReaperE(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.frames = []
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/REAPERE/1f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/REAPERE/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/REAPERE/3f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/REAPERE/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/REAPERE/2f.png').convert_alpha())
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect= self.image.get_rect()
        self.rect.topleft = [posX,posY]

    def update (self):
        self.frame_atual += Vel_Sprites
        self.image = self.frames[int(self.frame_atual)]
        if self.frame_atual >= 4:
            self.frame_atual = 0

class ReaperD(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.frames = []
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/REAPERD/1f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/REAPERD/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/REAPERD/3f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/REAPERD/2f.png').convert_alpha())
        self.frames.append(pygame.image.load('graficos/PERSONAGENS/REAPERD/2f.png').convert_alpha())
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect= self.image.get_rect()
        self.rect.topleft = [posX,posY]

    def update (self):
        self.frame_atual += Vel_Sprites
        self.image = self.frames[int(self.frame_atual)]
        if self.frame_atual >= 4:
            self.frame_atual = 0


