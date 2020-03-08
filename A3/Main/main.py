import random
from random import choices
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
directions = [NORTH, EAST, SOUTH, WEST]

# step 1 or 2


def grid(width, height):
    robot_loc = random.randint(0, width - 1), random.randint(0, height - 1)
    robot_dir = random.choice(directions)


def surrounding_pos(pos, step):
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


# def move robot
'''     
        # prob 0.3 to change direction.
        rand = random.random()
        if rand <= 0.3:
            self.robot_dir = Direction.random(self.robot_dir)
        while self.robot_faces_wall():
            self.robot_dir = Direction.random(self.robot_dir)

        x, y = self.robot_location

        # NORTH, EAST, SOUTH, WEST
        next_locations = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        self.robot_location = next_locations[self.robot_dir]
 '''

# -----------------------------------------------------------
# MR. ROBOT


def sensor():
    population = [true_loc, surr_pos_1, surr_pos_2, None]
    weights = [0.1, 0.05 * 8, 0.025 * 16, 0.1]

    print(choices(population, weights))


sensor()
