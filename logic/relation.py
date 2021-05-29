from logic.state import State


class Relation:
    def __init__(self, first: State, second: State):
        self.first = first
        self.second = second
