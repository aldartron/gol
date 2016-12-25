import pygame
from pygame import Surface
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

    def do_epoch(self):
        # Эпоха
        for row in self.grid:
            for cell in row:
                if self.count(cell) == 3:
                    cell.alive = True
                elif self.count(cell) == 2 and cell.alive:
                    cell.alive = True
                else: cell.alive = False
        print('epoch')

    def do_live(self):
        # Генерация эпох
        while (self.live):
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
        t = threading.Thread(target = self.do_live())
        t.start()
        t.join()

    def count(self, cell):
        # Подсчет количества живых соседей у клетки
        coord_deltas = [(-1,-1),(0,-1),(+1,-1),(-1,0),(+1,0),(-1,+1),(0,+1),(+1,+1)]
        neighbors = []
        result = 0

        for t in coord_deltas:
            x = list(range(self.settings.grid_size))[(cell.x + t[0]) % self.settings.grid_size]
            y = list(range(self.settings.grid_size))[(cell.y + t[1]) % self.settings.grid_size]
            neighbor = (x, y)
            neighbors.append(neighbor)

        for coord in neighbors:
            for row in self.grid:
                for cell in row:
                    if cell.x == coord[0] and cell.y == coord[1]:
                        if cell.alive:
                            result += 1

        return result



