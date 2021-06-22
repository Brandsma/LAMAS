from logic.formula import Formula


class Atom(Formula):
    def __init__(self, f1: str):
        self.f1 = f1

    def __str__(self):
        return self.f1

    def evaluate(self, model, state) -> bool:
        return state.evaluate(self.f1)
