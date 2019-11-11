from agents.base_agent import BaseAgent
from random import choice
from copy import deepcopy


class MiniMaxAgent(BaseAgent):
    def __init__(self, color, heuristic, maximum_depth):
        super().__init__(color)
        self.heuristic = heuristic
        self.maximum_depth = maximum_depth

    def get_move(self, board):
        current_depth = 0
        possible_moves = board.legal_moves()
        best_move = possible_moves[0]
        best_score = float('-inf')

        for move in possible_moves:
            copy_board = deepcopy(board)
            copy_board.push_uci(move.uci())
            score = max(best_score, self.minimax(copy_board, self.heuristic, False, current_depth, self.maximum_depth))

            if score > best_score:
                best_score = score
                best_move = move

        print(best_move)
        return best_move

    def minimax(self, board, heuristic, max_turn, current_depth=0, maximum_depth=4):

        if current_depth == maximum_depth:
            return -heuristic(board, self.color)

        opp = get_opposing_color(self.color)

        possible_moves = board.legal_moves()
        if max_turn:
            score = float('-inf')
            for move in possible_moves:
                copy_board = deepcopy(board)
                copy_board.push_uci(move.uci())
                score = max(score, self.minimax(copy_board, heuristic, not max_turn, current_depth + 1, maximum_depth))

            return score

        else:
            score = float('inf')
            for move in possible_moves:
                copy_board = deepcopy(board)
                copy_board.push_uci(move.uci())
                score = min(score, self.minimax(copy_board, heuristic, not max_turn, current_depth + 1, maximum_depth))

            return score

        return 0


def get_opposing_color(color):
    if color == "W":
        return "B"
    elif color == "B":
        return "W"
