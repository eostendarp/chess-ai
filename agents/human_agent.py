from agents.base_agent import BaseAgent
import chess

class HumanAgent(BaseAgent):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board):
        while True:
            print("Enter move: ")
            input_ = input()
            try:
                if chess.Move.from_uci(input_) in board.legal_moves:
                    return chess.Move.from_uci(input_)
            except:
                print("Invalid move...")