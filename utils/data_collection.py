import chess
from datetime import datetime
from tqdm import tqdm
from os import getcwd

from utils.heuristics import combined

from agents.alpha_beta_agent import AlphaBetaAgent
from agents.alpha_beta_agent_trans import AlphaBetaAgentTrans
from agents.combined_agent import CombinedAgent
from agents.combined_agent_trans import CombinedAgentTrans
from agents.history_agent import OrderedAgent
from agents.history_agent_trans import OrderedAgentTrans
from agents.minimax_agent import MiniMaxAgent
from agents.minimax_agent_trans import MiniMaxAgentTrans
from agents.pv_agent import PVAgent
from agents.pv_agent_trans import PVAgentTrans
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
        f.write('game_number\tagent_type\tagent_color\tagent_depth\tagent_num_moves\tagent_decision_time\tgame_result\n')

        for g_n in tqdm(range(num_runs)):
            g = ChessGame(white_agent_name, black_agent_name, white_agent, black_agent).play_game()
            f.write(str(g_n) + '\t' + g['white_agent_name'] + '\t' + 'white' + '\t' + g['white_agent_depth'] + '\t' + g['white_agent_num_moves'] + '\t' + g['white_agent_decision_time'] + '\t' + g['white_agent_result'] + '\n')
            f.write(str(g_n) + '\t' + g['black_agent_name'] + '\t' + 'black' + '\t' + g['black_agent_depth'] + '\t' + g['black_agent_num_moves'] + '\t' + g['black_agent_decision_time'] + '\t' + g['black_agent_result'] + '\n')


def main():
    # run
    pass
    # generate_data('random', RandAgent(chess.WHITE), 'random', RandAgent(chess.BLACK), getcwd()[:-5] + 'data/RvR.csv')
    # generate_data('random', RandAgent(chess.WHITE), 'alphabeta2', AlphaBetaAgent(chess.BLACK, combined, 2), getcwd()[:-5] + 'data/RvA.csv')
    # generate_data('minimax2', MiniMaxAgent(chess.WHITE, combined, 2), 'alphabeta2', AlphaBetaAgent(chess.BLACK, combined, 2), getcwd()[:-5] + 'data/MvA.csv')
    # generate_data('alphabeta2', AlphaBetaAgent(chess.WHITE, combined, 2), 'alphabeta2', AlphaBetaAgent(chess.BLACK, combined, 2), getcwd()[:-5] + 'data/AvA.csv')

    # # transposition table
    # generate_data('alphabeta2', AlphaBetaAgent(chess.WHITE, combined, 2), 'alphabeta2_trans', AlphaBetaAgentTrans(chess.BLACK, combined, 2), getcwd()[:-5] + 'data/AvAT.csv')
    # # depth
    # generate_data('alphabeta1', AlphaBetaAgent(chess.WHITE, combined, 1), 'alphabeta2', AlphaBetaAgent(chess.BLACK, combined, 2), getcwd()[:-5] + 'data/A1vA2.csv')
    # generate_data('alphabeta1', AlphaBetaAgent(chess.WHITE, combined, 1), 'alphabeta3', AlphaBetaAgent(chess.BLACK, combined, 3), getcwd()[:-5] + 'data/A1vA3.csv')
    # generate_data('alphabeta2', AlphaBetaAgent(chess.WHITE, combined, 2), 'alphabeta3', AlphaBetaAgent(chess.BLACK, combined, 3), getcwd()[:-5] + 'data/A2vA3.csv')

    # not run
    # generate_data('alphabeta2', AlphaBetaAgent(chess.WHITE, combined, 2), 'history2', OrderedAgent(chess.BLACK, combined, 2), getcwd()[:-5] + 'data/AvH.csv')
    # generate_data('alphabeta2', AlphaBetaAgent(chess.WHITE, combined, 2), 'pv2', PVAgent(chess.BLACK, combined, 2), getcwd()[:-5] + 'data/AvP.csv')
    # generate_data('alphabeta2', AlphaBetaAgent(chess.WHITE, combined, 2), 'combined2', CombinedAgent(chess.BLACK, combined, 2), getcwd()[:-5] + 'data/AvC.csv')
    # generate_data('history2', OrderedAgent(chess.WHITE, combined, 2), 'history2', OrderedAgent(chess.BLACK, combined, 2), getcwd()[:-5] + 'data/HvH.csv')
    # generate_data('pv2', PVAgent(chess.WHITE, combined, 2), 'pv2', PVAgent(chess.BLACK, combined, 2), getcwd()[:-5] + 'data/PvP.csv')
    # generate_data('combined2', CombinedAgent(chess.WHITE, combined, 2), 'combined2', CombinedAgent(chess.BLACK, combined, 2), getcwd()[:-5] + 'data/CvC.csv')


if __name__ == '__main__':
    main()
