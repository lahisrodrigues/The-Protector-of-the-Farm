from datetime import datetime

import pygame

from code.Const import WIN_WIDTH
from code.Database import Database


class GameOver:
    def __init__(self, window, score):
        self.window = window
        self.score = score
        self.font = pygame.font.SysFont("Arial", 40)
        self.player_name = ""
        self.date_str = datetime.now().strftime("%d/%m/%Y %H:%M")

    def run(self):
        pygame.mixer.music.stop()

        input_active = True
        while input_active:
            self.window.fill((0, 0, 0))

            txt_fin = self.font.render(f"GAME OVER - Score: {self.score}", True, (255, 255, 0))
            txt_date = self.font.render(f"Date: {self.date_str}", True, (200, 200, 200))
            txt_name = self.font.render(f"Enter Name: {self.player_name}", True, (255, 255, 255))
            txt_inst = self.font.render("Press ENTER to Save", True, (100, 100, 100))

            self.window.blit(txt_fin, (WIN_WIDTH // 4, 150))
            self.window.blit(txt_date, (WIN_WIDTH // 4, 220))
            self.window.blit(txt_name, (WIN_WIDTH // 4, 300))
            self.window.blit(txt_inst, (WIN_WIDTH // 4, 400))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # se o jogador não escrever nada, salva como "Anonymous"
                        if self.player_name.strip() == "":
                            self.player_name = "Anonymous"

                        db = Database()
                        db.insert_score(self.player_name, self.score, self.date_str)
                        db.close()

                        input_active = False

                    elif event.key == pygame.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    else:
                        if len(self.player_name) < 10:
                            self.player_name += event.unicode

            pygame.display.flip()

        return self.player_name
