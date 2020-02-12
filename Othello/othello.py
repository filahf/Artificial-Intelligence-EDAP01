# http://dhconnelly.com/paip-python/docs/paip/othello.html#section-8

import random
from copy import copy, deepcopy

EMPTY, BLACK, WHITE, OUTER = '.', '\033[1;30;41m \033[0m', '\033[1;30;47m \033[0m', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)

UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

# Board


def squares():
    return [i for i in range(11, 89) if 1 <= (i % 10) <= 8]


def initial_board():
    board = [OUTER] * 100
    for i in squares():
        board[i] = EMPTY

    board[44], board[45] = WHITE, BLACK
    board[54], board[55] = BLACK, WHITE
    return board


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


def move_to_nbr(move):
    x = ord(move[:1]) - 96
    y = move[1:]
    return str(x) + y


def print_board(board):
    rep = ''
    rep += ' %s\n' % ' '.join(map(str, char_range('a', 'h')))
    for row in range(1, 9):
        begin, end = 10*row + 1, 10*row + 9
        rep += '%d %s\n' % (row, ' '.join(board[begin:end]))

    return rep

def opponent(player):
    return BLACK if player is WHITE else WHITE


def find_bracket(square, player, board, direction):
    bracket = square + direction
    if board[bracket] == player:
        return None
    opp = opponent(player)
    while board[bracket] == opp:
        bracket += direction
    return None if board[bracket] in (OUTER, EMPTY) else bracket


def is_legal(move, player, board):
    def hasbracket(direction): return find_bracket(
        move, player, board, direction)
    return board[move] == EMPTY and any(map(hasbracket, DIRECTIONS))


def make_flips(move, player, board, direction):

    bracket = find_bracket(move, player, board, direction)
    if not bracket:
        return
    square = move + direction
    while square != bracket:
        board[square] = player
        square += direction


def make_move(move, player, board):
    board[move] = player
    for d in DIRECTIONS:
        make_flips(move, player, board, d)
    return board


def legal_moves(player, board):
    return [sq for sq in squares() if is_legal(sq, player, board)]


def random_strategy(player, board):
    return random.choice(legal_moves(player, board))



SQUARE_WEIGHTS = [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0, 120, -20,  20,   5,   5,  20, -20, 120,   0,
    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
    0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0,
    0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0,
    0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0,
    0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0,
    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
    0, 120, -20,  20,   5,   5,  20, -20, 120,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
]



def weighted_score(player, board):

#

    opp = opponent(player)
    total = 0
    for sq in squares():
        if board[sq] == player:
            total += SQUARE_WEIGHTS[sq]
        elif board[sq] == opp:
            total -= SQUARE_WEIGHTS[sq]
    return total




def score(player, board):

#

    mine, theirs = 0, 0
    opp = opponent(player)
    for sq in squares():
        piece = board[sq]
        if piece == player: mine += 1
        elif piece == opp: theirs += 1
    return mine - theirs






def alpha_beta(player, board, alpha, beta, depth):
    moves = legal_moves(player, board) 
    if depth == 0 or len(moves) == 0:#omg we found a leaf
        if weighted_score(opponent(player),board) == 0:
            return [float(weighted_score(player, board)), "temp"]
        return [float(weighted_score(player, board)) / weighted_score(opponent(player),board),"temp"]

    if  opponent(player):#Minimum player
        v = [100, "move"]
        for m in moves:
            temp_board = deepcopy(board)
            make_move(m, player, temp_board)
            res = alpha_beta(WHITE, temp_board, alpha, beta,
                    depth-1)
            if v[0] > res[0]:
                v = res
                v[1] = m
                beta = min(beta, v[0])
            if beta <= alpha:
                break 
    else:#Maximum player
        v = [-100, "move"]
        for m in moves:
            temp_board = deepcopy(board)
            make_move(m, player, temp_board)
            res = alpha_beta(BLACK, temp_board, alpha, beta,
                    depth-1)
            if v[0] < res[0]:
                v = res
                v[1] = m
                alpha = max(alpha, v[0])
            if beta <= alpha:
                break
    return v



def legal_move(player, board):

#

    return any(is_legal(sq, player, board) for sq in squares())



def next_player(board, prev_player):

#

    opp = opponent(prev_player)
    if(legal_move(opp, board)):
        return opp
    elif(legal_move(prev_player, board)):
        return prev_player
    return None


def main():

    ai = 0

    for i in range(3):
        board = initial_board()
        turn = BLACK
        while turn is not None:
            
            if(turn == BLACK):
                    #print("",print_board(board))
                    move = random_strategy(BLACK, board)
                    board = make_move(move, BLACK, board)
                    turn = next_player(board,BLACK)
            if(turn == WHITE):
                    #print("",print_board(board))
                    move = alpha_beta(WHITE,board,-1000,1000,4)[1]
                    board = make_move(move, WHITE, board)
                    turn = next_player(board,WHITE)
        if(score(WHITE,board)>score(BLACK,board)):
            ai = ai + 1
        i += 1
    print("AI won", ai)
        

    


main()



