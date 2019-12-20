from random import choice
from typing import Optional
from chess import Color, Board, Move
from bintrees import AVLTree
from chess.polyglot import zobrist_hash


class RandomAVL:
    def __init__(self, color: Color) -> None:
        self.color = color
        self.t_table = AVLTree()

    def get_move(self, board: Board) -> Optional[Move]:
        legal_moves = board.legal_moves
        h = zobrist_hash(board)

        try:
            score = self.t_table.get_value(h)
        except KeyError:
            score = None

        if score is None:
            score = 0
            self.t_table.insert(h, score)
        return choice([move for move in board.legal_moves]) if legal_moves else None
