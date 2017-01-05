import pygame
import time
import threading
from game_functions import coord_deltas


class Grid:

    def __init__(self, size, screen, settings):
        self.live = False
        self.screen = screen
        self.settings = settings
        self.size = size
        self.epoch = 0
        self.cols = []
        self.neighbors_grid = []

        # Заполнение грида
        for y in range(self.size):
            self.cols.append([False for x in range(self.size)])
            self.neighbors_grid.append([[] for x in range(self.size)])

        # Заполнение таблицы соседей
        for col in range(self.size):
            for row in range(self.size):
                for t in coord_deltas:
                    x = list(range(self.size))[(col + t[0]) % self.size]
                    y = list(range(self.size))[(row + t[1]) % self.size]
                    self.neighbors_grid[col][row].append((x,y))


    def vizualize(self):
        cell_size = self.settings.cell_size
        screen_height = self.settings.screen_height

        # Отрисовка живых ячеек
        for x in range(self.size):
            for y in range(self.size):
                if self.cols[x][y]:
                    pygame.draw.rect(self.screen, self.settings.cell_color,
                                     ((y * cell_size, x * cell_size), (cell_size, cell_size)))

        # Отрисовка сетки грида
        if self.settings.draw_grid:
            for i in range(self.size + 1):
                pygame.draw.line(self.screen, self.settings.grid_color, (0, i * cell_size), (screen_height, i * cell_size))
                pygame.draw.line(self.screen, self.settings.grid_color, (i * cell_size, 0), (i * cell_size, screen_height))

    def change_cell(self, x, y, alive):
        self.cols[x][y] = alive

    def start(self):
        # Запуск
        self.live = True
        self.do_live()

    def clear(self):
        # Очистка грида
        for x in range(self.size):
            for y in range(self.size):
                self.cols[x][y] = False

    def inverse(self):
        # Инверсия грида
        for x in range(self.size):
            for y in range(self.size):
                self.cols[x][y] = not self.cols[x][y]

    def count(self, col, row):
        # Подсчет количества живых соседей у клетки
        neighbors = []
        result = 0

        for neighbor in self.neighbors_grid[col][row]:
            if self.cols[neighbor[0]][neighbor[1]]:
                result += 1

        return result

    def do_epoch(self):
        # Реализация одной эпохи
        self.epoch += 1
        must_die = []
        must_live = []
        for x in range(self.size):
            for y in range(self.size):
                n = self.count(x, y)
                if n == 3:
                    must_live.append((x,y))
                elif n == 2 and self.cols[x][y]:
                    must_live.append((x,y))
                else:
                    must_die.append((x,y))

        for dead in must_die:
            self.cols[dead[0]][dead[1]] = False
        for live in must_live:
            self.cols[live[0]][live[1]] = True

    def do_live(self):
        # Последовательное выполнение эпох
        if self.live:
            self.do_epoch()