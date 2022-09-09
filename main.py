import pygame
import obstacle
from sys import exit
from os import path
from player import Player
from alien import Alien, ExtraAlien
from laser import Laser
from random import choice, randint


class Game:
    def __init__(self):
        # Setup for player
        player_sprite = Player((screen_width / 2, screen_height),
                               screen_width,
                               5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Setup for health and score systems
        self.lives = 3
        self.life_surf = pygame.image.load(
            path.join('graphics', 'player.png')).convert_alpha()
        self.life_x_start_pos = screen_width - (
                self.life_surf.get_size()[0] * 2 + 20)

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
            laser_sprite = Laser(random_alien.rect.center, 6, screen_height)
            self.alien_lasers.add(laser_sprite)

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
                if pygame.sprite.spritecollide(laser, self.aliens, True):
                    laser.kill()

                # extra alien collision
                if pygame.sprite.spritecollide(laser, self.extra_alien, True):
                    laser.kill()

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
                        pygame.quit()
                        exit()
        # Aliens
        if self.aliens:
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.blocks, True)

                if pygame.sprite.spritecollide(alien, self.player, False):
                    pygame.quit()
                    exit()

    def display_lives(self):
        for life in range(self.lives - 1):
            x = self.life_x_start_pos + (
                    life * (self.life_surf.get_size()[0] + 10))
            screen.blit(self.life_surf, (x, 8))

    def run(self):
        self.player.update()
        self.aliens.update(self.alien_direction)
        self.alien_position_checkup()
        self.alien_lasers.update()
        self.extra_alien_timer()
        self.extra_alien.update()
        self.collision_checks()
        self.display_lives()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)

        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.alien_lasers.draw(screen)
        self.extra_alien.draw(screen)


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Space Invaders')
    pygame.display.set_icon(pygame.image.load(path.join('graphics',
                                                        'game_icon.png')))
    clock = pygame.time.Clock()
    game = Game()

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == ALIENLASER:
                game.alien_shoot()

        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60)
