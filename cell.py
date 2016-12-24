import pygame
from pygame import Surface


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
