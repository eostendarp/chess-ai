import chess
from datetime import datetime
from tqdm import tqdm
from os import getcwd

from utils.heuristics import combined

from agents.alpha_beta_agent import AlphaBetaAgent
from agents.alpha_beta_agent_trans import AlphaBetaAgentTrans
from agents.combined_agent import CombinedAgent
from agents.history_agent import OrderedAgent
from agents.minimax_agent import MiniMaxAgent
from agents.pv_agent import PVAgent
from agents.random_agent import RandAgent


class ChessGame:
    def __init__(self, white_agent_name, white_agent, black_agent_name, black_agent):
        self.white_agent_name = white_agent_name
        self.black_agent_name = black_agent_name
        self.white_agent = white_agent
        self.black_agent = black_agent
        self.white_agent_depth = white_agent.maximum_depth if hasattr(white_agent, 'maximum_depth') else 0
        self.black_agent_depth = black_agent.maximum_depth if hasattr(black_agent, 'maximum_depth') else 0
        self.white_agent_num_moves = 0
        self.black_agent_num_moves = 0
        self.white_agent_decision_time = 0
        self.black_agent_decision_time = 0
        self.white_agent_result = 0
        self.black_agent_result = 0
        self.board = chess.Board()

    def play_game(self):
        while not self.board.is_game_over():
            self.play_round()
        result = self.board.result()
        if result == '0-1':
            self.white_agent_result = -1
            self.black_agent_result = 1
        elif result == '1-0':
            self.white_agent_result = 1
            self.black_agent_result = -1

        return {
            'white_agent_name': self.white_agent_name,
            'black_agent_name': self.black_agent_name,
            'white_agent_depth': str(self.white_agent_depth),
            'black_agent_depth': str(self.black_agent_depth),
            'white_agent_num_moves': str(self.white_agent_num_moves),
            'black_agent_num_moves': str(self.black_agent_num_moves),
            'white_agent_decision_time': str(self.white_agent_decision_time),
            'black_agent_decision_time': str(self.black_agent_decision_time),
            'white_agent_result': str(self.white_agent_result),
            'black_agent_result': str(self.black_agent_result)
        }

    def play_round(self):
        start = datetime.utcnow()
        self.play_move(self.white_agent)
        self.white_agent_decision_time += (datetime.utcnow() - start).total_seconds()
        self.white_agent_num_moves += 1

        start = datetime.utcnow()
        self.play_move(self.black_agent)
        self.black_agent_decision_time += (datetime.utcnow() - start).total_seconds()
        self.black_agent_num_moves += 1

    def play_move(self, agent):
        chosen_move = agent.get_move(self.board.copy())
        if chosen_move is not None:
            self.board.push_uci(chosen_move.uci())


def generate_data(white_agent_name, black_agent_name, white_agent, black_agent, path, num_runs=100):
    with open(path, 'w') as f:
        f.write('game_number, agent_type, agent_color, agent_decision_time\n')

        for g_n in tqdm(range(num_runs)):
            g = ChessGame(white_agent_name, black_agent_name, white_agent, black_agent).play_game()
            f.write(str(g_n) + ', ' + g['white_agent_name'] + ', ' + 'white' + ', ' + g['white_agent_decision_time'] + '\n')
            f.write(str(g_n) + ', ' + g['black_agent_name'] + ', ' + 'black' + ', ' + g['black_agent_decision_time'] + '\n')


from t_tables.minimax import Minimax
from t_tables.alpha_beta import AlphaBeta
from t_tables._random import Random

from t_tables.minimax_avl import MinimaxAVL
from t_tables.alpha_beta_avl import AlphaBetaAVL
from t_tables._random_avl import RandomAVL

from t_tables.minimax_hash import MinimaxHash
from t_tables.alpha_beta_hash import AlphaBetaHash
from t_tables._random_hash import RandomHash

from t_tables.minimax_rb import MinimaxRB
from t_tables.alpha_beta_rb import AlphaBetaRB
from t_tables._random_rb import RandomRB

from t_tables.minimax_splay import MinimaxSplay
from t_tables.alpha_beta_splay import AlphaBetaSplay
from t_tables._random_splay import RandomSplay

from t_tables.minimax_trie import MinimaxTrie
from t_tables.alpha_beta_trie import AlphaBetaTrie
from t_tables._random_trie import RandomTrie


def main():
    generate_data('random', Random(chess.WHITE), 'random_avl', RandomAVL(chess.BLACK), 'data/random_avl_1.csv', 100)
    generate_data('random', Random(chess.WHITE), 'random_hash', RandomHash(chess.BLACK), 'data/random_hash_1.csv', 100)
    generate_data('random', Random(chess.WHITE), 'random_rb', RandomRB(chess.BLACK), 'data/random_rb_1.csv', 100)
    generate_data('random', Random(chess.WHITE), 'random_splay', RandomSplay(chess.BLACK), 'data/random_splay_1.csv', 100)
    generate_data('random', Random(chess.WHITE), 'random_trie', RandomTrie(chess.BLACK), 'data/random_trie_1.csv', 100)

    generate_data('minimax', Minimax(chess.WHITE, combined, 1), 'minimax_avl', MinimaxAVL(chess.BLACK, combined, 1), 'data/minimax_avl_1.csv', 100)
    generate_data('minimax', Minimax(chess.WHITE, combined, 1), 'minimax_hash', MinimaxHash(chess.BLACK, combined, 1), 'data/minimax_hash_1.csv', 100)
    generate_data('minimax', Minimax(chess.WHITE, combined, 1), 'minimax_rb', MinimaxRB(chess.BLACK, combined, 1), 'data/minimax_rb_1.csv', 100)
    generate_data('minimax', Minimax(chess.WHITE, combined, 1), 'minimax_splay', MinimaxSplay(chess.BLACK, combined, 1), 'data/minimax_splay_1.csv', 100)
    generate_data('minimax', Minimax(chess.WHITE, combined, 1), 'minimax_trie', MinimaxTrie(chess.BLACK, combined, 1), 'data/minimax_trie_1.csv', 100)

    generate_data('alpha_beta', AlphaBeta(chess.WHITE, combined, 1), 'alpha_beta_avl', AlphaBetaAVL(chess.BLACK, combined, 1), 'data/alpha_beta_avl_1.csv', 100)
    generate_data('alpha_beta', AlphaBeta(chess.WHITE, combined, 1), 'alpha_beta_hash', AlphaBetaHash(chess.BLACK, combined, 1), 'data/alpha_beta_hash_1.csv', 100)
    generate_data('alpha_beta', AlphaBeta(chess.WHITE, combined, 1), 'alpha_beta_rb', AlphaBetaRB(chess.BLACK, combined, 1), 'data/alpha_beta_rb_1.csv', 100)
    generate_data('alpha_beta', AlphaBeta(chess.WHITE, combined, 1), 'alpha_beta_splay', AlphaBetaSplay(chess.BLACK, combined, 1), 'data/alpha_beta_splay_1.csv', 100)
    generate_data('alpha_beta', AlphaBeta(chess.WHITE, combined, 1), 'alpha_beta_trie', AlphaBetaTrie(chess.BLACK, combined, 1), 'data/alpha_beta_trie_1.csv', 100)


if __name__ == '__main__':
    main()
