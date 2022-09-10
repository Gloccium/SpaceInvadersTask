import pygame
from os import path


def define_menu(screen):
    font = pygame.font.Font(path.join('font', 'Pixeled.ttf'), 30)
    game_name = font.render('Space Invaders', False, 'white')
    game_name_rect = game_name.get_rect(center=(300, 200))
    game_message = font.render('Press SPACE to begin', False, 'white')
    game_message_rect = game_message.get_rect(center=(300, 300))

    pygame.display.set_caption('Space Invaders')
    pygame.display.set_icon(pygame.image.load(path.join('graphics',
                                                        'game_icon.png')))

    screen.fill('black')
    screen.blit(game_name, game_name_rect)
    screen.blit(game_message, game_message_rect)
