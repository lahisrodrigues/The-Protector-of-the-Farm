from code.Entity import Entity


class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple, direction):
        super().__init__(name, position)
        self.direction = direction

    def move(self, target_list=None):
        self.rect.center += self.direction * self.speed
