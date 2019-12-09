from random import randint
from pickle import load, dump
from chess import *
from typing import Dict, Tuple


LookupTable = Dict[Tuple[Square, PieceType, Color], int]
TransTable = Dict[int, float]


def random_bitstring(length: int = 64) -> int:
    return randint(0, 2 ** length - 1)


def gen_lookup_table() -> LookupTable:
    table: LookupTable = {}
    for s in SQUARES:
        for p in PIECE_TYPES:
            for c in COLORS:
                table[(s, p, c)] = random_bitstring()
    return table


def hash_(lookup_table: LookupTable, board: Board):
    h: int = 0
    for s in SQUARES:
        p: Piece = board.piece_at(s)
        if p is not None:
            c: Color = p.color
            h ^= lookup_table[(s, p.piece_type, c)]
    return h


def read_trans_table(path: str) -> TransTable:
    try:
        with open(path, 'rb') as f:
            return load(f)
    except OSError:
        return {}


def read_lookup_table(path: str) -> LookupTable:
    try:
        with open(path, 'rb') as f:
            return load(f)
    except OSError:
        return gen_lookup_table()


def write_trans_table(trans_table: TransTable, path: str) -> None:
    with open(path, 'wb') as f:
        dump(trans_table, f)


def write_lookup_table(lookup_table: LookupTable, path: str) -> None:
    with open(path, 'wb') as f:
        dump(lookup_table, f)
