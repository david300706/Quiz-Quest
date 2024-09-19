import FG_consts
import random as nd


# import screen
# import soldier

def create():
    # creates the grid for the game
    game_field_grid = []
    for row in range(FG_consts.GRID_HEIGHT):
        game_field_grid.append([])
        for col in range(FG_consts.GRID_WIDTH):
            game_field_grid[row].append("SAFE")
    game_field_grid, mines = mine_spread(game_field_grid)
    return game_field_grid, mines


def mine_spread(game_field):
    # spreads mines randomly across the map
    game_field_grid = game_field
    mine_amount = 0
    mines = []
    while mine_amount != FG_consts.AMOUNT_MINE:
        num1 = nd.randint(3, 47)
        num2 = nd.randint(2, 24)
        while game_field_grid[num2][num1] != "mine" and game_field_grid[num2][num1 - 1] != "mine" and \
                game_field_grid[num2][num1 + 1] != "mine":
            game_field_grid[num2][num1] = "mine"
            game_field_grid[num2][num1 - 1] = "mine"
            game_field_grid[num2][num1 + 1] = "mine"
            mines.append([num1, num2])
        mine_amount += 1
    return game_field_grid, mines


def bush_spread():
    # spreads bushes across the whole map
    bush_cords = []
    for i in range(20):
        num1 = nd.randint(0, FG_consts.SCREEN_HEIGHT - FG_consts.GRASS_HEIGHT * FG_consts.FRAME_HEIGHT)
        num2 = nd.randint(1, FG_consts.SCREEN_WIDTH - FG_consts.GRASS_WIDTH * FG_consts.FRAME_WIDTH)
        bush_cords.append((num2, num1))
    return bush_cords
