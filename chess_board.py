from json import dump


class ChessBoard:
    def __init__(self):
        self._board = _getNewBoard()

    def draw_board(self):
        _drawBoard(self._board)

    def is_valid_move(self, piece, position):
        return _isValidMove(self._board, piece, position[0], position[1])

    def calc_scores(self):
        return _getScoreOfBoard(self._board)

    def make_move(self, piece, position):
        return _makeMove(self._board, piece, position[0], position[1])

    def calc_valid_moves(self, color):
        return _calcValidMoves(self._board, color)

    def game_continues(self):
        return self.calc_valid_moves('W') or self.calc_valid_moves('B')

    def get_piece_at_position(self, position):
        return self._board[position[0], position[1]]

    @staticmethod
    def get_opponent_color(color):
        if color == 'W':
            return 'B'
        return 'W'

    def to_json_file(self, filename):
        with open(filename, 'w') as f:
            dump(self._board. f)


def _getNewBoard():
    board = [[' '] * 8 for _ in range(8)]
