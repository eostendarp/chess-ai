import chess
import random
import time


def main():
    board = chess.Board()
    legal_moves = board.legal_moves
    while not board.is_game_over():
        rand_move = random.choice([move for move in legal_moves])
        board.push_uci(rand_move.uci())
        print(str(board) + '\n')
        time.sleep(.25)


if __name__ == "__main__":
    main()
