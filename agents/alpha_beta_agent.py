from agents.base_agent import BaseAgent
from copy import deepcopy
from agents.heuristics import get_color_bool, get_opposing_color
from random import shuffle


class AlphaBetaAgent(BaseAgent):
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
            score = self.alpha_beta(board, self.heuristic, float('-inf'), float('inf'), False, current_depth + 1, self.maximum_depth)
            board.pop()

            if score > best_score:
                # print(score)
                # print(move)
                best_score = score
                best_move = move

        return best_move

    def alpha_beta(self, board, heuristic, alpha, beta, max_turn, current_depth, maximum_depth):

        if current_depth == maximum_depth or board.is_game_over():
            return heuristic(board, self.color_bool)

        possible_moves = [move for move in board.legal_moves]
        shuffle(possible_moves)

        best_score = float('-inf') if max_turn else float('inf')
        for move in possible_moves:
            board.push_uci(move.uci())
            score = self.alpha_beta(board, heuristic, alpha, beta, not max_turn, current_depth+1, maximum_depth)
            board.pop()

            if max_turn and score > best_score:
                best_score = score
                if best_score >= beta:
                    return best_score
                alpha = max(alpha, best_score)

            if not max_turn and score < best_score:
                best_score = score
                if best_score <= alpha:
                    return best_score
                beta = min(beta, best_score)



        return best_score


        # if max_turn:
        #     score = float('-inf')
        #     for move in possible_moves:
        #         board.push_uci(move.uci())
        #         score = max(score, self.alpha_beta(board, heuristic, alpha, beta, not max_turn, current_depth + 1, maximum_depth))
        #         if score >= beta:
        #             return score
        #         alpha = max(alpha, score)
        #
        # else:
        #     score = float('inf')
        #     for move in possible_moves:
        #         board.push_uci(move.uci())
        #         score = min(score, self.alpha_beta(board, heuristic, alpha, beta, not max_turn, current_depth + 1, maximum_depth))
        #         if score <= alpha:
        #             return score
        #         beta = min(beta, alpha)
        #
        # board.pop()
        # return score