import pygame
from os import path
from random import randint


class CRT:
    def __init__(self, screen, screen_width, screen_height):
        super().__init__()
        self.crt_screen = screen
        self.crt_screen_width = screen_width
        self.crt_screen_height = screen_height
        self.tv = pygame.image.load(
            path.join('graphics', 'tv.png')).convert_alpha()
        self.tv = pygame.transform.scale(self.tv,
                                         (screen_width, screen_height))

    def create_crt_lines(self):
        line_height = 3
        line_amount = self.crt_screen_height // line_height
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, 'black', (0, y_pos),
                             (self.crt_screen_width, y_pos), 1)

    def draw(self):
        self.tv.set_alpha(randint(75, 90))
        self.create_crt_lines()
        self.crt_screen.blit(self.tv, (0, 0))
