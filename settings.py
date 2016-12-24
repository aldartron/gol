import pygame


class Settings:

    def __init__(self):
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.font = pygame.font.SysFont("monospace", 16)
        self.grid_size = 20
        self.cell_size = (self.screen_height // self.grid_size)
        self.cell_color = (80, 80, 80)
