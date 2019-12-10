from agents.base_agent import BaseAgent
from random import shuffle
from chess import *
from utils.heuristics import mvvlva, get_possible_moves
import copy
from utils.history_utils import *
import os


class CombinedAgent(BaseAgent):
    def __init__(self, color, heuristic, maximum_depth, load_hh=False):
        super().__init__(color)
        self.name='combined'
        self.heuristic = heuristic
        self.maximum_depth = maximum_depth
        self.history = self.init_history(load_hh=load_hh)
        self.pv_line = []

    def init_history(self, load_hh):
        if load_hh:
            table = read_in_history_table(os.getcwd()+"/data/history_table.json")
        else:
            pieces = [PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING]
            values = {}
            for i in range(64):
                values[i] = 0

            table = {True:{}, False:{}}
            for p in pieces:
                table[True][p] = copy.copy(values)
                table[False][p] = copy.copy(values)
        return table

    def get_move(self, board):
        current_depth = 0
        # possible_moves = [move for move in board.legal_moves]
        # shuffle(possible_moves)
        possible_moves = get_possible_moves(board, True, self.pv_line, history=self.history)
        best_move = None
        best_score = float('-inf')
        score_array = [best_score]

        for move in possible_moves:
            board.push_uci(move.uci())

            if board.is_checkmate() and board.turn != self.color:
                return move

            score = self.alpha_beta(board, self.heuristic, float('-inf'), float('inf'),
                                    False, self.maximum_depth-1, score_array, self.pv_line)
            board.pop()

            if score > best_score:
                best_score = score
                best_move = move

        print("AlphaBeta:",best_score)
        self.pv_line.reverse()
        # print(self.pv_line)
        return best_move

    def alpha_beta(self, board, heuristic, alpha, beta, max_turn, depth, best, pline):
        original_best = best[0]

        if depth == 0 or board.is_game_over():
            curr_score = heuristic(board, self.color, max_turn)
            if curr_score > best[0]:
                pline.clear()
                best.clear()
                best.append(curr_score)
                return curr_score
            else:
                return best[0]

        possible_moves = get_possible_moves(board, max_turn, self.pv_line, history=self.history)


        best_score = float('-inf') if max_turn else float('inf')
        for move in possible_moves:
            board.push_uci(move.uci())
            score = self.alpha_beta(board, heuristic, alpha, beta,
                                    not max_turn, depth-1, best, pline)

            if original_best != best[0]:
                original_best = best[0]
                pline.append(board.pop())
            else:
                board.pop()

            if max_turn and score > best_score:
                best_score = score
                if best_score >= beta:
                    if not board.is_capture(move):
                        piece = board.piece_at(move.from_square)
                        self.history[max_turn][piece.piece_type][move.to_square] += pow(2, depth)
                    return best_score
                alpha = max(alpha, best_score)

            if not max_turn and score < best_score:
                best_score = score
                if best_score <= alpha:
                    if not board.is_capture(move):
                        piece = board.piece_at(move.from_square)
                        self.history[max_turn][piece.piece_type][move.to_square] += pow(2, depth)
                    return best_score
                beta = min(beta, best_score)

        return best_score