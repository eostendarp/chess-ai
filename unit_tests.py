import unittest
from agents.greedy_agent import GreedyAgent
from agents.random_agent import RandAgent
from agents.minimax_agent import MiniMaxAgent
from agents.alpha_beta_agent import AlphaBetaAgent
from agents.combined_agent import CombinedAgent
from utils.heuristics import *
from chess_game import ChessGame, compare_agents
from utils.trans_table_utils import *
import chess
import os


class TestChess(unittest.TestCase):

    def test_agent_creation(self):
        mini = MiniMaxAgent(True, combined, 3)
        alph = AlphaBetaAgent(True, combined, 3)
        comb = CombinedAgent(True, combined, 3)
        self.assertTrue(mini.color)
        self.assertTrue(alph.color)
        self.assertTrue(comb.color)

    def test_agent_move(self):
        alph = AlphaBetaAgent(True, combined, 3)
        comb = CombinedAgent(True, combined, 3)
        board = chess.Board(fen='r1bqkb1r/pp1np1p1/2p2n1p/3p1p2/P3P2P/R1PP2PB/1P1N1P2/2BQK1NR w q - 0 1')
        alph_move = alph.get_move(board)
        comb_move = comb.get_move(board)


        self.assertTrue(board.is_legal(alph_move))
        self.assertTrue(board.is_legal(comb_move))

    def test_get_possible_moves(self):
        fen = 'rnb1kbnr/pppppppp/8/4q1R1/3B1P1P/3P4/PPP1P1P1/RN1QKBN1 w Qkq - 0 1'
        board = Board(fen=fen)
        moves = get_possible_moves(board, True, [], 1)
        self.assertEqual(str(moves[0].uci()), "f4e5")
        self.assertEqual(str(moves[1].uci()), "d4e5")
        self.assertEqual(str(moves[2].uci()), "g5e5")

    def test_capture_moves(self):
        fen = 'rnb1kbn1/pppppppp/1r6/2Q1q1R1/3B1P1P/8/PPPPP1P1/RN2KBN1 w Qq - 0 1'
        board = Board(fen=fen)
        captures = capture_moves(board, True)
        self.assertEqual(str(captures['winning'][0].uci()), 'f4e5')
        self.assertEqual(str(captures['neutral'][0].uci()), 'c5e5')
        self.assertEqual(str(captures['losing'][0].uci()), 'g5g7')

    def test_trans_table(self):
        table = {}
        board = Board()
        val = piece_value_heuristic(board, True, True)
        board_hash = hash_(board)
        table[board_hash] = val
        write_trans_table(table, os.getcwd()+'/data/test/test_trans.pickle')

        tt = read_trans_table(os.getcwd()+'/data/test/test_trans.pickle')
        self.assertEqual(tt[board_hash], val)


if __name__ == '__main__':
    unittest.main()