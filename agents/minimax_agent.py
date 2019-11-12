from agents.base_agent import BaseAgent
from copy import deepcopy
from agents.heuristics import get_color_bool, get_opposing_color
from random import shuffle


class MiniMaxAgent(BaseAgent):
    def __init__(self, color, heuristic, maximum_depth):
        super().__init__(color)
        self.heuristic = heuristic
        self.maximum_depth = maximum_depth
        self.color_bool = get_color_bool(self.color)

    def get_move(self, board):
        current_depth = 0
        possible_moves = board.legal_moves
        best_move = None
        best_score = float('-inf')

        for move in possible_moves:
            board.push_uci(move.uci())
            score = self.minimax(board, self.heuristic, False, current_depth + 1, self.maximum_depth)
            board.pop()

            if score > best_score:
                print(score)
                print(move)
                best_score = score
                best_move = move


        return best_move

    def minimax(self, board, heuristic, max_turn, current_depth, maximum_depth):

        if current_depth == maximum_depth or board.is_game_over():
            return heuristic(board, self.color_bool)

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




