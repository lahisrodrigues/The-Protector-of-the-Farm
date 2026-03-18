import pygame

from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, target_list=None):
        closest_prey = None
        min_dist = 9999

        for ent in target_list:
            if ent.name in ["Chicken", "Bull"]:
                dist = pygame.Vector2(self.rect.center).distance_to(ent.rect.center)
                if dist < min_dist:
                    min_dist = dist
                    closest_prey = ent

        if closest_prey:
            direction = (pygame.Vector2(closest_prey.rect.center) - pygame.Vector2(self.rect.center))
            if direction.length() > 0:
                direction = direction.normalize()
                self.rect.center += direction * self.speed
        else:
            self.rect.x -= self.speed
