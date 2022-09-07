import pygame
from sys import exit
from os import path


class Game:
    def __init__(self):
        pass

    def run(self):
        pass
        # update all sprite groups
        # drawing all sprites


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Space invaders')
    pygame.display.set_icon(pygame.image.load(path.join('Graphics',
                                                        'Icon',
                                                        'game_icon.png')))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60)
