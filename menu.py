import pygame
from os import path


def define_menu(screen):
    pygame.display.set_caption('Space Invaders')
    pygame.display.set_icon(pygame.image.load(path.join('graphics',
                                                        'game_icon.png')))

    font = pygame.font.Font(path.join('font', 'Pixeled.ttf'), 30)

    game_name = font.render('Space Invaders', False, 'white')
    game_name_rect = game_name.get_rect(center=(300, 200))

    game_message = font.render('Press TAB to begin', False, 'white')
    game_message_rect = game_message.get_rect(center=(300, 300))

    red_alien = pygame.image.load(
        path.join('graphics', 'red.png')).convert_alpha()
    red_alien_rect = red_alien.get_rect(center=(300, 100))

    green_alien = pygame.image.load(
        path.join('graphics', 'green.png')).convert_alpha()
    green_alien_rect = green_alien.get_rect(center=(100, 100))

    yellow_alien = pygame.image.load(
        path.join('graphics', 'yellow.png')).convert_alpha()
    yellow_alien_rect = yellow_alien.get_rect(center=(500, 100))

    player = pygame.image.load(
        path.join('graphics', 'player.png')).convert_alpha()
    player_rect = player.get_rect(center=(295, 500))

    screen.fill('black')
    screen.blit(game_name, game_name_rect)
    screen.blit(game_message, game_message_rect)
    screen.blit(red_alien, red_alien_rect)
    screen.blit(green_alien, green_alien_rect)
    screen.blit(yellow_alien, yellow_alien_rect)
    screen.blit(player, player_rect)
