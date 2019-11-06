from agents.base_agent import BaseAgent
from copy import deepcopy
from chess import Board


class GreedyAgent(BaseAgent):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board):
        board_score = board.compute_score(self.color)
        for move in board.legal_moves:
            board_copy = deepcopy(board)
            board_copy.make_move(move)
            move_score = board_copy.compute_score(self.color)
            if move_score > board_score:
                return move
        else:
            return board.legal_moves[0]
