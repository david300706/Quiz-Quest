import consts
import maze_main
import screen
import pygame

state = {"player_location": [2, 2]}




# def user_events():
#     pygame.init()
#     global state
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#
#         if event.type == pygame.KEYDOWN:
#
#             if event.key == pygame.K_UP:
#                 print(state["player_location"])
#                 state["player_location"][1] -= 1
#
#             if event.key == pygame.K_DOWN:
#                 print(state["player_location"])
#                 state["player_location"][1] += 1
#
#             if event.key == pygame.K_RIGHT:
#                 print(state["player_location"])
#                 state["player_location"][0] += 1
#
#             if event.key == pygame.K_LEFT:
#                 print(state["player_location"])
#                 state["player_location"][0] -= 1
# user_events()