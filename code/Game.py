import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("The Protector of the Farm")
        self.clock = pygame.time.Clock()
        self.menu = Menu(self.window)

    def run(self):
        while True:
            menu_return = self.menu.run()

            if menu_return == "NEW GAME":
                level = Level(self.window, "Level 1", self.clock)
                score_final = level.run()

                if score_final is not None:
                    from code.GameOver import GameOver
                    game_over = GameOver(self.window, score_final)
                    player_name = game_over.run()
                    print(f"Player {player_name} scored {score_final} points.")

            elif menu_return == "SCORE":
                from code.ScoreMenu import ScoreMenu
                score_menu = ScoreMenu(self.window)
                score_menu.run()

            elif menu_return == "EXIT":
                pygame.quit()
                sys.exit()
