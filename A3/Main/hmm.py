

import numpy as np
# http://www.adeveloperdiary.com/data-science/machine-learning/introduction-to-hidden-markov-model/

# Your transition matrix will thus have the dimensions
# (rows*columns*4) x (rows*columns*4) and you will need (rows*columns+1) observation matrices,
# each being a diagonal matrix of dimensions (rows*columns*4) x (rows*columns*4) to get the
# matrix multiplications to work out.
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
directions = [NORTH, EAST, SOUTH, WEST]


def transition_matrix(width, height):
    t_matrix = np.array(width*height*4)


def possible_transitions(width, height, x, y, direction):
    neighbors = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
    transitions = []

    can_go_forward = True

    x_coord, y_coord = neighbors[direction]
    if not 0 <= y_coord < height or not 0 <= x_coord < width:
        can_go_forward = False

    for d, (x_coord, y_coord) in enumerate(neighbors):
        if not 0 <= y_coord < height or not 0 <= x_coord < width:
            # The neighbor is out of the grid
            continue
        else:
            if d == direction:
                transitions.append(((x_coord, y_coord, d), 0.7))
            else:
                if can_go_forward:
                    p = 0.3
                else:
                    p = 1.0
                transitions.append(((x_coord, y_coord, d), p))

    if can_go_forward:
        transitions = [(pos, p / (len(transitions) - 1))
                       if p != 0.7 else (pos, p) for pos, p in transitions]
    else:
        transitions = [(pos, p / len(transitions))
                       for pos, p in transitions]

    return transitions


def obs_matrix(width, height):
    # Rows*columns+1 matrixes
    # (rows*columns*4)x(rows*columns*4)
    obs = np.array(np.zeros((width*height*4, width*height*4)))
    for x in range(width):
        for y in range(height):
            for direction in directions:
                # State at time t-1
                i = x * height * 4 + y * 4 + direction
                print(i)

                # Possible states at time t+1
                poss_trans = possible_transitions(
                    width, height, x, y, direction)
                #print("poss_trans", poss_trans)
                for (px, py, pd), prob in poss_trans:
                    #print("px", px, py, pd)
                    j = px * height * 4 + py * 4 + pd

                    obs[i, j] = prob
    print(obs)


print(obs_matrix(2, 2))
