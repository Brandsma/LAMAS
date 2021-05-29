from logic.formula import Formula


class Not(Formula):
    def __init__(self, f1: Formula):
        self.f1 = f1

    def __str__(self):
        return "~" + str(self.f1)

    def evaluate(self, model, state) -> bool:
        return not self.f1.evaluate(model, state)
