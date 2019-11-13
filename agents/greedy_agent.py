from agents.base_agent import BaseAgent
from copy import deepcopy
from random import choice
from chess import *


class GreedyAgent(BaseAgent):
    def __init__(self, color: bool):
        super().__init__(color)

    def get_move(self, board: Board) -> Move:
        board_copy = deepcopy(board)
        if not board.is_game_over():
            for move in board.legal_moves:
                if board_copy.is_capture(move):
                    return move
            else:
                return choice([move for move in board.legal_moves])
        else:
            return None

