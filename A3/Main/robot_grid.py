import random
from random import choices
# North, East, South, West
directions = [0, 1, 2, 3]

grid = (0, 0)
robot_loc = (0, 0)
robot_dir = 0


def grid(width, height):
    global robot_loc
    global robot_dir
    global grid
    grid = (width, height)
    robot_loc = random.randint(0, width - 1), random.randint(0, height - 1)
    robot_dir = random.choice(directions)
    return robot_loc, robot_dir


def surrounding_pos(step_size):
    x, y = robot_loc
    one_array = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1),
                 (x, y), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    two_array = [(x-2, y-2), (x-2, y-1), (x-2, y), (x-2, y+1), (x-2, y+2), (x-1, y-2), (x-1, y+2), (x, y-2),
                 (x, y+2), (x+1, y-2), (x+1, y+2), (x+2, y-2), (x+2, y-1), (x+2, y), (x+2, y+1), (x+2, y+2)]
    if step_size is 1:
        pos_array = one_array
    else:
        pos_array = two_array
    next_pos = random.choice(pos_array)
    if(facing_wall(next_pos)):
        return None
    else:
        return next_pos


def out_of_bounds(move):
    if move[0] >= grid[0] or move[1] >= grid[1]:
        return True
    elif move[0] < 0 or move[1] < 0:
        return True
    else:
        return False


def facing_wall(move=None):
    if(move != None):
        next_pos = move
    else:
        x, y = robot_loc[0], robot_loc[1]
        width, height = grid
        check_pos = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        next_pos = check_pos[robot_dir]

    return out_of_bounds(next_pos)


def move_robot():
    global robot_loc
    global robot_dir
    # P( h_t+1 != h_t | not encountering a wall) = 0.3
    cases = ["change_dir", None]
    weights = [0.3, 0.7]
    prop = choices(cases, weights)
    if(prop == "change_dir"):
        robot_dir = random.choice(directions)
    # P( h_t+1 != h_t | encountering a wall) = 1.0
    while facing_wall():
        robot_dir = random.choice(directions)
    x, y = robot_loc[0], robot_loc[1]
    step_dirs = [(x, y + 1), (x + 1, y), (x, y - 1),
                 (x - 1, y)]  # Fixa det här
    robot_loc = step_dirs[robot_dir]
    print("Robot moved to ", robot_loc, " from ", x, y)


def sensor():
    # true_loc, surr_pos_1, surr_pos_2, None
    cases = [0, 1, 2, None]
    weights = [0.1, 0.4, 0.4, 0.1]
    prop = choices(cases, weights)
    if(prop[0] == 0):
        return robot_loc
    elif(prop[0] == 1):
        return surrounding_pos(1)
    elif(prop[0] == 2):
        return surrounding_pos(2)
    else:
        return None


grid(4, 4)

print("current robot pos", robot_loc, "sensor thinks", sensor())
print(move_robot())
print("current robot pos", robot_loc, "sensor thinks", sensor())
