"""
Add heuristics here
"""
from chess import *
from typing import Dict
import collections


def piece_value_heuristic(board: Board, color: bool) -> int:
    score = 0
    opponent = not color
    board_size: int = 64

    for square in range(0, board_size):
        current_piece = board.piece_at(square)
        score = score + get_piece_value(current_piece, color)

    return score


def get_piece_value(piece: Piece, color: bool) -> int:
    if piece is None:
        return 0

    piece_values: Dict[str, int] = {"P": 1, "N": 3, "B": 3, "R": 5, "Q": 9, "K": 100}

    value = 0

    value = piece_values[piece.symbol().upper()]

    if piece.color != color:
        value = value * -1

    return value


def general_mobility(board: Board) -> int:
    piece_mobility_values = {"P":3, "N":7, "B":7, "R":5, "Q":8, "K":2}
    moves = [move.from_square for move in board.legal_moves]
    move_count = collections.Counter(moves)
    mobility_score = 0
    for move in move_count.keys():
        piece = board.piece_at(move).symbol().upper()
        num_moves = move_count[move]
        mobility_score += num_moves * piece_mobility_values[piece]

    return mobility_score


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
