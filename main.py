import chess
import random
import time
from chess_game import ChessGame
from agents.greedy_agent import GreedyAgent
from agents.random_agent import RandAgent

def main():
    my_game = ChessGame(GreedyAgent, RandAgent)
    my_game.play_game()


if __name__ == "__main__":
    main()
