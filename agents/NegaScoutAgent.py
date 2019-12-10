from agents.base_agent import BaseAgent
from random import shuffle
from chess import *
from utils.heuristics import mvvlva, get_possible_moves
import copy
from utils.history_utils import *
import os


class NegaScoutAgent(BaseAgent):
    def __init__(self, color, heuristic, maximum_depth, load_hh=False):
        super().__init__(color)
        self.heuristic = heuristic
        self.maximum_depth = maximum_depth
        self.history = self.init_history(load_hh=load_hh)
        self.pv_line = []

    def init_history(self, load_hh):
        if load_hh:
            table = read_in_history_table(os.getcwd() + "/data/history_table.json")
        else:
            pieces = [PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING]
            values = {}
            for i in range(64):
                values[i] = 0

            table = {True: {}, False: {}}
            for p in pieces:
                table[True][p] = copy.copy(values)
                table[False][p] = copy.copy(values)
        return table

    def get_move(self, board):
        possible_moves = get_possible_moves(board, True, self.pv_line, history=self.history)
        best_move = None
        best_score = float('-inf')
        score_array = [best_score]

        for move in possible_moves:
            board.push_uci(move.uci())
            print(board.unicode(borders=True))

            if board.is_checkmate() and board.turn != self.color:
                return move

            score = self.negascout(board, self.heuristic, float('-inf'), float('inf'),
                                   self.maximum_depth, score_array, self.pv_line)

            board.pop()

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def negascout(self, board, heuristic, alpha, beta, current_depth, best, pv_line):
        original_best = best[0]

        if current_depth == 0 or board.is_game_over():
            curr_score = heuristic(board, self.color, board.turn==self.color)
            if curr_score > best[0]:
                pv_line.clear()
                best.clear()
                best.append(curr_score)
                return curr_score
            else:
                return best[0]

        possible_moves = get_possible_moves(board, board.turn==self.color, self.pv_line, history=self.history)

        for move in range(len(possible_moves)):
            board.push_uci(possible_moves[move].uci())

            # First move in list is considered the best move
            if move == 0:
                score = 0 - self.negascout(board, heuristic, 0-beta, 0-alpha,
                                           current_depth-1, best, pv_line)
                board.pop()
            else:   # Search with null window
                score = 0 - self.negascout(board, heuristic, 0-alpha-1, 0-alpha,
                                           current_depth-1, best, pv_line)
                board.pop()

                if alpha < score < beta:    # if failed high, do a re-search
                    score = 0 - self.negascout(board, heuristic, 0-beta, 0-score,
                                               current_depth-1, best, pv_line)
                    board.pop()
            alpha = max(alpha, score)
            # Beta cut-off
            if alpha >= beta:
                if not board.is_capture(possible_moves[move]):
                    piece = board.piece_at(possible_moves[move].from_square)
                    self.history[board.turn==self.color][piece.piece_type][possible_moves[move].to_square] += pow(2, current_depth)
                break

        return alpha

