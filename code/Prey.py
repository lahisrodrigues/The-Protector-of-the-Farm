import random

import pygame

from code.Entity import Entity


class Prey(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.direction = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()
        self.change_dir_timer = pygame.time.get_ticks()

    def move(self, target_list=None):
        now = pygame.time.get_ticks()

        if pygame.time.get_ticks() - self.change_dir_timer > 2000 or self.direction.length() == 0:
            self.direction = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
            if self.direction.length() > 0:
                self.direction = self.direction.normalize()
            self.change_dir_timer = now

        self.rect.center += self.direction * self.speed