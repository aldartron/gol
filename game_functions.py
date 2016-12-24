import sys
import pygame


def check_events(grid, settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif pygame.mouse.get_pressed()[0]:
            click_on_cell(grid, settings, True)
        elif pygame.mouse.get_pressed()[2]:
            click_on_cell(grid, settings, False)
        elif event.type == pygame.MOUSEBUTTONUP:
            grid.release()
        elif pygame.mouse.get_rel():
            focus_on_cell(grid, settings)


def update_screen(settings, screen, grid):
    screen.fill(settings.bg_color)
    grid.vizualize()
    pygame.display.flip()


def click_on_cell(grid, settings, alive):
    cell = get_cell(grid, settings)
    cell.change(alive)


def focus_on_cell(grid, settings):
    cell = get_cell(grid, settings)
    if cell is not None:
        cell.focus()


def get_cell(grid, settings):
    # Определяет ячейку, над которой находится курсор
    pos = pygame.mouse.get_pos()
    if pos[0] < 600:
        y = pos[0] // settings.cell_size
        x = pos[1] // settings.cell_size
        return grid.grid[x][y]