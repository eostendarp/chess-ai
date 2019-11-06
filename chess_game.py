import chess
import copy


class ChessGame:

    def __init__(self, agent1, agent2):
        self.agent1 = agent1
        self.agent2 = agent2
        self.board = chess.Board()

    def play_game(self):
        '''
        runs a single game of chess between two agents
        :return: the result of the game
        '''
        while not self.board.is_game_over():
            self.play_round()
        result = self.board.result()
        end_state = {self.agent1.name: result.split('-')[0], self.agent2.name: result.split('-')[1]}
        return end_state

    def play_round(self):
        self.play_move(self.agent1)
        self.play_move(self.agent2)

    def play_move(self, agent):
        chosen_move = agent.get_move(copy.deepcopy(self.board))
        self.board.push_uci(chosen_move.uci())


def compare_agents(agent1, agent2, num_games):
    '''
    plays multiple games to compare the two agents
    :param agent1: an agent to play a chess game
    :param agent2: an agent to play a chess gam
    :param num_games: (int) the number of games to be played
    :return:
    '''
    tally = {agent1.name: 0, agent2: 0}
    for i in range(num_games):
        if i % 2 == 0:
            game = ChessGame(agent1, agent2)
        else:
            game = ChessGame(agent2, agent1)
        results = game.play_game()
        tally[agent1.name] += results[agent1.name]
        tally[agent2.name] += results[agent2.name]

    return tally

