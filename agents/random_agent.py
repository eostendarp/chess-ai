from agents.base_agent import BaseAgent
from random import choice
from chess import *


class RandAgent(BaseAgent):
    """
    Random Agent Randomly Picks Valid Move
    """
    def __init__(self, color: bool):
        super().__init__(color)

    def get_move(self, board: Board) -> Optional[Move]:
        """
        Returns random move
        :param board: chess board
        :return: random move from legal moves
        """
        if not board.is_game_over():
            return choice([move for move in board.legal_moves])
        else:
            return None
