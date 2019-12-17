from agents.base_agent import BaseAgent
from random import choice
from chess import *
from utils.trans_table_utils import *
from os import getcwd


class RandAgentTrans(BaseAgent):
    """
    Random Agent Randomly Picks Valid Move
    """
    def __init__(self, color: bool):
        super().__init__(color)
        self.trans_table = read_trans_table(getcwd() + '/data/random_agent/trans_table.pickle')


    def get_move(self, board: Board) -> Optional[Move]:
        """
        Returns random move
        :param board: chess board
        :return: random move from legal moves
        """
        if not board.is_game_over():
            h = hash_(board)
            s = self.trans_table.get(h)
            if s is None:
                self.trans_table[h] = 0
            return choice([move for move in board.legal_moves])
        else:
            return None
