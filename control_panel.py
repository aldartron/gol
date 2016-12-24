import pygame
from pygame import Surface
import game_functions as gf


class Panel:

    def __init__(self, screen, grid, settings):
        self.settings = settings
        self.screen = screen
        self.content = []
        self.surface = Surface((settings.screen_width - settings.screen_height, settings.screen_height))
        self.grid = grid
        self.content.append(Button(screen, grid, settings, 'START', 0))
        self.content.append(Button(screen, grid, settings, 'Faster', 2))
        self.content.append(Button(screen, grid, settings, 'Slower', 3))
        self.content.append(Button(screen, grid, settings, 'CLEAR', 5))
        self.content.append(Button(screen, grid, settings, 'RANDOM', 6))
        self.content.append(Button(screen, grid, settings, 'INVERSE', 7))
        self.content.append(Button(screen, grid, settings, 'EXIT', 9))

    def blitme(self):
        self.surface.fill(self.settings.panel_color)
        self.screen.blit(self.surface, (self.settings.screen_height, 0))
        # Отображение элементов панели
        for element in self.content:
            element.blitme()

    def focus(self):
        for element in self.content:
            if element.area != 0:
                element.in_focus = element.area.collidepoint(pygame.mouse.get_pos())

    def click(self):
        for element in self.content:
            if element.in_focus:
                element.click(self.grid)


class Button:

    def __init__(self, screen, grid, settings, caption, index):
        self.settings = settings
        self.index = index
        self.surface = Surface((settings.screen_width - settings.screen_height - 40, settings.button_height))
        self.surface.fill(settings.button_color)
        self.caption = caption
        self.screen = screen
        self.in_focus = False
        self.area = 0

    def blitme(self):
        self.area = self.screen.blit(self.surface, (self.settings.screen_height + 20, 20 + 10 * self.index + 45 * self.index))
        # Отрисовка рамки
        if self.in_focus:
            border_color = self.settings.border_in_focus_color
        else:
            border_color = self.settings.border_color
        pygame.draw.rect(self.surface, border_color, self.surface.get_rect(), 3)
        # Отрисовка надписи
        label = self.settings.font.render(self.caption, 1, (85,85,85))
        labelx = self.surface.get_rect().centerx - label.get_rect().width // 2
        labely = self.surface.get_rect().centery - label.get_rect().height // 2
        self.surface.blit(label, (labelx, labely))

    def click(self, grid):
        # Вызов игровых функций для соответствующей кнопки
        if self.caption == 'START':
            gf.start(grid)
        elif self.caption == 'STOP':
            gf.stop(grid)
        elif self.caption == 'CLEAR':
            gf.clear(grid)
        elif self.caption == 'EXIT':
            gf.exit(grid)
        elif self.caption == 'INVERSE':
            gf.inverse(grid)

