import pygame
from os import path
from essentials.laser import FrontLaser, DiagonalLaser


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()
        self.image = pygame.image.load(
            path.join('interface', 'graphics', 'player.png')).convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.max_x_constraint = constraint
        self.ready_to_shoot = True
        self.last_shoot_laser_time = 0
        self.laser_cooldown = 600

        self.lasers = pygame.sprite.Group()

        self.laser_sound = pygame.mixer.Sound(
            path.join('interface', 'audio', 'laser.wav'))
        self.laser_sound.set_volume(0.05)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed

        if self.ready_to_shoot:
            [self.shoot_laser(key) for key in
             [pygame.K_SPACE, pygame.K_e, pygame.K_q] if keys[key]]

    def recharge(self):
        if not self.ready_to_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_shoot_laser_time \
                    >= self.laser_cooldown:
                self.ready_to_shoot = True

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    def shoot_laser(self, key):
        self.lasers.add(FrontLaser(self.rect.center, self.rect.bottom,
                                   True)) if key == pygame.K_SPACE \
            else self.lasers.add(
            DiagonalLaser(self.rect.center, self.rect.bottom, key))
        self.ready_to_shoot = False
        self.last_shoot_laser_time = pygame.time.get_ticks()
        self.laser_sound.play()

    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.lasers.update()
