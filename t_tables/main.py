from chess import WHITE, BLACK
from t_tables.chess_game import generate_data
from utils.heuristics import combined

from t_tables.alpha_beta import AlphaBeta
from t_tables.minimax import Minimax
from t_tables._random import Random


def main():
    white_agent, black_agent = [Minimax(WHITE, combined, 1), AlphaBeta(BLACK, combined, 1)]
    generate_data(white_agent, black_agent, 'temp.csv', 10)


if __name__ == '__main__':
    main()
