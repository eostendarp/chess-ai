from random import shuffle
from chess.polyglot import zobrist_hash

class AlphaBetaHash:
    def __init__(self, color, heuristic, maximum_depth):
        self.color = color
        self.heuristic = heuristic
        self.maximum_depth = maximum_depth
        self.t_table = {}

    def get_move(self, board):
        """
        Top level function for alpha_beta
        :param board: Board object
        :return: returns a Move object to be used in chess_game.py
        """
        current_depth = 0
        possible_moves = [move for move in board.legal_moves]
        shuffle(possible_moves)
        best_move = None
        best_score = float('-inf')

        for move in possible_moves:
            board.push_uci(move.uci())

            if board.is_checkmate() and board.turn != self.color:
                return move

            h = str(zobrist_hash(board))
            try:
                score = self.t_table.get(h)
            except KeyError:
                score = None

            if score is None:
                score = self.alpha_beta(board, self.heuristic, float('-inf'), float('inf'), False, current_depth + 1,
                                        self.maximum_depth)
                self.t_table[h] = score
            board.pop()

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def alpha_beta(self, board, heuristic, alpha, beta, max_turn, current_depth, maximum_depth):
        """
        alpha beta implementation for pruning of decision tree
        :param board: Board object
        :param heuristic: function name of the heuristic to be used for evaluation
        :param alpha: alpha value
        :param beta: beta value
        :param max_turn: Bool
        :param current_depth: int
        :param maximum_depth: int
        :return: the best score calculated for a move
        """

        if current_depth == maximum_depth or board.is_game_over():
            return heuristic(board, self.color, max_turn)

        possible_moves = [move for move in board.legal_moves]
        shuffle(possible_moves)

        best_score = float('-inf') if max_turn else float('inf')
        for move in possible_moves:
            board.push_uci(move.uci())
            score = self.alpha_beta(board, heuristic, alpha, beta, not max_turn, current_depth + 1, maximum_depth)
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
