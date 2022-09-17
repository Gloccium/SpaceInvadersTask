import pygame
from essentials import obstacle
from sys import exit
from os import path
from essentials.player import Player
from essentials.alien import Alien, ExtraAlien
from essentials.laser import FrontLaser
from random import choice, randint
from essentials.crt import CRT
from essentials.menu import show_start_menu, show_restart_window, \
    show_pause_window, show_leaderboard_window
from essentials.game_states import GameStates


class Game:
    def __init__(self):
        # Setup for game states
        self.game_state = GameStates.MAIN_MENU.value

        # Setup for player
        player_sprite = Player((screen_width / 2, screen_height),
                               screen_width,
                               5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Setup for health and score systems
        self.lives = 3
        self.life_surf = pygame.image.load(
            path.join('interface', 'graphics', 'player.png')).convert_alpha()
        self.life_x_start_pos = screen_width - (
                self.life_surf.get_size()[0] * 2 + 20)
        self.score = 0
        self.highest_score = open('leaderboard.txt').readline()
        self.font = pygame.font.Font(
            path.join('interface', 'font', 'Pixeled.ttf'), 20)

        # Setup for obstacles
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num * (screen_width /
                                            self.obstacle_amount)
                                     for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(self.obstacle_x_positions,
                                       x_start=screen_width / 15, y_start=480)

        # Setup for aliens
        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.alien_setup(rows=6, columns=8)
        self.alien_direction = 1

        # Setup for extra alien
        self.extra_alien = pygame.sprite.GroupSingle()
        self.extra_alien_spawn_time = randint(400, 800)

        # Audio
        self.laser_sound = pygame.mixer.Sound(
            path.join('interface', 'audio', 'laser.wav'))
        self.laser_sound.set_volume(0.05)
        self.explosion_sound = pygame.mixer.Sound(
            path.join('interface', 'audio', 'explosion.wav'))
        self.explosion_sound.set_volume(0.1)

    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for column_index, column in enumerate(row):
                if column == 'x':
                    x = x_start + column_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, '#F15050', x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self, offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def alien_setup(self, rows, columns, x_distance=60, y_distance=48,
                    x_offset=70, y_offset=100):
        for row_index, row in enumerate(range(rows)):
            for column_index, column in enumerate(range(columns)):
                x = column_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                if row_index == 0:
                    alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2:
                    alien_sprite = Alien('green', x, y)
                else:
                    alien_sprite = Alien('red', x, y)
                self.aliens.add(alien_sprite)

    def alien_position_checkup(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width:
                self.alien_direction = -1
                self.alien_move_downwards(2)
            elif alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_downwards(2)

    def alien_move_downwards(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = FrontLaser(random_alien.rect.center, screen_height,
                                      False)
            self.alien_lasers.add(laser_sprite)
            self.laser_sound.play()

    def extra_alien_timer(self):
        self.extra_alien_spawn_time -= 1
        if self.extra_alien_spawn_time <= 0:
            self.extra_alien.add(ExtraAlien(choice(['right', 'left']),
                                            screen_width))
            self.extra_alien_spawn_time = randint(400, 800)

    def collision_checks(self):
        # Player lasers
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                # obstacle collisions
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                # alien collisions
                aliens_hit = pygame.sprite.spritecollide(laser, self.aliens,
                                                         True)
                if aliens_hit:
                    for alien in aliens_hit:
                        self.score += alien.value
                    laser.kill()
                    self.explosion_sound.play()

                # extra alien collision
                if pygame.sprite.spritecollide(laser, self.extra_alien, True):
                    self.score += randint(50, 100)
                    laser.kill()
                    self.explosion_sound.play()

        # Alien lasers
        if self.alien_lasers:
            for laser in self.alien_lasers:
                # obstacle collisions
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                # player collision
                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.lives -= 1
                    if self.lives <= 0:
                        self.game_state = GameStates.RESTART_WINDOW.value
                        self.load_highest_score()
        # Aliens
        if self.aliens:
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.blocks, True)

                if pygame.sprite.spritecollide(alien, self.player, False):
                    self.game_state = GameStates.RESTART_WINDOW.value
                    self.load_highest_score()

    def display_lives(self):
        for life in range(self.lives - 1):
            x = self.life_x_start_pos + (
                    life * (self.life_surf.get_size()[0] + 10))
            screen.blit(self.life_surf, (x, 8))

    def display_score(self):
        score_surf = self.font.render(f'score:  {self.score}', False, 'white')
        score_rect = score_surf.get_rect(topleft=(10, -10))
        screen.blit(score_surf, score_rect)

    def game_continuation(self):
        if not self.aliens.sprites():
            self.alien_setup(rows=6, columns=8)
            self.create_multiple_obstacles(self.obstacle_x_positions,
                                           x_start=screen_width / 15,
                                           y_start=480)

    @staticmethod
    def pause():
        paused = True

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    paused = False

            show_pause_window(screen)
            pygame.display.update()

    def update_highest_score(self):
        if self.score > int(self.highest_score):
            self.highest_score = self.score

    def load_highest_score(self):
        with open('leaderboard.txt', 'w') as file:
            file.write(str(self.highest_score))
            file.close()

    def run(self):
        self.player.update()
        self.alien_lasers.update()
        self.extra_alien.update()
        self.update_highest_score()

        self.aliens.update(self.alien_direction)
        self.alien_position_checkup()
        self.extra_alien_timer()
        self.collision_checks()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.alien_lasers.draw(screen)
        self.extra_alien.draw(screen)
        self.display_lives()
        self.display_score()
        self.game_continuation()


def start_game():
    clock = pygame.time.Clock()
    game = Game()
    crt = CRT(screen, screen_width, screen_height)

    ALIEN_LASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIEN_LASER, 800)

    background_music = pygame.mixer.Sound(
        path.join('interface', 'audio', 'music.wav'))
    background_music.set_volume(0.05)
    background_music.play(loops=-1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.load_highest_score()
                pygame.quit()
                exit()

            if game.game_state == GameStates.GAME_SCREEN.value:
                if event.type == ALIEN_LASER:
                    game.alien_shoot()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    game.pause()

            if event.type == pygame.KEYDOWN \
                    and game.game_state == GameStates.RESTART_WINDOW.value:
                if event.key == pygame.K_TAB:
                    game = Game()
                    game.game_state = GameStates.GAME_SCREEN.value
                if event.key == pygame.K_m:
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
