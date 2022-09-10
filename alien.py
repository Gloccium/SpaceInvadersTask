import pygame
from os import path


class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        file_path = path.join('graphics', color + '.png')
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

        if color == 'red':
            self.value = 10
        elif color == 'green':
            self.value = 20
        else:
            self.value = 30

    def update(self, direction):
        self.rect.x += direction


class ExtraAlien(pygame.sprite.Sprite):
    def __init__(self, side, screen_width):
        super().__init__()
        self.image = pygame.image.load(path.join('graphics',
                                                 'extra.png')).convert_alpha()

        if side == 'right':
            x = screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3

        self.rect = self.image.get_rect(topleft=(x, 80))

    def update(self):
        self.rect.x += self.speed
