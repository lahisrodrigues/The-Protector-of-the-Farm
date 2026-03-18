import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_BLACK, COLOR_WHITE
from code.Database import Database


class ScoreMenu:
    def __init__(self, window):
        self.window = window
        self.title_font = pygame.font.SysFont("Arial", 50, bold=True)
        self.font = pygame.font.SysFont("Arial", 35)

    def run(self):
        db = Database()
        top_scores = db.get_top_scores(limit=7)
        db.close()

        running = True
        while running:
            self.window.fill(COLOR_BLACK)

            title_surf = self.title_font.render("TOP 5 SCORES", True, (255, 255, 0))
            self.window.blit(title_surf, (WIN_WIDTH // 2 - title_surf.get_width() // 2, 80))

            y_offset = 200
            if not top_scores:
                no_score = self.font.render("No scores yet!", True, COLOR_WHITE)
                self.window.blit(no_score, (WIN_WIDTH // 2 - no_score.get_width() // 2, y_offset))
            else:
                for idx, (name, score, date) in enumerate(top_scores):
                    text = f"{idx + 1}. {name} - {score} pts ({date})"
                    score_surf = self.font.render(text, True, COLOR_WHITE)
                    self.window.blit(score_surf, (WIN_WIDTH // 2 - score_surf.get_width() // 2, y_offset))
                    y_offset += 60

            back_surf = self.font.render("Press ESC to return to Menu", True, (150, 150, 150))
            self.window.blit(back_surf, (WIN_WIDTH // 2 - back_surf.get_width() // 2, WIN_HEIGHT - 100))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
