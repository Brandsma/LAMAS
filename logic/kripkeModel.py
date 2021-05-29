from logic.state import State
from logic.relation import Relation
from typing import List


class KripkeModel:
    def __init__(self, states: List[State], relations: List[Relation]):
        self.states = states
        self.relations = relations

    def add_state(self, state: State):
        self.states.append(state)

    def remove_state(self, state: State):
        self.states.remove(state)
