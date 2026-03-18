import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.direction = pygame.Vector2(1, 0)

    def move(self, target_list=None):
        keys = pygame.key.get_pressed()
        move_dir = pygame.Vector2(0, 0)

        if keys[pygame.K_UP] or keys[pygame.K_w]: move_dir.y = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: move_dir.y = 1
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: move_dir.x = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: move_dir.x = 1

        if move_dir.length() > 0:
            move_dir = move_dir.normalize()
            self.direction = move_dir
            self.rect.center += move_dir * self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT

    def shoot(self):
        from code.PlayerShot import PlayerShot
        return PlayerShot(name="StoneShoot", position=self.rect.center, direction=self.direction)
