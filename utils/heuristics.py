"""
Add heuristics here
"""
from chess import *
from typing import Dict, List
import collections
import random
from utils.state_identifier import eval_boardstate


def piece_value_heuristic(board: Board, color: bool, max_turn) -> int:
    score = 0
    opponent = not color
    board_size: int = 64

    for tile in range(0, board_size):
        current_piece = board.piece_at(tile)
        score = score + get_piece_value(current_piece, color)

    return score


def get_piece_value(piece: Piece, color: bool) -> int:
    if piece is None:
        return 0

    piece_values: Dict[str, int] = {"P": 1, "N": 3, "B": 3, "R": 5, "Q": 9, "K": 100}

    value = 0

    value = piece_values[piece.symbol().upper()]

    if piece.color != color:
        value = value * -1

    return value


def general_mobility(board: Board, max_turn: bool, state) -> int:
    if state['opening']:
        piece_mobility_values = {PAWN: 6, KNIGHT: 8, BISHOP: 8, ROOK: 5, QUEEN: 2, KING: 0}
    elif state['middlegame']:
        piece_mobility_values = {PAWN: 2, KNIGHT: 5, BISHOP: 5, ROOK: 6, QUEEN: 6, KING: 1}
    elif state['endgame']:
        piece_mobility_values = {PAWN: 5, KNIGHT: 8, BISHOP: 8, ROOK: 5, QUEEN: 6, KING: 5}

    moves = [move.from_square for move in board.legal_moves]
    move_count = collections.Counter(moves)
    mobility_score = 0
    for move in move_count.keys():
        piece = board.piece_at(move)
        num_moves = move_count[move]
        mobility_score += num_moves * piece_mobility_values[piece.piece_type]

    if not max_turn:
        mobility_score = mobility_score * -1

    return int(mobility_score/2)


# Find potential victims -> then for each victim find least valuable aggressor
@DeprecationWarning
def mvvlva(board: Board, color: bool):
    pieces = PIECE_TYPES[:-1]
    mvv_locations = []
    moves = []
    # Victim cycle -> find MVV
    for piece in pieces[::-1]:
        # Get the location(s) of the given piece type for the opponent
        location = board.pieces(piece, not color)
        attackers = []
        if len(location) > 0:
            # Check to see that mvv can be attacked
            for l in location:
                attkr_locations = board.attackers(color, l)
                attackers += list(attkr_locations)
            if len(attackers) > 0:
                mvv_locations = location
                break

    if len(attackers) > 0:
        # Aggressor Cycle -> find the least valuable aggressor for the victim
        for l in mvv_locations:
            piece_to_location = [{"piece": board.piece_at(x), "from_square": x, "to_square": l} for x in attackers]
            sorted_pieces = sorted(piece_to_location, key=lambda x: x['piece'].piece_type)
            for x in sorted_pieces:
                m = Move(x['from_square'], x['to_square'])
                if board.is_legal(m):
                    moves.append(m)
    return moves


# winning capture = small piece captures bigger piece e.g. pawn captures knight
# nuetral capture = piece captures other piece of same value
# losing capture = higher value piece captures lower value piece
def capture_moves(board: Board, color: bool):
    pieces = PIECE_TYPES[:-1]
    can_be_captured = []
    # find piece locations for opponents
    for piece in pieces[::-1]:
        locations = board.pieces(piece, not color)
        if len(locations) > 0:
            # for each piece locate potential attackers
            for l in locations:
                attk_locations = list(board.attackers(color, l))
                if len(attk_locations) > 0:
                    # if there are attackers associate victim to attacker and add to list
                    piece_to_location = [
                        {"victim": board.piece_at(l), "attacker": board.piece_at(x), "from_square": x,
                         "to_square": l} for x in attk_locations]
                    can_be_captured.append(piece_to_location)

    # for all possible captures, find pieces that will do the capture
    winning_moves = []
    neutral_moves = []
    losing_moves = []
    for target in can_be_captured:
        for move in target:
            m = Move(move['from_square'], move['to_square'])
            if board.is_legal(m):
                if move['victim'].piece_type > move['attacker'].piece_type:
                    winning_moves.append((move, m))
                elif move['victim'].piece_type == move['attacker'].piece_type:
                    neutral_moves.append((move, m))
                else:
                    losing_moves.append((move, m))

    winning = sorted(winning_moves, key=lambda x: x[0]['victim'].piece_type-x[0]['attacker'].piece_type, reverse=True) if len(winning_moves) > 1 else winning_moves
    neutral = sorted(neutral_moves, key=lambda x: x[0]['victim'].piece_type) if len(neutral_moves) > 1 else neutral_moves
    losing = sorted(losing_moves, key=lambda x: x[0]['attacker'].piece_type) if len(losing_moves) > 1 else losing_moves

    captures = {
        'winning': [move[1] for move in winning],
        'neutral': [move[1] for move in neutral],
        'losing': [move[1] for move in losing]
    }
    return captures


def combined(board: Board, color: bool, max_turn: bool) -> int:
    state = eval_boardstate(board, max_turn)
    score = piece_value_heuristic(board, color, max_turn) + general_mobility(board, max_turn, state)
    return score


def sort_non_captures(history, turn, moves, board):
    # sort moves by hh:
    moves_to_values = []
    for m in moves:
        p = board.piece_at(m.from_square).piece_type
        val = history[turn][p][m.to_square]
        moves_to_values.append({'move': m, 'val': val})

    sorted_non_caps = sorted(moves_to_values, key=lambda x: x['val'], reverse=True)
    return [m['move'] for m in sorted_non_caps]


def get_possible_moves(board, turn, pv_line, current_depth, history=None):
    """
    returns a list of possible moves that can be made by the agent
    uses mvvlva and history table for move ordering
    :param board: the current board
    :param turn: bool
    :param history: history_table for agent
    :return: list of move objects
    """
    legal_moves = board.legal_moves
    pv = []
    '''
    if len(pv_line) > 1 and turn:
        pv = [pv_line[1]] if pv_line[1] in legal_moves else []

    if len(pv_line) > 0 and not turn:
        pv = [pv_line[0]] if pv_line[0] in legal_moves else []
    '''
    if len(pv_line) > current_depth+1:
        pv = [pv_line[current_depth+1]] if pv_line[current_depth+1] in legal_moves else []




    # Get sorted capture moves:
    captures = capture_moves(board, turn)

    # get non-captures:
    non_captures = [move for move in legal_moves if move not in captures['winning'] and move not in captures['neutral'] and move not in captures['losing']]

    # sort non_captures with HH:
    sorted_non_caps = sort_non_captures(history, turn, non_captures, board)

    move_list = pv + captures['winning'] + captures['neutral'] + sorted_non_caps + captures['losing']

    return move_list


