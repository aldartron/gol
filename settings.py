import pygame


class Settings:

    def __init__(self):
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.font = pygame.font.SysFont('Monospace', 22, 1)
        self.grid_size = 50
        self.grid_color = (163, 163, 163)
        self.draw_grid = True
        self.cell_size = (self.screen_height // self.grid_size)
        self.cell_color = (92, 92, 92)

        self.panel_color = (163, 163, 163)
        self.button_color = self.bg_color
        self.button_height = 45
        self.border_color = (80, 80, 80)
        self.border_in_focus_color = (180, 80, 80)
