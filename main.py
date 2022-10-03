import pygame
from sys import exit
from os import path
from essentials.game import Game
from essentials.crt import CRT
from essentials.menu import show_start_menu, show_restart_window,\
    show_leaderboard_window
from essentials.game_states import GameStates

def start_game():
    clock = pygame.time.Clock()
    game = Game(screen, screen_width, screen_height)
    crt = CRT(screen, screen_width, screen_height)

    ALIEN_LASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIEN_LASER, 800)

    PLAYER_BONUS_END = pygame.USEREVENT + 2
    pygame.time.set_timer(PLAYER_BONUS_END, 10000)

    PLAYER_DEBUFF_END = pygame.USEREVENT + 3
    pygame.time.set_timer(PLAYER_DEBUFF_END, 3000)

    background_music = pygame.mixer.Sound(
        path.join('interface', 'audio', 'music.wav'))
    background_music.set_volume(0.05)
    background_music.play(loops=-1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.high_score.append(game.score)
                game.load_highest_score()
                pygame.quit()
                exit()

            if game.game_state == GameStates.GAME_SCREEN.value:
                if event.type == ALIEN_LASER:
                    game.alien_shoot()
                if event.type == PLAYER_BONUS_END:
                    game.player_end_bonus()
                if event.type == PLAYER_DEBUFF_END:
                    game.player_end_debuff()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    game.pause()

            if event.type == pygame.KEYDOWN \
                    and game.game_state == GameStates.RESTART_WINDOW.value:
                if event.key == pygame.K_TAB:
                    game = Game(screen, screen_width, screen_height)
                    game.game_state = GameStates.GAME_SCREEN.value
                if event.key == pygame.K_m:
                    game = Game(screen, screen_width, screen_height)
                    game.game_state = GameStates.MAIN_MENU.value

            if event.type == pygame.KEYDOWN and game.game_state \
                    == GameStates.MAIN_MENU.value:
                if event.key == pygame.K_TAB:
                    game.game_state = GameStates.GAME_SCREEN.value
                if event.key == pygame.K_l:
                    game.game_state = GameStates.LEADERBOARD_SCREEN.value

            if event.type == pygame.KEYDOWN and event.key == pygame.K_m and \
                    game.game_state == GameStates.LEADERBOARD_SCREEN.value:
                game.game_state = GameStates.MAIN_MENU.value

        if game.game_state == GameStates.MAIN_MENU.value:
            show_start_menu(screen)
        if game.game_state == GameStates.GAME_SCREEN.value:
            screen.fill((30, 30, 30))
            game.run()
            crt.draw()
        if game.game_state == GameStates.RESTART_WINDOW.value:
            show_restart_window(screen)
        if game.game_state == GameStates.LEADERBOARD_SCREEN.value:
            show_leaderboard_window(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    start_game()
