from agents.base_agent import BaseAgent
from copy import deepcopy
from random import shuffle
from chess import *
from os import getcwd
from utils import trans_table_utils as ttu


class MiniMaxAgentTrans(BaseAgent):
    def __init__(self, color: bool, heuristic, maximum_depth: int):
        super().__init__(color)
        self.heuristic = heuristic
        self.maximum_depth = maximum_depth
        self.trans_tables = ttu.read_trans_table(getcwd() + '/data/minimax_agent/trans_table.pickle')

    def get_move(self, board: Board) -> Move:
        current_depth = 0
        possible_moves = [move for move in board.legal_moves]
        shuffle(possible_moves)
        best_move = None
        best_score = float('-inf')

        for move in possible_moves:
            board.push_uci(move.uci())

            if board.is_checkmate() and board.turn != self.color:
                return move

            h = ttu.hash_(board)
            score = self.trans_tables.get(h)
            if score is None:
                score = self.minimax(board, self.heuristic, False, current_depth + 1, self.maximum_depth)
                self.trans_tables[h] = score
            board.pop()

            if score > best_score:
                # print(score)
                # print(move)
                best_score = score
                best_move = move

        return best_move

    def minimax(self, board: Board, heuristic, max_turn: int, current_depth: int, maximum_depth: int) -> int:

        if current_depth == maximum_depth or board.is_game_over():
            return heuristic(board, self.color)

        possible_moves = [move for move in board.legal_moves]
        shuffle(possible_moves)
        if max_turn:
            score = float('-inf')
            for move in possible_moves:
                board.push_uci(move.uci())
                score = max(score, self.minimax(board, heuristic, not max_turn, current_depth + 1, maximum_depth))
                board.pop()

            return score

        else:
            score = float('inf')
            for move in possible_moves:
                board.push_uci(move.uci())
                score = min(score, self.minimax(board, heuristic, not max_turn, current_depth + 1, maximum_depth))
                board.pop()

            return score
