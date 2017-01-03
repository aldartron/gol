import pygame
from cell import Cell
import time
import threading


class Grid:

    def __init__(self, size, screen, settings):
        self.live = False
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
        if self.live:
            self.do_live()

    def do_epoch(self):
        # Эпоха
        must_die = []
        must_live = []
        for row in self.grid:
            for cell in row:
                if self.count(cell) == 3:
                    must_live.append(cell)
                elif self.count(cell) == 2 and cell.alive:
                    must_live.append(cell)
                else:
                    must_die.append(cell)
        for dead in must_die:
            dead.change(False)
        for live in must_live:
            live.change(True)
        print('epoch')

    def do_live(self):
        # Генерация эпох
        self.do_epoch()
        time.sleep(1)

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
        self.live = True

    def count(self, cell):
        # Подсчет количества живых соседей у клетки
        coord_deltas = [(-1,-1),(0,-1),(1,-1),
                        (-1, 0),       (1, 0),
                        (-1, 1),(0, 1),(1, 1)]
        neighbors = []
        result = 0

        for t in coord_deltas:
            x = cell.x + t[0]
            y = cell.y + t[1]
            neighbors.append((x,y))

        for coords in neighbors:
            for row in self.grid:
                for cell in row:
                    if cell.x == coords[0] and cell.y == coords[1]:
                        if cell.alive:
                            result += 1

        return result
