from chess import Board
import utils.heuristics
import math
from chess import *
from typing import Dict, List
import collections


def tapered_evaluation(board, color, max_turn):

    if board.is_checkmate() and board.turn != color:
        return math.inf

    middlegame_score = _middlegame_eval(board, color)
    endgame_score = _endgame_eval(board, color)
    phase = _phase(board)
    eval_ = ((middlegame_score * (256 - phase)) + (endgame_score * phase)) / 256

    return eval_

def _phase(board):
    pawn_phase = 0
    knight_phase = 1
    bishop_phase = 1
    rook_phase = 2
    queen_phase = 4
    total_phase = pawn_phase * 16 + knight_phase * 4 + bishop_phase * 4 + rook_phase * 4 + queen_phase * 2
    phase = total_phase

    phase -= len(board.pieces(1, 0)) * pawn_phase
    phase -= len(board.pieces(1, 1)) * pawn_phase
    phase -= len(board.pieces(2, 0)) * knight_phase
    phase -= len(board.pieces(2, 1)) * knight_phase
    phase -= len(board.pieces(3, 0)) * bishop_phase
    phase -= len(board.pieces(3, 1)) * bishop_phase
    phase -= len(board.pieces(4, 0)) * rook_phase
    phase -= len(board.pieces(4, 1)) * rook_phase
    phase -= len(board.pieces(5, 0)) * queen_phase
    phase -= len(board.pieces(5, 1)) * queen_phase

    phase = (phase * 256 + (total_phase / 2)) / total_phase

    return phase

def _middlegame_eval(board, color):
    eval_score = 0
    eval_score += utils.heuristics.piece_value_heuristic(board, color, None)
    eval_score += (_pawns_mg(board, color) - _pawns_mg(board, not color))
    eval_score += (_pieces_mg(board, color) - _pieces_mg(board, not color))
    eval_score += (_mobility(board, color) - _mobility(board, not color))
    eval_score += (_threats_mg(board, color) - _threats_mg(board, not color))
    return eval_score

def _pawns_mg(board, color):
    eval_score = 0
    board_size = 64
    pawn_location = []
    for tile in range(0, board_size):
        if board.piece_type_at(tile) == 1 and board.color_at(tile) == color:
            pawn_location.append(tile)
    for pawn in pawn_location:
        eval_score -= 5 if _isolated_pawn(board, color, pawn) else 0
        eval_score -= 10 if _doubled_pawn(board, color, pawn) else 0
        eval_score += 6 if _passed_pawn(board, color, pawn) else 0
        eval_score += 5 if _connected_rank_pawn(board, color, pawn) else 0
        eval_score += 8 if _connected_diag_pawn(board, color, pawn) else 0
    return eval_score

def _pieces_mg(board, color):
    board_size = 64
    eval_score = 0
    for tile in range(0, board_size):
        if 15 < tile < 48:
            eval_score += 21 if _outpost_pieces(board, color, tile) else 0
        eval_score -= 3 * _bishop_pawns(board, color, tile)
        eval_score += 10 * _rook_on_pawn(board, color, tile)
        eval_score += 20 if _rook_on_file(board, color, tile) else 0
        eval_score -= 45 if _attacked_queen(board, color, tile) else 0
    return eval_score

def _threats_mg(board, color):
    board_size = 64
    eval_score = 0
    for tile in range(0, board_size):
        eval_score += 65 if _hanging(board, color, tile) else 0
        eval_score += 120 if _threat_safe_pawn(board, color, tile) else 0

    return eval_score

# Threats Heuristics
def _hanging(board, color, square):
    if not _weak_enemies(board, color, square):
        return False
    else:
        return True

def _weak_enemies(board, color, square):
    if board.piece_type_at(square) is None or board.color_at(square) == color:
        return False
    if color:
        if square % 8 != 0:
            if board.piece_type_at(square - 1 - 8) == 1:
                return False
        if square % 8 != 7:
            if board.piece_type_at(square + 1 - 8) == 1:
                return False
        if board.is_attacked_by(color, square) and not board.is_attacked_by(not color, square):
            return True
        else:
            return False
    else:
        if square % 8 != 0:
            attacking_square = square - 1 + 8
            if attacking_square >= 64:
                return False
            if board.piece_type_at(attacking_square) == 1:
                return False
        if square % 8 != 7:
            attacking_square = square + 1 + 8
            if attacking_square >= 64:
                return False
            if board.piece_type_at(attacking_square) == 1:
                return False
        if board.is_attacked_by(color, square) and not board.is_attacked_by(not color, square):
            return True
        else:
            return False

def _threat_safe_pawn(board, color, square):
    if board.piece_type_at(square) is None:
        return False
    if not _attacked_by_pawn(board, color, square):
        return False
    square_x = square % 8
    if color:
        if square_x != 0:
            attacking_square = square - 1 - 8
            if attacking_square < 0:
                return False
            if _safe_pawn(board, color, square - 1 - 8):
                return True
        if square_x != 7:
            attacking_square = square + 1 - 8
            if attacking_square < 0:
                return False
            if _safe_pawn(board, color, square + 1 - 8):
                return True
    else:
        if square_x != 0:
            attacking_square = square - 1 + 8
            if attacking_square >= 64:
                return False
            if _safe_pawn(board, color, square - 1 + 8):
                return True
        if square_x != 7:
            attacking_square = square + 1 + 8
            if attacking_square >= 64:
                return False
            if _safe_pawn(board, color, square + 1 + 8):
                return True


# Mobility Heuristic
def _mobility(board, color):
    piece_mobility_values = {PAWN: 4, KNIGHT: 8, BISHOP: 8, ROOK: 5, QUEEN: 3, KING: 2}
    moves = [move.from_square for move in board.legal_moves]
    move_count = collections.Counter(moves)
    mobility_score = 0
    for move in move_count.keys():
        piece = board.piece_at(move)
        num_moves = move_count[move]
        mobility_score += num_moves * piece_mobility_values[piece.piece_type]

    return mobility_score

# Pieces Heuristics
def _outpost_pieces(board, color, square):
    if board.color_at(square) is not color:
        return False
    if color:
        if board.piece_type_at(square) == 2 or board.piece_type_at(square) == 3:
            if square % 8 != 0:
                if board.piece_type_at(square - 1 - 8) == 1:
                    return True
            elif square % 8 != 7:
                if board.piece_type_at(square + 1 - 8) == 1:
                    return True
    else:
        if board.piece_type_at(square) == 2 or board.piece_type_at(square) == 3:
            if square % 8 != 0:
                if board.piece_type_at(square - 1 + 8) == 1:
                    return True
            elif square % 8 != 7:
                if board.piece_type_at(square + 1 + 8) == 1:
                    return True
    return False

def _bishop_pawns(board, color, square):
    if board.piece_type_at(square) != 3 or board.color_at(square) is not color:
        return 0
    bishop_pawn_number = 0
    bishop_color = square % 2
    pawn_locations = board.pieces(1, color)
    for pawn in pawn_locations:
        if pawn % 2 == bishop_color:
            bishop_pawn_number += 1
    return bishop_pawn_number

def _rook_on_pawn(board, color, square):
    num_threatened_pawns = 0
    if board.piece_type_at(square) != 4 or board.color_at(square) is not color:
        return 0
    for attacking in board.attacks(square):
        if board.piece_type_at(attacking) == 1:
            num_threatened_pawns += 1
    return num_threatened_pawns

def _rook_on_file(board, color, square):
    if board.piece_type_at(square) != 4 or board.color_at(square) is not color:
        return False
    rook_location = square % 8
    for rank in range(0, 8):
        if board.piece_type_at(rook_location + rank) == 4 and board.color_at(rook_location + rank) == color:
            pass
        elif board.piece_type_at(rook_location + rank) is not None:
            return False
    return True

def _attacked_queen(board, color, square):
    if board.piece_type_at(square) != 5 or board.color_at(square) is not color:
        return False
    if board.is_attacked_by(not color, square):
        return True


# Pawn Heuristics
def _safe_pawn(board, color, square):
    if board.piece_type_at(square) == 1 and board.color_at(square) == color:
        if len(board.attackers(not color, square)) != 0:
            return False
        else:
            return True

def _isolated_pawn(board, color, square):
    square_x = square % 8
    if color:
        for y in range(0, 8):
            if square_x != 0:
                if board.piece_type_at(square_x - 1 + y) is not None:
                    return False
            if square_x != 7:
                if board.piece_type_at(square_x + 1 + y) is not None:
                    return False
    else:
        for y in range(0, 8):
            if square_x != 0:
                if board.piece_type_at(square_x - 1 - y) is not None:
                    return False
            if square_x != 7:
                if board.piece_type_at(square_x + 1 - y) is not None:
                    return False
    return True

def _doubled_pawn(board, color, square):
    if color:
        if board.piece_type_at(square+8) == 1 and board.color_at(square+8) == color:
            return True
    else:
        if board.piece_type_at(square-8) == 1 and board.color_at(square-8) == color:
            return True
    return False

def _passed_pawn(board, color, square):
    if color:
        if square >= 32:
            return True
    else:
        if square <= 31:
            return True
    return False

def _connected_rank_pawn(board, color, square):
    if square % 8 != 0:
        if board.piece_type_at(square - 1) == 1:
            return True
    if square % 8 != 7:
        if board.piece_type_at(square + 1) == 1:
            return True
    return False

def _connected_diag_pawn(board, color, square):
    if color:
        if square % 8 != 0:
            if board.piece_type_at(square - 1 + 8) == 1:
                return True
        if square % 8 != 7:
            if board.piece_type_at(square + 1 + 8) == 1:
                return True
    else:
        if square % 8 != 0:
            if board.piece_type_at(square - 1 - 8) == 1:
                return True
        if square % 8 != 7:
            if board.piece_type_at(square + 1 - 8) == 1:
                return True
    return False

def _attacked_by_pawn(board, color, square):
    square_x = square % 8
    if color:
        if square_x != 0:
            attacking_square = square - 1 + 8
            if attacking_square >= 64:
                return False
            if board.piece_type_at(attacking_square) == 1 and board.color_at(attacking_square) != color:
                return True
        if square_x != 7:
            attacking_square = square + 1 + 8
            if attacking_square >= 64:
                return False
            if board.piece_type_at(attacking_square) == 1 and board.color_at(attacking_square) != color:
                return True
    else:
        if square_x != 0:
            attacking_square = square - 1 - 8
            if attacking_square < 0:
                return False
            if board.piece_type_at(attacking_square) == 1 and board.color_at(attacking_square) != color:
                return True
        if square_x != 7:
            attacking_square = square + 1 - 8
            if attacking_square < 0:
                return False
            if board.piece_type_at(attacking_square) == 1 and board.color_at(attacking_square) != color:
                return True
    return False

def _endgame_eval(board, color):
    eval_score = 0
    eval_score += utils.heuristics.piece_value_heuristic(board, color, None)
    eval_score += (_pawns_eg(board, color) - _pawns_eg(board, not color))
    eval_score += (_pieces_eg(board, color) - _pieces_eg(board, not color))
    eval_score += (_mobility(board, color) - _mobility(board, not color))
    eval_score += (_threats_eg(board, color) - _threats_eg(board, not color))
    return eval_score

def _pawns_eg(board, color):
    eval_score = 0
    board_size = 64
    pawn_location = []
    for tile in range(0, board_size):
        if board.piece_type_at(tile) == 1 and board.color_at(tile) == color:
            pawn_location.append(tile)
    for pawn in pawn_location:
        eval_score -= 15 if _isolated_pawn(board, color, pawn) else 0
        eval_score -= 20 if _doubled_pawn(board, color, pawn) else 0
        eval_score += 25 if _passed_pawn(board, color, pawn) else 0
        eval_score += 16 if _connected_rank_pawn(board, color, pawn) else 0
        eval_score += 17 if _connected_diag_pawn(board, color, pawn) else 0
    return eval_score

def _pieces_eg(board, color):
    board_size = 64
    eval_score = 0
    for tile in range(0, board_size):
        if 15 < tile < 48:
            eval_score += 15 if _outpost_pieces(board, color, tile) else 0
        eval_score -= 7 * _bishop_pawns(board, color, tile)
        eval_score += 35 * _rook_on_pawn(board, color, tile)
        eval_score += 12 if _rook_on_file(board, color, tile) else 0
        eval_score -= 14 if _attacked_queen(board, color, tile) else 0
    return eval_score

def _threats_eg(board, color):
    board_size = 64
    eval_score = 0
    for tile in range(0, board_size):
        eval_score += 35 if _hanging(board, color, tile) else 0
        eval_score += 55 if _threat_safe_pawn(board, color, tile) else 0

    return eval_score