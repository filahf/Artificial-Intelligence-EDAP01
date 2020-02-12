

import random
import math


EMPTY, BLACK, WHITE, OUTER = '.', '\033[1;30;41m \033[0m', '\033[1;30;47m \033[0m', ''
DIRECTIONS = (-11, -10, -9, -1, 1, 9, 10, 11)


def squares():
    return [i for i in range(11, 89) if 1 <= (i % 10) <= 8]


def initial_board():
    board = [OUTER] * 100
    for i in squares():
        board[i] = EMPTY
    board[44], board[45] = WHITE, BLACK
    board[54], board[55] = BLACK, WHITE
    return board


def print_board(board):
    rep = ''
    rep += '  %s\n' % ' '.join(map(str, range(1, 9)))
    for row in range(1, 9):
        begin, end = 10*row + 1, 10*row + 9
        rep += '%d %s\n' % (row, ' '.join(board[begin:end]))
    return rep


def is_valid(move):
    return isinstance(move, int) and move in squares()


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


def make_move(move, player, board):
    board[move] = player
    for d in DIRECTIONS:
        make_flips(move, player, board, d)
    return board


def make_flips(move, player, board, direction):
    bracket = find_bracket(move, player, board, direction)
    if not bracket:
        return
    square = move + direction
    while square != bracket:
        board[square] = player
        square += direction


def legal_moves(player, board):
    return [sq for sq in squares() if is_legal(sq, player, board)]


def any_legal_move(player, board):
    return any(is_legal(sq, player, board) for sq in squares())


def next_player(board, prev_player):
    opp = opponent(prev_player)
    if any_legal_move(opp, board):
        return opp
    elif any_legal_move(prev_player, board):
        return prev_player
    return None


def score(player, board):
    mine, theirs = 0, 0
    opp = opponent(player)
    for sq in squares():
        piece = board[sq]
        if piece == player:
            mine += 1
        elif piece == opp:
            theirs += 1
    return mine - theirs


def final_value(player, board):

    diff = score(player, board)
    if diff < 0:
        return -math.inf
    elif diff > 0:
        return math.inf
    return diff


def random_strategy(player, board):
    return random.choice(legal_moves(player, board))


def alphabeta(player, board, alpha, beta, depth, evaluate):
    if depth == 0:
        return evaluate(player, board), "null"

    def value(board, alpha, beta):
        return -alphabeta(opponent(player), board, -beta, -alpha, depth-1, evaluate)[0]
    moves = legal_moves(player, board)
    if not moves:
        if not any_legal_move(opponent(player), board):
            return final_value(player, board), "null"
        return value(board, alpha, beta), "null"

    best_move = moves[0]
    for move in moves:
        if alpha >= beta:
            break
        val = value(make_move(move, player, list(board)), alpha, beta)
        if val > alpha:
            alpha = val
            best_move = move
    return alpha, best_move


def main():

    ai = 0

    for i in range(1):
        board = initial_board()
        turn = BLACK
        while turn is not None:

            if(turn == BLACK):
                print(print_board(board))
                move = random_strategy(BLACK, board)
                board = make_move(move, BLACK, board)
                turn = next_player(board, BLACK)
            if(turn == WHITE):
                print(print_board(board))
                move = alphabeta(WHITE, board, -math.inf,
                                 math.inf, 7, score)[1]
                board = make_move(move, WHITE, board)
                turn = next_player(board, WHITE)
        if(score(WHITE, board) > score(BLACK, board)):
            print("AI won")
            ai = ai + 1
        i += 1
        print(print_board(board))
        print(i)
    print("AI won", ai)


main()
