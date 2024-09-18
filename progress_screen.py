import progress_consts
import pygame

SCREEN_SIZE = (1500, 1500)

def screen_settings(size):
    screen = pygame.display.set_mode(size)
    return screen


def draw_maze_image(location, screen):
    maze = progress_consts.MAZE_IMG.get_rect(
        topleft=(location))
    screen.blit(progress_consts.MAZE_IMG, maze)


def draw_images(screen):
    for i in range(len(progress_consts.IMAGES)):
        draw_maze_image((i + 1) * progress_consts.DISTANCE, screen)


def draw_soldier(location, screen):
    soldier = progress_consts.SOLDIER_IMG.get_rect(
        topleft=(location))
    screen.blit(progress_consts.SOLDIER_IMG, soldier)


def draw_screen(state):
    state["screen"].fill(progress_consts.BACKGROUND)
    draw_images(state["screen"])
    draw_soldier(state["soldier_location"], state["screen"])
    pygame.display.flip()


screen_settings(SCREEN_SIZE)