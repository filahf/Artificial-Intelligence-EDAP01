NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
directions = [NORTH, EAST, SOUTH, WEST]

# step 1 or 2


def sorrounding_pos(pos, step):
    x, y = pos[0], pos[1]
    pos_array = [(x-step, y-step), (x-step, y), (x-step, y+step), (x, y-step),
                 (x, y), (x, y+step), (x+step, y-step), (x+step, y), (x+step, y+step)]
    next_pos = random.choice(pos_array)
    # check for walls
    return next_pos


def wall_close(pos, direction, grid):
    x, y = pos[0], pos[1]
    width, height = grid
    check_pos = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
    next_pos = check_pos[direction]
    if next_pos[0] >= width or next_pos[1] >= height:
        return True
    elif next_pos[0] < 0 or next_pos[1] < 0:
        return True
    else:
        return False
