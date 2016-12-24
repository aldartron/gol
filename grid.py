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
