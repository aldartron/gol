import pygame
from pygame import Surface
from cell import Cell


class Grid:

    def __init__(self, size, screen, settings):
        self.is_deleting = False
        self.screen = screen
        self.settings = settings
        self.size = size
        self.epoch = 0
        self.grid = []
        self.pause = True
        # Заполнение грида
        for y in range(self.size):
            row = [Cell(x, y, screen, settings) for x in range(self.size)]
            self.grid.append(row)

    def vizualize(self):
        for row in self.grid:
            for cell in row:
                cell.blitme()

        cell_size = self.settings.cell_size
        screen_height = self.settings.screen_height

        # Отрисовка сетки грида
        if self.settings.draw_grid:
            for i in range(self.settings.grid_size + 1):
                pygame.draw.line(self.screen, self.settings.grid_color, (0, i * cell_size), (screen_height, i * cell_size))
                pygame.draw.line(self.screen, self.settings.grid_color, (i * cell_size, 0), (i * cell_size, screen_height))

    def clear(self):
        # Очистка грида
        for row in self.grid:
            for cell in row:
                cell.alive = False

    def inverse(self):
        # Инверсия грида
        for row in self.grid:
            for cell in row:
                cell.alive = not cell.alive

    def start(self):
        # Запуск
        pass

