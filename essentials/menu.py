import pygame
from os import path


def show_start_menu(screen):
    pygame.display.set_caption('Space Invaders')
    pygame.display.set_icon(pygame.image.load(
        path.join('interface', 'graphics', 'game_icon.png')))

    font = pygame.font.Font(path.join('interface', 'font', 'Pixeled.ttf'), 30)

    game_name = font.render('Space Invaders', False, 'white')
    game_name_rect = game_name.get_rect(center=(300, 200))

    game_message = font.render('Press TAB to begin', False, 'white')
    game_message_rect = game_message.get_rect(center=(300, 300))

    red_alien = pygame.image.load(
        path.join('interface', 'graphics', 'red.png')).convert_alpha()
    red_alien_rect = red_alien.get_rect(center=(300, 100))

    green_alien = pygame.image.load(
        path.join('interface', 'graphics', 'green.png')).convert_alpha()
    green_alien_rect = green_alien.get_rect(center=(100, 100))

    yellow_alien = pygame.image.load(
        path.join('interface', 'graphics', 'yellow.png')).convert_alpha()
    yellow_alien_rect = yellow_alien.get_rect(center=(500, 100))

    player = pygame.image.load(
        path.join('interface', 'graphics', 'player.png')).convert_alpha()
    player_rect = player.get_rect(center=(295, 500))

    screen.fill('black')
    screen.blit(game_name, game_name_rect)
    screen.blit(game_message, game_message_rect)
    screen.blit(red_alien, red_alien_rect)
    screen.blit(green_alien, green_alien_rect)
    screen.blit(yellow_alien, yellow_alien_rect)
    screen.blit(player, player_rect)


def show_restart_window(screen):
    font = pygame.font.Font(path.join('interface', 'font', 'Pixeled.ttf'), 30)

    label = font.render('Game over', False, 'white')
    label_rect = label.get_rect(center=(300, 200))

    game_message = font.render('Press TAB to try again', False, 'white')
    game_message_rect = game_message.get_rect(center=(300, 300))

    screen.fill('black')
    screen.blit(label, label_rect)
    screen.blit(game_message, game_message_rect)