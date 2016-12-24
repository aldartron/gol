import sys
import pygame
from settings import Settings
from grid import Grid
import game_functions as gf


def run_game():
    # Инициализация
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width,settings.screen_height)
    )
    pygame.display.set_caption("Conway's Game of Life")

    grid = Grid(settings.grid_size, screen, settings)

    # Основной цикл
    while True:
        gf.check_events(grid, settings)
        gf.update_screen(settings, screen, grid)

run_game()