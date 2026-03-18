import sys

import pygame

from code.Const import COLOR_BLACK, COLOR_WHITE, WIN_WIDTH, WIN_HEIGHT


class Menu:
    def __init__(self, window):
        self.window = window
        self.options = ["NEW GAME", "SCORE", "EXIT"]
        self.menu_index = 0

        try:
            self.bg = pygame.image.load('./asset/MenuBg.png').convert()
            self.bg = pygame.transform.scale(self.bg, (WIN_WIDTH, WIN_HEIGHT))
        except FileNotFoundError:
            self.bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
            self.bg.fill(COLOR_BLACK)

    def run(self):
        pygame.mixer.music.load('./asset/MenuSound.mp3')
        pygame.mixer.music.play(-1)

        while True:
            self.window.blit(self.bg, (0, 0))
            self.menu_text(60, "The Protector of the Farm", (255, 150, 0), (WIN_WIDTH // 2, 120))

            for i in range(len(self.options)):
                color = (255, 255, 0) if i == self.menu_index else COLOR_WHITE
                self.menu_text(40, self.options[i], color, (WIN_WIDTH // 2, 280 + i * 50))

            self.menu_text(30, "GAMES CONTROLS", (200, 200, 200), (WIN_WIDTH // 2, 520))
            self.menu_text(25, "Move: Arrow keys or W A S D keys", (255, 255, 255), (WIN_WIDTH // 2, 560))
            self.menu_text(25, "Throw the Stone: SPACE Bar", (255, 255, 255), (WIN_WIDTH // 2, 590))
            self.menu_text(25, "Menu: Use arrows to select and ENTER to confirm", (255, 255, 255),
                           (WIN_WIDTH // 2, 620))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.menu_index = (self.menu_index - 1) % len(self.options)
                    if event.key == pygame.K_DOWN:
                        self.menu_index = (self.menu_index + 1) % len(self.options)
                    if event.key == pygame.K_RETURN:
                        return self.options[self.menu_index]
                    if event.key == pygame.K_s:
                        return "NEW GAME"

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont("Arial", text_size, bold=True)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
