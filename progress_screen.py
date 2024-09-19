import progress_consts
import pygame
import tkinter as tk

SCREEN_SIZE = (1000, 1000)
pygame.init()


def screen_settings(size):
    screen = pygame.display.set_mode(size)
    return screen


def draw_maze_image(location, screen):
    maze = progress_consts.MAZE_IMG.get_rect(topleft=(location))
    screen.blit(progress_consts.MAZE_IMG, maze)


def draw_images(screen):
    for i in range(len(progress_consts.IMAGES)):
        draw_maze_image(((i + 1) * progress_consts.DISTANCE, progress_consts.WINDOW_WIDTH / 2), screen)


def draw_soldier(location, screen):
    soldier = progress_consts.SOLDIER_IMG.get_rect(
        bottomleft=(location))
    screen.blit(progress_consts.SOLDIER_IMG, soldier)


def draw_screen(state):
    state["screen"].fill(progress_consts.BACKGROUND)
    draw_images(state["screen"])
    draw_soldier(state["soldier_location"], state["screen"])
    pygame.display.flip()


def draw_massage(massage, font_size, text_color, location, screen):
    screen.fill(progress_consts.POP_UP_COLOR)
    font = pygame.font.SysFont(progress_consts.FONT_NAME, font_size, bold=True)
    text_img = font.render(massage, True, text_color)
    text_width = text_img.get_width()
    text_height = text_img.get_height()
    location_x = location[0] - text_width / 2
    location_y = location[1] - text_height / 2
    screen.blit(text_img, (location_x, location_y))
    pygame.display.flip()


def draw_tk(text):
    root = tk.Tk()
    T = tk.Text(root, height=70, width=150)
    T.grid(row=0, column=0)
    T.insert(tk.END, text)

    button = tk.Button(root, text="enter game", command=root.destroy)
    button.grid(row=0, column=1)

    tk.mainloop()
