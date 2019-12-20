from random import shuffle
from chess import *


class Minimax:
    def __init__(self, color: bool, heuristic, maximum_depth: int):
        self.color = color
        self.heuristic = heuristic
        self.maximum_depth = maximum_depth

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

            score = self.minimax(board, self.heuristic, False, current_depth + 1, self.maximum_depth)
            board.pop()

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, board: Board, heuristic, max_turn: bool, current_depth: int, maximum_depth: int) -> int:

        if current_depth == maximum_depth or board.is_game_over():
            return heuristic(board, self.color, max_turn)

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
