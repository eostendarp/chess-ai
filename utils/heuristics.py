"""
Add heuristics here
"""
from chess import *
from typing import Dict


def piece_value_heuristic(board: Board, color: bool) -> int:
    score = 0
    opponent = not color
    board_size: int = 64

    for tile in range(0, board_size):
        current_piece = board.piece_at(tile)
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


def general_mobility(board):
    moves = [move for move in board.legal_moves]
    return len(moves)*2


def combined(board, color):
    score = piece_value_heuristic(board, color) + general_mobility(board)
    return score

