from logger import setup_logger
from logic.and_formula import And
from logic.not_formula import Not
from logic.or_formula import Or
from logic.atom_formula import Atom
from logic.implies_formula import Implies
from logic.state import State
from logic.kripkeModel import KripkeModel

log = setup_logger(__name__)


def main():
    log.info("Starting program...")

    and_form = Implies(And(Not(Atom(True)), Or(
        Not(Atom(False)), Atom(True))), Atom(True))
    print(str(and_form))

    state = State("12345")
    model = KripkeModel([], [])

    print(and_form.evaluate(model, state))


if __name__ == "__main__":
    main()
