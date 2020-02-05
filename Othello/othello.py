# http://dhconnelly.com/paip-python/docs/paip/othello.html#section-8

import random

EMPTY, RED, WHITE, OUTER = '.', '\033[1;30;41m \033[0m', '\033[1;30;47m \033[0m', '?'
PIECES = (EMPTY, RED, WHITE, OUTER)

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

    board[44], board[45] = WHITE, RED
    board[54], board[55] = RED, WHITE
    return board


def print_board(board):

    rep = ''
    rep += ' %s\n' % ' '.join(map(str, range(1, 9)))
    for row in range(1, 9):
        begin, end = 10*row + 1, 10*row + 9
        rep += '%d %s\n' % (row, ' '.join(board[begin:end]))

    return rep

# Contro


def opponent(player):
    return RED if player is WHITE else WHITE


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


board = initial_board()


# for x in range(32):
#     print(print_board(board))
#     move = random_strategy(RED, board)
#     board = make_move(move, RED, board)
#     print(print_board(board))
#     move = random_strategy(WHITE, board)
#     board = make_move(move, WHITE, board)

while(legal_moves(RED,board) != None):
    print(print_board(board))
    move = random_strategy(RED, board)
    board = make_move(move, RED, board)
    print(print_board(board))
    move = random_strategy(WHITE, board)
    board = make_move(move, WHITE, board)

