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
    grid.do_live()
    panel.blitme()
    pygame.display.flip()


def click_on_cell(grid, settings, alive):
    pos = pygame.mouse.get_pos()
    y = pos[0] // settings.cell_size
    x = pos[1] // settings.cell_size
    grid.change_cell(x, y, alive)


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