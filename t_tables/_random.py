from random import choice
from typing import Optional
from chess import Color, Board, Move


class Random:
    def __init__(self, color: Color) -> None:
        self.color = color

    @staticmethod
    def get_move(board: Board) -> Optional[Move]:
        legal_moves = board.legal_moves
        return choice([move for move in board.legal_moves]) if legal_moves else None
