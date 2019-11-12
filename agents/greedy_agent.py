from agents.base_agent import BaseAgent
from copy import deepcopy
from random import choice
from chess import Board


class GreedyAgent(BaseAgent):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board):
        boardcopy = deepcopy(board)
        for move in board.legal_moves:
            if boardcopy.is_capture(move):
                return move
        else:
            if not board.is_game_over():
                return choice([move for move in board.legal_moves])
            else:
                return None
