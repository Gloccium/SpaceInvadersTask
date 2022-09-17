import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, screen_height):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.height_y_constraint = screen_height

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
            self.kill()

    def update(self):
        self.rect.y += self.speed
        self.destroy()


class DiagonalLaser(pygame.sprite.Sprite):
    def __init__(self, pos, x_speed, y_speed, screen_height):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill('#FF66B2')
        self.rect = self.image.get_rect(center=pos)
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.height_y_constraint = screen_height

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
            self.kill()

    def update(self):
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed
        self.destroy()
