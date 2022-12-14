import pygame
import json
from os import path


def show_start_menu(screen):
    pygame.display.set_caption('Space Invaders')
    pygame.display.set_icon(pygame.image.load(
        path.join('interface', 'graphics', 'game_icon.png')))

    font = pygame.font.Font(path.join('interface', 'font', 'Pixeled.ttf'), 30)
    leaderboard_font = pygame.font.Font(path.join('interface', 'font',
                                                  'Pixeled.ttf'), 20)

    game_name = font.render('Space Invaders', False, 'white')
    game_name_rect = game_name.get_rect(center=(300, 200))

    game_message = font.render('Press TAB to begin', False, 'white')
    game_message_rect = game_message.get_rect(center=(300, 300))

    leaderboard_message = leaderboard_font.render(
        'Press L to open leaderboard', False, 'white')
    leaderboard_message_rect = leaderboard_message.get_rect(center=(300, 400))

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
    screen.blit(leaderboard_message, leaderboard_message_rect)
    screen.blit(red_alien, red_alien_rect)
    screen.blit(green_alien, green_alien_rect)
    screen.blit(yellow_alien, yellow_alien_rect)
    screen.blit(player, player_rect)


def show_restart_window(screen):
    font = pygame.font.Font(path.join('interface', 'font', 'Pixeled.ttf'), 30)
    smaller_font = pygame.font.Font(path.join('interface', 'font',
                                              'Pixeled.ttf'), 20)

    label = font.render('Game over', False, 'white')
    label_rect = label.get_rect(center=(300, 200))

    game_message = font.render('Press TAB to try again', False, 'white')
    game_message_rect = game_message.get_rect(center=(300, 300))

    return_message = smaller_font.render(
        'Press M to return to menu', False, 'white')
    return_message_rect = return_message.get_rect(center=(300, 400))

    screen.fill('black')
    screen.blit(label, label_rect)
    screen.blit(game_message, game_message_rect)
    screen.blit(return_message, return_message_rect)


def show_pause_window(screen):
    font = pygame.font.Font(path.join('interface', 'font', 'Pixeled.ttf'), 30)

    pause_message = font.render('Paused', False, 'white')
    pause_message_rect = pause_message.get_rect(center=(300, 200))

    game_message = font.render('Press C to continue',
                               False, 'white')
    game_message_rect = game_message.get_rect(center=(300, 300))

    screen.fill('black')
    screen.blit(pause_message, pause_message_rect)
    screen.blit(game_message, game_message_rect)


def show_leaderboard_window(screen):
    with open('leaderboard.json', 'r') as f:
        high_score = sorted(json.load(f)['best_score'], reverse=True)

    font = pygame.font.Font(path.join('interface', 'font', 'Pixeled.ttf'), 20)

    message_list = []
    [message_list.append((font.render(f'{i + 1}: {high_score[i]}', False,
                                      'white'), 200 + 50 * i)) for i in
     range(3)]
    game_message = font.render('Press M to return to main menu', False,
                               'white')
    game_message_rect = game_message.get_rect(center=(300, 350))
    screen.fill('black')
    [screen.blit(score_message, score_message.get_rect(center=(300, y))) for
     score_message, y in message_list]
    screen.blit(game_message, game_message_rect)
