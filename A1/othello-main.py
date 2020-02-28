

import random
import math
import time
# Based on Peter Norvigs Paradigms of Artificial Intelligence and Daniel Connellys implemenation

EMPTY, BLACK, WHITE, OUTER = '.', '\033[1;30;41m \033[0m', '\033[1;30;47m \033[0m', ''
DIRECTIONS = (-11, -10, -9, -1, 1, 9, 10, 11)
max_time = 0

def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def move_to_int(move):
    y = ord(move[:1]) - 96
    x = move[1:]
    return int(x + str(y))

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
    if(player is BLACK):
        return WHITE
    return BLACK


def find_bracket(square, player, board, direction):
    bracket = square + direction
    if board[bracket] == player:
        return None
    opp = opponent(player)
    while board[bracket] == opp:
        bracket += direction
    return None if board[bracket] in (OUTER, EMPTY) else bracket


def is_legal(move, player, board):
    def bracket(direction): return find_bracket(
        move, player, board, direction)
    return board[move] == EMPTY and any(map(bracket, DIRECTIONS))


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
    player_score = board.count(player)
    opp_score = board.count(opponent(player))
    return player_score - opp_score




def final_value(player, board):

    score_diff = score(player, board)
    if(score_diff < 0):
        return -math.inf
    elif(score_diff > 0):
        return math.inf
    elif(score_diff == 0):
        return 0

# According to Peter Norvigs Paradigms of Artificial Intelligence page 
def alpha_beta(player, board, alpha, beta, depth, max_time):
    if depth == 0 or time.time() >= max_time:
        return score(player, board), "no move available"

    moves = legal_moves(player, board)
    if not moves:
        if not any_legal_move(opponent(player), board):
            return final_value(player, board), "null"
        return -alpha_beta(opponent(player), board, -beta, -alpha, depth-1, max_time)[0], "no move available"

    best_move = moves[0]

    for move in moves:
        if alpha >= beta:
            break
        val = -alpha_beta(opponent(player), make_move(move, player, list(board)), -beta, -alpha, depth-1, max_time)[0]
        if val > alpha:
            alpha = val
            best_move = move
    return alpha, best_move

def available_human_moves(player,board):
    arr = legal_moves(player,board)
    chars = "abcdefgh"
    movs = []
    for i in arr:
        move = str(i)
        x = chars[int(move[1])-1]
        y = str(move[0])
        movs.append(x+y)
    return movs

def get_winner(board):
    print("--------FINAL BOARD------")
    print(print_board(board))
    print("W: ", board.count(WHITE), "  B: ", board.count(BLACK))
    if(score(WHITE, board) > score(BLACK, board)):
        return "White won"
    elif(score(WHITE, board) == score(BLACK, board)):
        return "DRAW"
    else:
        return "Black won"
                

def player_move(player,board):
    print(print_board(board))
    print("You are playing as "+ player + ", your turn!")
    print("Available moves are: ", available_human_moves(player,board))
    move = input("Enter move ")
    if(move not in available_human_moves(player,board)):
        print("Illegal move, try again")
        move = input("Enter move ")
    board = make_move(move_to_int(move),player,board)
    turn = next_player(board,player)
    return board, turn




def main():
    board = initial_board()
    player_input = input("Choose color b/w: ")
    global max_time
    max_time = int(input("How long do you want to wait in seconds before the computer makes a move? "))
    player = EMPTY
    if(player_input == "b"):
        player = BLACK
    elif(player_input == 'w'):
        player = WHITE
        print("in w",player)
    ai = opponent(player)
    turn = BLACK
    while(True):
        if(turn == BLACK):
            if(ai == BLACK):
                move = alpha_beta(BLACK, board, -math.inf,math.inf, 7, time.time() + max_time)[1]
                board = make_move(move,BLACK,board)
                turn = next_player(board,BLACK)
                print("--------------------------------------------")
            if(player == BLACK):
                board, turn = player_move(player,board)
        if(turn == WHITE):
            if(ai == WHITE):
                move = alpha_beta(WHITE, board, -math.inf,math.inf, 7, time.time() + max_time)[1]
                board = make_move(move,WHITE,board)
                turn = next_player(board,WHITE)
                print("--------------------------------------------")
            elif(player == WHITE):
                board, turn = player_move(player,board)
        else:
            print(get_winner(board))
            break

if __name__ == "__main__":
    main()