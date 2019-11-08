import chess
import random
import time
from agents.greedy_agent import GreedyAgent

def main():
    board = chess.Board()
    my_greedy_agent = GreedyAgent('w')
    print(my_greedy_agent.get_move(board))
    legal_moves = board.legal_moves
    while not board.is_game_over():
        print("peepee poopoo")
        rand_move = random.choice([move for move in legal_moves])
        board.push_uci(rand_move.uci())
        print(str(board) + '\n')
        time.sleep(.25)


if __name__ == "__main__":
    main()
