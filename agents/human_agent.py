from agents.base_agent import BaseAgent
import chess
from copy import deepcopy


class HumanAgent(BaseAgent):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board):
        valid_moves = [move for move in board.legal_moves]
        is_valid_move = False
        while not is_valid_move:
            move = input("Enter a valid move in uci format: ").lower()
            if len(move) == 4 or len(move) == 5:
                player_move = chess.Move.from_uci(move)

                if board.is_legal(player_move):
                    try:
                        board.push(player_move)
                        return player_move
                    except:
                        print("invalid move...")
            else:
                print("invalid move...")
