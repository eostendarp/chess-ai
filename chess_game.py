import chess
import copy
from agents.random_agent import RandAgent
from agents.greedy_agent import GreedyAgent


class ChessGame:

    def __init__(self, agent1, agent2):
        self.agent1 = agent1
        self.agent2 = agent2
        self.board = chess.Board()

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
            end_state = {self.agent1.color: float(result.split('-')[0]), self.agent2.color: float(result.split('-')[1]), 'Tie': 0}

        return end_state

    def play_round(self, display_move=False):
        self.play_move(self.agent1)
        if display_move:
            print(str(self.board) + "\n")

        self.play_move(self.agent2)
        if display_move:
            print(str(self.board) + "\n")

    def play_move(self, agent):
        chosen_move = agent.get_move(copy.deepcopy(self.board))
        if chosen_move is not None:
            self.board.push_uci(chosen_move.uci())


def compare_agents(agent1, agent2, num_games, display_moves=False):
    '''
    plays multiple games to compare the two agents
    :param agent1: an agent to play a chess game
    :param agent2: an agent to play a chess gam
    :param num_games: (int) the number of games to be played
    :return:
    '''
    tally = {agent1.color: 0, agent2.color: 0, 'Tie': 0}
    for i in range(num_games):
        if i % 2 == 0:
            game = ChessGame(agent1, agent2)
        else:
            game = ChessGame(agent2, agent1)
        results = game.play_game(display_moves=display_moves)
        tally[agent1.color] += results[agent1.color]
        tally[agent2.color] += results[agent2.color]
        tally['Tie'] += results['Tie']
        if display_moves:
            print(str(game.board)+"\n")

    return tally


def run():
    print("Comparing Agents")
    tally = compare_agents(RandAgent("B"), RandAgent("W"), 100)
    print(tally)
    
run()
