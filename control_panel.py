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
        self.content.append(Button(screen, grid, settings, 'Step' , 1))
        self.content.append(Button(screen, grid, settings, 'Faster', 3))
        self.content.append(Button(screen, grid, settings, 'Slower', 4))
        self.content.append(Button(screen, grid, settings, 'CLEAR', 6))
        self.content.append(Button(screen, grid, settings, 'Grid?', 7))
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
        # Очистка поверхности
        self.surface.fill(self.settings.button_color)
        # Отрисовка рамки
        border_width = 3
        if self.in_focus:
            border_color = self.settings.border_in_focus_color
            if self.caption == 'PAUSE':
                border_width = 7
        elif self.caption == 'PAUSE':
            border_color = self.settings.border_active_color
            border_width = 7
        else:
            border_color = self.settings.border_color
        pygame.draw.rect(self.surface, border_color, self.surface.get_rect(), border_width)
        # Отрисовка надписи
        label = self.settings.font.render(self.caption, 1, self.settings.font_color)
        labelx = self.surface.get_rect().centerx - label.get_rect().width // 2
        labely = self.surface.get_rect().centery - label.get_rect().height // 2
        self.surface.blit(label, (labelx, labely))

    def click(self, grid):
        # Вызов игровых функций для соответствующей кнопки
        if self.caption == 'START':
            gf.start(grid)
            self.caption = 'PAUSE'
        elif self.caption == 'PAUSE':
            gf.start(grid)
            self.caption = 'START'
        elif self.caption == 'CLEAR':
            gf.clear(grid)
        elif self.caption == 'EXIT':
            gf.exit(grid)
        elif self.caption == 'Step':
            gf.step(grid)
        elif self.caption == 'Grid?':
            gf.change_grid(grid)
        elif self.caption == 'Faster':
            gf.faster(grid)
        elif self.caption == 'Slower':
            gf.slower(grid)

