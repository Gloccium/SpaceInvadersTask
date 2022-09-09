import pygame
from sys import exit
from os import path

import obstacle
from player import Player


class Game:
    def __init__(self):
        # Setup for player
        player_sprite = Player((screen_width / 2, screen_height),
                               screen_width,
                               5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

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

    def run(self):
        self.player.update()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)

        self.blocks.draw(screen)


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Space invaders')
    pygame.display.set_icon(pygame.image.load(path.join('graphics',
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
