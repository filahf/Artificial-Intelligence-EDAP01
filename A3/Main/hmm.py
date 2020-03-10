
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)


# http://www.adeveloperdiary.com/data-science/machine-learning/introduction-to-hidden-markov-model/
# North, East, South, West
directions = [0, 1, 2, 3]
grid = (6, 6)

# Your transition matrix will thus have the dimensions
# (rows*columns*4) x (rows*columns*4) and you will need (rows*columns+1) observation matrices,
# each being a diagonal matrix of dimensions (rows*columns*4) x (rows*columns*4) to get the
# matrix multiplications to work out.


def out_of_bounds(move):
    if move[0] >= grid[0] or move[1] >= grid[1] or move[0] < 0 or move[1] < 0:
        return True
    else:
        return False


def init_state(width, height):
    # the initial postion of the robot. Must be on the grid somewhere with a direction-> P(X0 = i) = 1 / widht*height*directions
    whd_length = width * height * len(directions)
    i_state = [1 / whd_length] * whd_length
    return i_state


def transition_model(height, width):
    matrix = np.array(
        np.zeros(shape=(grid[0] * height * 4, grid[0] * height * 4)))

    def fill_trans_row(width, height, x, y, d, row):
        col = 0
        for n_x in range(grid[0]):
            for n_y in range(height):
                for n_d in range(4):
                    matrix[row, col] = transition_prob(
                        (x, y, d), (n_x, n_y, n_d))
                    col += 1
    row = 0
    for r in range(width):
        for c in range(height):
            for d in range(4):
                fill_trans_row(width, height, r, c, d, row)
                row += 1
    return matrix


def transition_prob(pose, new_pose):
    possible_dirs = 4
    current_x, current_y, current_dir = pose
    next_x, next_y, next_dir = new_pose
    step_dirs = [(current_x, current_y + 1), (current_x + 1, current_y), (current_x, current_y - 1),
                 (current_x - 1, current_y)]
    for i in step_dirs:
        if(out_of_bounds(i)):
            possible_dirs -= 1

    if(step_dirs[current_dir] == (next_x, next_y)):
        if(current_dir == next_dir):
            return 0.7
        elif(not out_of_bounds(step_dirs[current_dir])):
            return 1.0 / possible_dirs
        else:
            return 0.3 / (possible_dirs - 1)
    return 0.0


def get_neighbours(pose, step_size):
    x, y = pose
    result = []
    one_array = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1),
                 (x, y), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    two_array = [(x-2, y-2), (x-2, y-1), (x-2, y), (x-2, y+1), (x-2, y+2), (x-1, y-2), (x-1, y+2), (x, y-2),
                 (x, y+2), (x+1, y-2), (x+1, y+2), (x+2, y-2), (x+2, y-1), (x+2, y), (x+2, y+1), (x+2, y+2)]
    if step_size == 1:
        neigbours = one_array
    else:
        neigbours = two_array
    for move in neigbours:
        if(out_of_bounds(move) or move == pose):
            pass
        else:
            result.append(move)

    return result


def set_neighbour_prob(obs, neigbours, prob):
    for move in neigbours:
        index = move[0] * grid[0] * 4 + move[1] * 4
        for i in range(4):
            obs[index + i, index + i] = prob


def sensor_model(pose):
    obs = np.array(
        np.zeros(shape=(grid[0] * grid[1] * 4, grid[0] * grid[1] * 4)))
    x, y = pose

    index = (x * 4 * grid[1] + y * 4) + 1
    for i in range(4):
        obs[index, index] = 0.1

    set_neighbour_prob(obs, get_neighbours(pose, 1), 0.05)
    set_neighbour_prob(obs, get_neighbours(pose, 2), 0.025)

    return obs


def forward_filter(old_f, trans, sensed_cord):
    f_new = np.dot(np.dot(sensor_model(sensed_cord), trans), old_f)
    f_norm = f_new / np.sum(f_new)
    return f_new


# print(transition_model(4, 4))
# print(get_neighbours((0, 0), 2))
m = 6 * 6 * 4
probability = 1 / m
f_old = np.array([[probability] for y in range(m)])
# print(f_old)
trans = transition_model(6, 6)
print(forward_filter(f_old, trans, (0, 0)))
#print(sensor_model((1, 2)))
