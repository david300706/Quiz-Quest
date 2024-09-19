import FG_consts
import FG_guard
import FG_soldier
import FG_gamefield
import pygame
import FG_screen
import time
import math
import consts
import database
import scroll

state = {"bushes": FG_gamefield.bush_spread(),
         "game_running": True,
         "soldier_location": [0, 0],
         "soldier_feet_location": [[], []],
         "guard_location": FG_consts.GUARD_START,
         "guard_forward": False,
         "game_field": None,
         "show_mines": False,
         "is_winning": False,
         "is_losing": False,
         "is_eaten": False,
         "next_fact": 0
         }


def main(data):
    pygame.init()
    state["game_field"], state["mines"] = FG_gamefield.create()
    user_events()
    state["screen"] = FG_screen.screen()
    FG_screen.draw_start_massage(state["screen"])

    pygame.display.update()
    time.sleep(1)
    lives = 3
    while state["game_running"]:
        user_events()

        if state["is_losing"] or state["is_eaten"]:

            if state["next_fact"] + 1 <= len(data):
                scroll.draw_scroll(consts.SCROLL_, state["screen"], (300, 200))

                rows_amount = math.ceil(len(data[state["next_fact"]]) / FG_consts.ONE_LINE_LENGTH)
                print(rows_amount)


                for i in range(rows_amount - 1):
                    print(data[state["next_fact"]][:50 * i + 1])
                    FG_screen.draw_message(data[state["next_fact"]][:50 * (i + 1)], 20, FG_consts.NIGHT_COLOR, (500, 450 + i * 14),
                                           state["screen"])
                print(data[state["next_fact"]][50 * (rows_amount - 1):])
                FG_screen.draw_message(data[state["next_fact"]][50 * (rows_amount - 1):], 20, FG_consts.NIGHT_COLOR, (500, 450 + (rows_amount - 1) * 14),
                                       state["screen"])


                FG_screen.print_lost(state["screen"])

                time.sleep(3)
                state["next_fact"] += 1
            else:
                FG_screen.print_lost(state["screen"])
                state["game_running"] = False

            state["soldier_location"] = [0, 0]
            lives -= 1
        elif state["is_winning"]:
            FG_screen.print_won(state["screen"])
            state["game_running"] = False

        if state["show_mines"]:
            FG_screen.show_mines(state)
            state["show_mines"] = False
            time.sleep(1)
        else:
            FG_screen.draw_game(state)

        state["is_losing"] = FG_soldier.is_eliminated(state)
        state["is_winning"] = FG_soldier.is_winning(state)
        state["is_eaten"] = FG_guard.guard_eat(state)
        FG_soldier.get_soldier_body(state["soldier_location"])

        FG_soldier.soldier_feet_cords(state["soldier_location"])
        state["guard_location"], state["guard_forward"] = FG_guard.guard_movement(state["guard_location"],
                                                                                  state["guard_forward"])


time_down = 0
number_to_save = 0


def user_events():
    pygame.init()
    global time_down
    global number_to_save
    global state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                state["show_mines"] = True

            if event.key == pygame.K_UP and state["soldier_location"][1] > 0:
                state["soldier_location"][1] -= 1

            if event.key == pygame.K_DOWN and state["soldier_location"][
                1] < FG_consts.GRID_HEIGHT - FG_consts.SOLDIER_HEIGHT:
                state["soldier_location"][1] += 1

            if event.key == pygame.K_RIGHT and state["soldier_location"][
                0] < FG_consts.GRID_WIDTH - FG_consts.SOLDIER_WIDTH:
                state["soldier_location"][0] += 1

            if event.key == pygame.K_LEFT and state["soldier_location"][0] > 0:
                state["soldier_location"][0] -= 1

            # if event.key in FG_consts.keys_to_save:
            #     time_down = pygame.time.get_ticks()
            #     number_to_save = FG_consts.keys_to_save.get(event.key)

        # elif event.type == pygame.KEYUP:
        #     if event.key in FG_consts.keys_to_save:
        #         time_to_release = pygame.time.get_ticks()
        #
        #         is_over_second = (time_to_release - time_down) / 1000
        #
        #         if int(is_over_second) < 1:
        #             FG_database.create_df(number_to_save, state)
        #
        #         else:
        #             state = database.retrieve_state(number_to_save, state)
        #
        #         time_down = 0
        #         number_to_save = 0


facts = [
    "Honey never spoils.",
    "Bananas are berries, but strawberries aren't."]

main(facts)
