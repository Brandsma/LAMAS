from logic.formula import Formula


class And(Formula):
    def __init__(self, f1: Formula, f2: Formula):
        self.f1 = f1
        self.f2 = f2

    def __str__(self):
        return "(" + str(self.f1) + " & " + str(self.f2) + ")"

    def evaluate(self, model, state) -> bool:
        return self.f1.evaluate(model, state) and self.f2.evaluate(model, state)
