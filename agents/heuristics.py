"""
Add heuristics here
"""


def piece_value_heuristic(board, color):
    score = 0
    opponent = not color
    board_size = 64

    for square in range(0, board_size):
        current_piece = board.piece_at(square)
        score = score + get_piece_value(current_piece, color)

    return score


def get_piece_value(piece, color):
    if piece is None:
        return 0

    value = 0

    if piece.symbol().upper() == "P":
        value = 1
    if piece.symbol().upper() == "N":
        value = 3
    if piece.symbol().upper() == "B":
        value = 3
    if piece.symbol().upper() == "R":
        value = 5
    if piece.symbol().upper() == "Q":
        value = 9
    if piece.symbol().upper() == 'K':
        value = 100

    if piece.color != color:
        value = value * -1

    return value


def general_mobility(board):
    moves = [move for move in board.legal_moves]
    return len(moves)*2


def combined(board, color):
    score = piece_value_heuristic(board, color) + general_mobility(board)
    return score

def get_opposing_color(color):
    if color == "W":
        return "B"
    elif color == "B":
        return "W"


def get_color_bool(color):
    if color == "W":
        return True
    elif color == "B":
        return False
