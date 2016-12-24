import pygame
from pygame import Surface
from settings import Settings


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

    def release(self):
        for row in self.grid:
            for cell in row:
                cell.is_changed = False
        print('release')


class Cell:

    def __init__(self, x, y, screen, settings):
        self.is_changed = False
        self.alive = False
        self.settings = settings
        self.screen = screen
        self.x = x
        self.y = y
        self.size = self.settings.cell_size
        self.surface = Surface((self.size, self.size))

    def blitme(self):
        if self.alive:
            self.surface.fill(self.settings.cell_color)
        else:
            self.surface.fill(self.settings.bg_color)
        self.screen.blit(self.surface, (
            self.x * self.size, self.y * self.size
        ))

    def change(self, alive):
        self.alive = alive

    def focus(self):
        print(self.surface.get_rect())
        pygame.draw.rect(self.surface, (0,0,0), self.surface.get_rect(), 3)
        print('draw rect')