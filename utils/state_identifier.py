from chess import Board
import math


def eval_boardstate(board, color, max_turn):
    eval_op = _eval_opening(board, color)
    eval_mg = _eval_middlegame(board, color)
    eval_eg = _eval_endgame(board, color)
    print(f"Opening Score: {eval_op} Middlegame Score: {eval_mg} Endgame Score: {eval_eg}")
    state = {"opening": 0, "middlegame": 0, "endgame": 0}
    if eval_op > eval_mg and eval_op > eval_eg:
        state["opening"] = 1
        return state
    elif eval_mg > eval_op and eval_mg > eval_eg:
        state["middlegame"] = 1
        return state
    else:
        state["endgame"] = 1
        return state


def _eval_opening(board, color):
    eval = 0
    if 12 > len(board.move_stack) > 0:
        eval += 600 * 1/len(board.move_stack)
    elif len(board.move_stack) == 0:
        eval = math.inf
    return eval


def _eval_middlegame(board, color):
    eval = 0
    eval += _attacking_king_zone_mg(board, color)
    eval += _material_mg(board, color)
    eval += _mobility_mg(board, color)
    eval += _pawn_structure_mg(board, color)
    eval = eval *.75
    return eval


def _eval_endgame(board, color):
    eval = 0
    eval += _king_mobility_eg(board, color)
    eval += _material_eg(board, color)
    return eval


def _material_mg(board, color):
    PAWN_VAL = 1
    BISHOP_VAL = 2
    KNIGHT_VAL = 2
    ROOK_VAL = 3
    QUEEN_VAL = 5

    num_pieces = 0
    for _ in range(1, 6):
        for color in range(1, 2):
            num_pieces += len(board.pieces(_, color))
    material = num_pieces * 7
    return material


def _attacking_king_zone_mg(board, color):
    # Attacking King Zone:
    PAWN_VAL = 5
    KNIGHT_VAL = 20
    BISHOP_VAL = 20
    ROOK_VAL = 40
    QUEEN_VAL = 80

    attack_pieces_count = 0
    value_of_attacks = 0
    attack_weight = [0, 50, 75, 88, 94, 97, 99]

    king = board.king(color)
    king_squares = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            spot = king + i + (j * 8)
            if 0 <= spot <= 63:
                king_squares.append(spot)
    for square in king_squares:
        if len(board.attackers(not color, square)) == 0:
            pass
        else:
            for attacker in board.attackers(not color, square):
                if board.piece_type_at(attacker) == 1:
                    attack_pieces_count += 1
                    value_of_attacks += PAWN_VAL
                elif board.piece_type_at(attacker) == 2:
                    attack_pieces_count += 1
                    value_of_attacks += KNIGHT_VAL
                elif board.piece_type_at(attacker) == 3:
                    attack_pieces_count += 1
                    value_of_attacks += BISHOP_VAL
                elif board.piece_type_at(attacker) == 4:
                    attack_pieces_count += 1
                    value_of_attacks += ROOK_VAL
                elif board.piece_type_at(attacker) == 5:
                    attack_pieces_count += 1
                    value_of_attacks += QUEEN_VAL
    if attack_pieces_count >= 7:
        attack_pieces_count = 6
        # Due to size of weight list, nothing more than 7 is worse than 7
    king_attack_score = (value_of_attacks * attack_weight[attack_pieces_count]) / 100

    return king_attack_score


def _mobility_mg(board, color):
    # Mobility
    #   Simply the number of moves (for now)
    num_moves = board.legal_moves.count()
    mobility = num_moves * 5
    return mobility


def _pawn_structure_mg(board, color):
    # Pawn Structure
    unmoved_pawns = 0
    if color:
        pawn_rank = [48, 49, 50, 51, 52, 53, 54, 55]
    else:
        pawn_rank = [8, 9, 10, 11, 12, 13, 14, 15]
    for square in pawn_rank:
        if board.piece_type_at(square) == 1:
            unmoved_pawns += 1
    pawn_structure_score = -1 * (unmoved_pawns * 10)
    return pawn_structure_score


def _king_mobility_eg(board, color):
    # King Mobility
    king = board.king(color)
    king_squares = []
    empty_squares = 0
    king_mobility = 0
    for i in range(-2, 3):
        for j in range(-2, 3):
            spot = king + i + (j * 8)
            if 0 <= spot <= 63:
                king_squares.append(spot)
    for square in king_squares:
        if board.piece_at(square) is None:
            empty_squares += 1
    king_mobility += empty_squares * 20
    return king_mobility


def _material_eg(board, color):
    num_pieces = 0
    for _ in range(1, 6):
        for color in range(1, 2):
            num_pieces += len(board.pieces(_, color))
    material = num_pieces * -7
    return material


## DATED METHOD WIP
def _middlegame_OLD(board, color) -> int:
    # Heuristic score for middlgame positioning
    # Primarily we care about king safety, but also mobility and pawn development (for now)
    middlegame_score = 0
    # Attacking King Zone:
    #   (and protective, or friendly, pawns)
    PAWN_VAL = 5
    KNIGHT_VAL = 20
    BISHOP_VAL = 20
    ROOK_VAL = 40
    QUEEN_VAL = 80

    attack_pieces_count = 0
    value_of_attacks = 0
    attack_Weight = [0, 50, 75, 88, 94, 97, 99]

    num_pawns = 0
    pawn_shield = 0
    king = board.king(color)
    king_squares = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            spot = king + i + (j * 8)
            if spot >= 0 and spot <= 63:
                king_squares.append(spot)
    for square in king_squares:
        if board.piece_type_at(square) == 1 and board.color_at(square) == color:
            num_pawns += 1
        if len(board.attackers(not color, square)) == 0:
            pass
        else:
            for attacker in board.attackers(not color, square):
                if board.piece_type_at(attacker) == 1:
                    attack_pieces_count += 1
                    value_of_attacks += PAWN_VAL
                elif board.piece_type_at(attacker) == 2:
                    attack_pieces_count += 1
                    value_of_attacks += KNIGHT_VAL
                elif board.piece_type_at(attacker) == 3:
                    attack_pieces_count += 1
                    value_of_attacks += BISHOP_VAL
                elif board.piece_type_at(attacker) == 4:
                    attack_pieces_count += 1
                    value_of_attacks += ROOK_VAL
                elif board.piece_type_at(attacker) == 5:
                    attack_pieces_count += 1
                    value_of_attacks += QUEEN_VAL
    if attack_pieces_count >= 7:
        attack_pieces_count = 6
        # Due to size of weight list, nothing more than 7 is worse than 7
    king_attack_score = (value_of_attacks * attack_Weight[attack_pieces_count]) / 100
    pawn_shield = num_pawns * 20
    middlegame_score -= king_attack_score
    middlegame_score += pawn_shield

    # Mobility
    #   Simply the number of moves (for now)
    num_moves = board.legal_moves.count()
    mobility = num_moves * 5
    middlegame_score += mobility

    # Pawn Structure
    unmoved_pawns = 0
    if color:
        pawn_rank = [48, 49, 50, 51, 52, 53, 54, 55]
    else:
        pawn_rank = [8, 9, 10, 11, 12, 13, 14, 15]
    for square in pawn_rank:
        if board.piece_type_at(square) == 1:
            unmoved_pawns += 1
    pawn_structure_score = -1 * (unmoved_pawns * 10)
    middlegame_score += pawn_structure_score
    return middlegame_score


def _endgame_OLD(board, color) -> int:
    # Heuristic score for endgame positioning
    #
    # King Mobility
    king = board.king(color)
    king_squares = []
    empty_squares = 0
    endgame_score = 0
    for i in range(-2, 3):
        for j in range(-2, 3):
            spot = king + i + (j * 8)
            if 0 <= spot <= 63:
                king_squares.append(spot)
    for square in king_squares:
        if board.piece_at(square) is None:
            empty_squares += 1
    endgame_score += empty_squares * 20
    num_pieces = 0
    for _ in range(1, 6):
        for color in range(1, 2):
            num_pieces += len(board.pieces(_, color)) * 5
    endgame_score -= num_pieces

    return endgame_score


def tapered_eval(board: Board, color, max_turn) -> int:
    # Returns a tapered eval score for the current board, this allows for smooth state changing
    middlegame_score = _middlegame_OLD(board, color)
    endgame_score = _endgame_OLD(board, color)
    phase = _phase(board)
    eval_ = ((middlegame_score * (256 - phase)) + (endgame_score * phase)) / 256

    #print(f"Eval: {eval_}")

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
## END
