from agents.base_agent import BaseAgent
import chess
from copy import deepcopy

class HumanAgent(BaseAgent):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board):
        temp_board = deepcopy(board)
        valid_moves_list = board.legal_moves
        is_valid_move = True
        while is_valid_move:
            #print(board)
            move = input("Enter a valid move in uci format: ").lower()
            if len(move) == 4 or len(move) == 5 and chess.Move.from_uci(move) in valid_moves_list:
                try:
                    temp_board.push(chess.Move.from_uci(move))
                    return chess.Move.from_uci(move)
                except:
                    print("invalid move...")
            else:
                print("invalid move...")
