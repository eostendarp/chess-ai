from chess import *
class BaseAgent:
    """
    Base Agent All Other Agents Inherit from
    """
    def __init__(self, color: bool):
        self.color = color

    def get_move(self, board: Board) -> Move:
        raise NotImplementedError
