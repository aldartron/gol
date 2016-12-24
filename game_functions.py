import sys
import pygame


def check_events(grid, settings, panel):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif pygame.mouse.get_pos()[0] < 600:
            # Если курсор в пределах грида
            if pygame.mouse.get_pressed()[0]:
                click_on_cell(grid, settings, True)
            elif pygame.mouse.get_pressed()[2]:
                click_on_cell(grid, settings, False)
        elif pygame.mouse.get_rel():
            panel.focus()
            if event.type == pygame.MOUSEBUTTONUP:
                panel.click()


def update_screen(settings, screen, grid, panel):
    screen.fill(settings.bg_color)
    grid.vizualize()
    panel.blitme()
    pygame.display.flip()


def click_on_cell(grid, settings, alive):
    cell = get_cell(grid, settings)
    cell.change(alive)


def get_cell(grid, settings):
    # Определяет ячейку, над которой находится курсор
    pos = pygame.mouse.get_pos()
    if pos[0] < 600:
        y = pos[0] // settings.cell_size
        x = pos[1] // settings.cell_size
        return grid.grid[x][y]


# Функции кнопок
def start(grid):
    grid.start()


def stop(grid):
    pass


def clear(grid):
    grid.clear()


def exit(grid):
    sys.exit()


def inverse(grid):
    grid.inverse()