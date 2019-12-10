from pickle import load, dump
from chess import *
from typing import Dict, Tuple
from chess import polyglot

Hash = int
LookupTable = Dict[Tuple[Square, PieceType, Color], Hash]
TransTable = Dict[Hash, float]


def hash_(board: Board) -> Hash:
    return polyglot.zobrist_hash(board)


def read_trans_table(path: str) -> TransTable:
    try:
        with open(path, 'rb') as f:
            return load(f)
    except OSError:
        return {}


def write_trans_table(trans_table: TransTable, path: str) -> None:
    with open(path, 'wb') as f:
        dump(trans_table, f)
