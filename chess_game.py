import chess
import chess.svg
from chess import BISHOP
from datetime import datetime
from agents.minimax_agent import MiniMaxAgent
from agents.alpha_beta_agent import AlphaBetaAgent
from agents.alpha_beta_agent_trans import AlphaBetaAgentTrans
from utils.heuristics import combined, piece_value_heuristic, mvvlva, capture_moves
from utils.history_utils import *
from agents.pv_agent import PVAgent
from utils.tapered_evaluation import tapered_evaluation
from agents.combined_agent import CombinedAgent
from utils import trans_table_utils as ttu
from os import getcwd
from agents.combined_agent import CombinedAgent
from agents.combined_agent_trans import CombinedAgentTrans
from agents.human_agent import HumanAgent


class ChessGame:

    def __init__(self, agent1, agent2):
        self.agent1 = agent1
        self.agent2 = agent2
        self.board = chess.Board()
        self.total_move_times = {agent1.color: 0, agent2.color: 0}
        self.moves_made = {agent1.color: 0, agent2.color: 0}

    def play_game(self, display_moves=False):
        '''
        runs a single game of chess between two agents
        :return: the result of the game
        '''
        end_state = {}
        while not self.board.is_game_over():
            self.play_round(display_move=display_moves)
        result = self.board.result()
        state = result.split("-")
        if state[0] == '1/2':
            end_state = {self.agent1.color: 0, self.agent2.color: 0, 'Tie': 1}
        else:
            end_state = {self.agent1.color: float(result.split('-')[0]), self.agent2.color: float(result.split('-')[1]),
                         'Tie': 0}

        return end_state

    def play_round(self, display_move=False):
        """
        Plays a single round of a game facilitates a single turn for each agent
        :param display_move: (optional) bool to display the board
        :return:
        """
        start = datetime.utcnow()
        self.play_move(self.agent1)
        self.total_move_times[self.agent1.color] += (datetime.utcnow() - start).total_seconds()
        self.moves_made[self.agent1.color] += 1

        if display_move:
            print(str(self.board.unicode(borders=True)) + "\n")

        start = datetime.utcnow()
        self.play_move(self.agent2)
        self.total_move_times[self.agent2.color] += (datetime.utcnow() - start).total_seconds()
        self.moves_made[self.agent2.color] += 1

        if display_move:
            print(str(self.board.unicode(borders=True)) + "\n")

    def play_move(self, agent):
        chosen_move = agent.get_move(self.board.copy())
        if chosen_move is not None:
            self.board.push_uci(chosen_move.uci())


def compare_agents(agent1, agent2, num_games, display_moves=False):
    '''
    plays multiple games to compare the two agents
    :param display_moves: Displays board or not
    :param agent1: an agent to play a chess game
    :param agent2: an agent to play a chess gam
    :param num_games: (int) the number of games to be played
    :return:
    '''
    average_move_time = {agent1.color: 0, agent2.color: 0}
    tally = {agent1.color: 0, agent2.color: 0, 'Tie': 0}
    for i in range(num_games):
        if i % 2 == 0:
            game = ChessGame(agent1, agent2)
        else:
            game = ChessGame(agent2, agent1)
        if display_moves:
            print(game.board.unicode(borders=True))

        if i % 3 == 0:
            print(i,"Games finished")

        results = game.play_game(display_moves=display_moves)

        tally[agent1.color] += results[agent1.color]
        tally[agent2.color] += results[agent2.color]
        tally['Tie'] += results['Tie']

        for symbol in average_move_time.keys():
            average_move_time[symbol] += (game.total_move_times[symbol] / game.moves_made[symbol])

        if display_moves:
            print(str(game.board.unicode(borders=True)) + "\n")

    return tally, average_move_time


def capture_test():
    fen = "8/8/8/3b4/2B1P3/8/8/8 w - - 0 1"
    b = chess.Board(fen=fen)
    print(b)
    capture_moves(b, True)


def run():

    print("Comparing Agents")
    agent1, agent2 = [HumanAgent(False), CombinedAgentTrans(True, combined, 3, load_hh=True)]
    tally, avg = compare_agents(agent1, agent2, 5, False)
    # ttu.write_trans_table(agent2.trans_table, getcwd() + '/data/combined_agent/trans_table.pickle')
    print(tally)
    print("Average Decision Times:", avg)

run()
