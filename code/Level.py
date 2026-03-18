import random
import sys

import pygame

from code.Const import FPS, WIN_HEIGHT, WIN_WIDTH, GAME_TIME, INITIAL_SPAWN_INTERVAL, MIN_SPAWN_INTERVAL
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Score import Score


class Level:
    def __init__(self, window, name, clock):
        self.window = window
        self.name = name
        self.clock = clock
        self.background = pygame.image.load('./asset/GramLevel1and2.jpg').convert()
        self.entity_list = []
        self.entity_list.append(EntityFactory.get_entity("FarmerPlayer", (100, 300)))
        self.entity_list.append(EntityFactory.get_entity("Chicken", (1100, 400)))
        self.entity_list.append(EntityFactory.get_entity("Chicken", (1200, 500)))
        self.entity_list.append(EntityFactory.get_entity("FoxPredator", (1300, 300)))
        self.entity_list.append(EntityFactory.get_entity("DogPredator", (1400, 300)))
        self.score = Score()
        self.font = pygame.font.SysFont("Arial", 30)
        self.spawn_timer = 0
        self.level_timer = GAME_TIME
        self.spawn_interval = INITIAL_SPAWN_INTERVAL

        pygame.mixer.music.load('./asset/GameSound.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

    def run(self):
        level_running = True
        while level_running:
            dt = self.clock.tick(FPS)
            self.level_timer -= dt
            self.window.blit(self.background, (0, 0))

            if self.spawn_interval > MIN_SPAWN_INTERVAL:
                self.spawn_interval -= 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        farmer = self.entity_list[0]
                        if farmer and farmer.name == "FarmerPlayer":
                            self.entity_list.append(farmer.shoot())

            for ent in self.entity_list[:]:
                if ent is not None:
                    ent.move(self.entity_list)
                    self.window.blit(ent.surf, ent.rect)

                    if ent.name in ["StoneShoot", "Chicken", "Bull"]:
                        if ent.rect.bottom < -50 or ent.rect.top > WIN_HEIGHT + 50 or \
                                ent.rect.right < -50 or ent.rect.left > WIN_WIDTH + 50:
                            if ent in self.entity_list:
                                self.entity_list.remove(ent)

            self.spawn_timer += dt
            if self.spawn_timer > self.spawn_interval:
                categoria = random.choice(["PRESA", "PREDADOR", "PRESA", "PREDADOR", "PRESA", "PRESA", "PREDADOR"])
                if categoria == "PRESA":
                    animal_type = random.choice(["Chicken", "Bull"])
                    pos = (random.randint(100, 500), random.randint(156, 400))
                else:
                    animal_type = random.choice(["FoxPredator", "DogPredator"])
                    lado_x = random.choice([-50, WIN_WIDTH + 50])
                    pos = (lado_x, random.randint(50, WIN_HEIGHT - 50))

                new_ent = EntityFactory.get_entity(animal_type, pos)
                if new_ent:
                    self.entity_list.append(new_ent)
                self.spawn_timer = 0

            ent1, ent2, event_type = EntityMediator.verify_collision(self.entity_list)

            if event_type == "STRIKE":
                enemy = ent1 if "Predator" in ent1.name else ent2
                self.score.add_strike(enemy.name)
                if ent1 in self.entity_list: self.entity_list.remove(ent1)
                if ent2 in self.entity_list: self.entity_list.remove(ent2)
            elif event_type == "CAUGHT":
                if ent1.name in ["Chicken", "Bull"] and ent1 in self.entity_list:
                    self.entity_list.remove(ent1)
                elif ent2 in self.entity_list:
                    self.entity_list.remove(ent2)
                self.score.lose_animal()

            if self.level_timer <= 0:
                return self.score.points

            score_surf = self.font.render(self.score.get_score(), True, (255, 255, 255))
            self.window.blit(score_surf, (20, 20))

            time_seconds = max(0, int(self.level_timer / 1000))
            timer_surf = self.font.render(f"Time: {time_seconds}s", True, (255, 255, 0))
            self.window.blit(timer_surf, (WIN_WIDTH - 150, 20))

            pygame.display.flip()
        return None
