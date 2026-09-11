import pygame
from pygame import mixer

class Botao:
    def __init__(self, x, y, imagem1, imagem2, function=None, arg=None):
        self.image = None
        self.pressed = True
        self.hoover = False
        self.imagem1 = pygame.image.load(imagem1).convert_alpha()
        self.image2 = pygame.image.load(imagem2).convert_alpha()
        self.x = x
        self.y = y
        self.largura = self.imagem1.get_width()
        self.altura = self.imagem1.get_height()
        self.hoover_sound = mixer.Sound('sounds/hoover.ogg')
        self.hoover_sound.set_volume(0.07)
        self.func = function
        self.arg = arg

    def desenhar(self):

        if self.image:
            pygame.display.get_surface().blit(
                self.image,
                (self.x, self.y)
            )

    def update(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.x <= mouseX <= self.x + self.largura and self.y <= mouseY <= self.y + self.altura:
            self.image = self.image2
            if not self.hoover:
                self.hoover_sound.play()
            pressed = pygame.mouse.get_pressed()[0]
            if pressed and not self.pressed:
                if self.func:
                    if self.arg:
                        self.func(self.arg)
                    else:
                        self.func()
            self.pressed = pressed
            self.hoover = True
        else:
            self.image = self.imagem1
            self.hoover = False