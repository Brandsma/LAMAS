from logic.formula import Formula


class Atom(Formula):
    def __init__(self, f1: bool):
        self.f1 = f1

    def __str__(self):
        return str(self.f1)

    def evaluate(self, model, state) -> bool:
        return self.f1
