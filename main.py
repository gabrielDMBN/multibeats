import sys
import pygame
from pygame import mixer


class Game:
    def __init__(self):
        pygame.init()
        largura, altura = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
        self.level = __import__("menu")
        self.clock = pygame.time.Clock()
        self.time = pygame.time.get_ticks()
        self.lest_time = pygame.time.get_ticks()
        self.delta_time = 0
        self.level.init(self)

    def new_level(self, nome):
        self.level = __import__(nome)

        self.level.init(self)

    def update(self):
        self.lest_time = self.time
        self.time = pygame.time.get_ticks()
        self.delta_time = (self.time - self.lest_time) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mixer.stop()
                    self.new_level('menu')
    def run(self):
        while True:
            self.update()
            self.level.loop(self)
            self.clock.tick(60)
            #print(self.clock.get_fps())
            pygame.display.flip()


if __name__ == "__main__":
    jogo = Game()
    jogo.run()
