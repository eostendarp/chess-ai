from chess import Board

def tapered_eval(board: Board, color) -> int:
    # Returns a tapered eval score for the current board, this allows for smooth state changing
    middlegame_score = _middlegame(board, color)
    endgame_score = _endgame(board, color)

    pawn_phase = 0
    knight_phase = 1
    bishop_phase = 1
    rook_phase = 2
    queen_phase = 4
    total_phase = pawn_phase*16 + knight_phase*4 + bishop_phase*4 + rook_phase*4 + queen_phase*2
    phase = total_phase

    phase -= len(board.pieces(1, 0))
    phase -= len(board.pieces(1, 1))
    phase -= len(board.pieces(2, 0))
    phase -= len(board.pieces(2, 1))
    phase -= len(board.pieces(3, 0))
    phase -= len(board.pieces(3, 1))
    phase -= len(board.pieces(4, 0))
    phase -= len(board.pieces(4, 1))
    phase -= len(board.pieces(5, 0))
    phase -= len(board.pieces(5, 1))

    phase = (phase * 256 + (total_phase / 2)) / total_phase

    eval = ((middlegame_score * (256 - phase)) + (endgame_score * phase)) / 256

    print(f"Middle: {middlegame_score} End: {endgame_score} Eval: {eval}")

    return eval

def _middlegame(board, color) -> int:
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
            spot = king+i+(j*8)
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
    king_attack_score = (value_of_attacks * attack_Weight[attack_pieces_count])/100
    pawn_shield = num_pawns * 20
    middlegame_score -= king_attack_score
    middlegame_score += pawn_shield

    # Mobility
    #   Simply the number of moves (for now)
    num_moves = board.legal_moves.count()
    mobility = num_moves * 10
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
    pawn_structure_score = -1*(unmoved_pawns * 20)
    middlegame_score += pawn_structure_score

    return middlegame_score

def _endgame(board, color) -> int:
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
            if spot >= 0 and spot <= 63:
                king_squares.append(spot)
    for square in king_squares:
        if board.piece_at(square) == None:
            empty_squares += 1
    endgame_score += empty_squares*20
    return endgame_score