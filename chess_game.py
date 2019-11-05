import chess
import copy


class ChessGame:

    def __init__(self, agent1, agent2):
        self.agent1 = agent1
        self.agent2 = agent2
        self.board = chess.Board()

    def play_game(self):
        while not self.board.is_game_over():
            self.play_round()

    def play_round(self):
        self.play_move(self.agent1)
        self.play_move(self.agent2)

    def play_move(self, agent):
        chosen_move = agent.get_move(copy.deepcopy(self.board))
        self.board.push_uci(chosen_move.uci())