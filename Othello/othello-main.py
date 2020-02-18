

import random
import math


EMPTY, BLACK, WHITE, OUTER = '.', '\033[1;30;41m \033[0m', '\033[1;30;47m \033[0m', ''
DIRECTIONS = (-11, -10, -9, -1, 1, 9, 10, 11)

def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def move_to_nbr(move):
    x = ord(move[:1]) - 96
    y = move[1:]
    return str(x) + y

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
    rep += '  %s\n' % ' '.join(map(str, char_range('a', 'h')))
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
    return [square for square in squares() if is_legal(square, player, board)]


def any_legal_move(player, board):
    return any(is_legal(square, player, board) for square in squares())


def next_player(board, prev_player):
    opp = opponent(prev_player)
    if any_legal_move(opp, board):
        return opp
    elif any_legal_move(prev_player, board):
        return prev_player
    return None


def score(player, board):
    player1 = 0
    player2 = 0
    opp = opponent(player)
    for square in squares():
        piece = board[square]
        if piece == player:
            player1 += 1
        elif piece == opp:
            player2 += 1
    return player1 - player2


def final_value(player, board):

    score_diff = score(player, board)
    if(score_diff < 0):
        return -math.inf
    elif(score_diff > 0):
        return math.inf
    elif(score_diff == 0):
        return 0


def random_strategy(player, board):
    return random.choice(legal_moves(player, board))


def alphabeta(player, board, alpha, beta, depth):
    # Find the best move, for PLAYER
    # searching depth levels deep and backing up values,
    # using cutoffs whenever possible."

    if depth == 0:
        return score(player, board), "null"

    def value(board, alpha, beta):
        return -alphabeta(opponent(player), board, -beta, -alpha, depth-1)[0]
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

            print(print_board(board), end='\r')
            if(turn == BLACK):
                move = random_strategy(BLACK, board)
                board = make_move(move, BLACK, board)
                turn = next_player(board, BLACK)
            if(turn == WHITE):
                #print(print_board(board))
                move = alphabeta(WHITE, board, -math.inf,
                                 math.inf, 7)[1]
                board = make_move(move, WHITE, board)
                turn = next_player(board, WHITE)
        if(score(WHITE, board) > score(BLACK, board)):
            print("AI won")
            ai = ai + 1
        #print(print_board(board))
        i += 1
        print("game",i)
    print("AI won", ai)


main()
