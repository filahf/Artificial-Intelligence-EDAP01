
import numpy as np
import random


# http://www.adeveloperdiary.com/data-science/machine-learning/introduction-to-hidden-markov-model/
# North, East, South, West
directions = [0, 1, 2, 3]
grid = (8, 8)

# Your transition matrix will thus have the dimensions
# (rows*columns*4) x (rows*columns*4) and you will need (rows*columns+1) observation matrices,
# each being a diagonal matrix of dimensions (rows*columns*4) x (rows*columns*4) to get the
# matrix multiplications to work out.


def out_of_bounds(move):
    if move[0] >= grid[0] or move[1] >= grid[1] or move[0] < 0 or move[1] < 0:
        return True
    else:
        return False


def init_state():
    # the initial postion of the robot. Must be on the grid somewhere with a direction-> P(X0 = i) = 1 / widht*height*directions
    whd_length = grid[0] * grid[1] * len(directions)
    probability = 1 / whd_length
    init_state = np.array([[probability] for y in range(whd_length)])
    return init_state


def transition_model():
    matrix = np.array(
        np.zeros(shape=(grid[0] * grid[1] * 4, grid[0] * grid[1] * 4)))
    width, height = grid

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
    return obs


def sensor_model(pose):
    obs = np.array(
        np.zeros(shape=(grid[0] * grid[1] * 4, grid[0] * grid[1] * 4)))
    if(pose is None):
        for i in range(grid[0]):
            for j in range(grid[1]):
                index = 4*i*grid[1]+4*j
                if j == 0 or j == grid[1]-1:
                    if i == 0 or i == grid[0]-1:
                        for k in range(4):
                            obs[index + k, index+k] = 0.625
                    else:
                        for k in range(4):
                            obs[index + k, index+k] = 0.5
                elif i == 0 or k == grid[1]-1:
                    for k in range(4):
                        obs[index + k, index+k] = 0.5
                else:
                    for k in range(4):
                        obs[index + k, index+k] = 0.325
    else:
        x, y = pose

        index = (x * 4 * grid[1] + y * 4) + 1
        for i in range(4):
            obs[index, index] = 0.1

        set_neighbour_prob(obs, get_neighbours(pose, 1), 0.05)
        set_neighbour_prob(obs, get_neighbours(pose, 2), 0.025)

    return obs


def manhattan_distance(pose, sensed_posed):
    max = abs(pose[0]-sensed_posed[0])
    if abs(pose[1]-sensed_posed[1]) > max:
        max = abs(pose[1]-sensed_posed[1])
    return max


def forward_filter(sensed_cord, old_f=None):
    if(old_f is None):
        old_f = init_state()

    trans = transition_model()
    f_new = np.dot(np.dot(sensor_model(sensed_cord), trans), old_f)
    f_norm = f_new / np.sum(f_new)

    index = np.argmax(f_norm)
    x = (index // 4) // grid[1]
    y = (index // 4) % grid[1]
    return (x, y), f_norm


#print(forward_filter(f_old, trans, (0, 0)))
# print(forward_filter((None)))
