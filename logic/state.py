from logic.relation import Relation
from typing import List


class State:
    def __init__(self, truth_definitions, relations: List[Relation]):
        self.truth_definitions = truth_definitions
        self.relations = relations

    def evaluate(self, atom):
        return self.truth_definitions[atom]

    def get_all_connected_states(self):
        connected = []
        for relation in self.relations:
            connected.append(relation.second)
        return connected

    def add_relation_to_state(self, state):
        self.relations.append(Relation(self, state))
