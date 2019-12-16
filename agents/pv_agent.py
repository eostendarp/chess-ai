from agents.base_agent import BaseAgent
from random import shuffle


class PVAgent(BaseAgent):
    def __init__(self, color, heuristic, maximum_depth):
        super().__init__(color)
        self.heuristic = heuristic
        self.maximum_depth = maximum_depth
        self.pv_line = []

    def get_move(self, board):
        current_depth = 0
        possible_moves = [move for move in board.legal_moves]
        shuffle(possible_moves)
        best_move = None
        best_score = float('-inf')
        score_array = [best_score]

        for move in possible_moves:
            board.push_uci(move.uci())

            if board.is_checkmate() and board.turn != self.color:
                return move

            score = self.alpha_beta(board, self.heuristic, float('-inf'), float('inf'), False, current_depth + 1,
                                    self.maximum_depth, score_array, self.pv_line)

            board.pop()

            if score > best_score:
                #print(score)
                #print(move)
                best_score = score
                best_move = move

        self.pv_line.reverse()
        #print("AlphaBeta:", best_score)
        #print("Best Move:", best_move)
        print(self.pv_line)
        return best_move

    def alpha_beta(self, board, heuristic, alpha, beta, max_turn, current_depth, maximum_depth, best, pline):
        original_best = best[0]

        if current_depth == maximum_depth or board.is_game_over():
            curr_score = heuristic(board, self.color, max_turn)

            if curr_score > best[0]:
                pline.clear()
                best.clear()
                best.append(curr_score)
                return curr_score
            else:
                return curr_score

        possible_moves = [move for move in board.legal_moves]
        shuffle(possible_moves)

        best_score = float('-inf') if max_turn else float('inf')
        for move in possible_moves:
            board.push_uci(move.uci())
            score = self.alpha_beta(board, heuristic, alpha, beta, not max_turn, current_depth + 1, maximum_depth, best,
                                    pline)

            if original_best != best[0]:
                original_best = best[0]
                pline.append(board.pop().uci())
            else:
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