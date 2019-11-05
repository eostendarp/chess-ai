class BaseAgent:
    def __init__(self, color):
        self.color = color

    def get_move(self, board):
        raise NotImplementedError
