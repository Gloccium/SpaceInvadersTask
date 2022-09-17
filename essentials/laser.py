import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_speed = 0
        self.y_speed = 0
        self.height_y_constraint = 0

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
            self.kill()

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        self.destroy()


class FrontLaser(Laser):
    def __init__(self, pos, screen_height, is_player):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)
        self.x_speed = 0
        self.y_speed = -8 if is_player else 6
        self.height_y_constraint = screen_height


class DiagonalLaser(Laser):
    def __init__(self, pos, screen_height, key):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill('#FF66B2')
        self.rect = self.image.get_rect(center=pos)
        self.x_speed = 5 if key == pygame.K_e else -5
        self.y_speed = -5
        self.height_y_constraint = screen_height
