import unittest
from agents.greedy_agent import GreedyAgent
from agents.random_agent import RandAgent
from chess_game import ChessGame, compare_agents
import chess


class TestChess(unittest.TestCase):

    def test_agent_creation(self):
        greedy = GreedyAgent('B')
        random = RandAgent('W')
        self.assertEqual(greedy.color, 'B')
        self.assertEqual(random.color, 'W')

    def test_agent_move(self):
        greedy = GreedyAgent('B')
        random = RandAgent('W')
        board = chess.Board()
        greedy_move = greedy.get_move(board)
        random_move = random.get_move(board)

        self.assertTrue(board.is_legal(greedy_move))
        self.assertTrue(board.is_legal(random_move))

    def test_play_game(self):
        greedy = GreedyAgent('B')
        random = RandAgent('W')
        game = ChessGame(greedy, random)
        end_state = game.play_game()

        self.assertTrue(game.board.is_game_over())
        self.assertTrue(sum(end_state[key] for key in end_state.keys()) > 0)

    def test_compare(self):
        agent1 = RandAgent('W')
        agent2 = RandAgent('B')
        num_games = 200
        scores = compare_agents(agent1, agent2, num_games)

        self.assertEqual((sum(scores[key] for key in scores.keys())), num_games)
        self.assertTrue(scores[agent1.color] > 0)
        self.assertTrue(scores[agent2.color] > 0)


if __name__ == '__main__':
    unittest.main()