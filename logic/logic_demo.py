from logger import setup_logger
from logic.and_formula import And
from logic.not_formula import Not
from logic.or_formula import Or
from logic.atom_formula import Atom
from logic.implies_formula import Implies
from logic.knowledge_formula import Knows
from logic.state import State
from logic.kripkeModel import KripkeModel

log = setup_logger(__name__)


def logic_demo():
    log.info("Logic demo")
    # knows_form = Knows("A", And(Not(Atom('P')), Or(
    #     Not(Atom('Q')), Atom('P'))))
    knows_form = Knows("A", Atom("P"))
    print(str(knows_form))

    state_A = State({'P': True, 'Q': False}, [])
    state_B = State({'P': True, 'Q': False}, [])
    state_A.add_relation_to_state(state_B)
    state_B.add_relation_to_state(state_A)

    model = KripkeModel([], [])

    print(knows_form.evaluate(model, state_A))
