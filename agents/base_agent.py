from chess import *
class BaseAgent:
    def __init__(self, color: bool):
        self.color = color

    def get_move(self, board: Board) -> Move:
        raise NotImplementedError
