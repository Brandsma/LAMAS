from logic.formula import Formula


class Knows(Formula):
    def __init__(self, agent, f1: Formula):
        self.agent = agent
        self.f1 = f1

    def __str__(self):
        return "K_{" + str(self.agent) + "}( " + str(self.f1) + " )"

    def evaluate(self, model, state) -> bool:
        connected_states = state.get_all_connected_states()
        connected_states.append(state)
        knows = True
        for curr_state in connected_states:
            # If any of the connected states is false, then the agent does not know
            if not self.f1.evaluate(model, curr_state):
                knows = False
        return knows
