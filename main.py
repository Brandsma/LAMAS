from logger import setup_logger
from logic.and_formula import And
from logic.not_formula import Not
from logic.or_formula import Or
from logic.atom_formula import Atom
from logic.implies_formula import Implies
from logic.state import State
from logic.kripkeModel import KripkeModel
from logic.logic_demo import logic_demo
from communication import communication_demo
import logging

log = setup_logger(__name__, logging.INFO)

def main():
    log.info("Starting program...")
    #logic_demo()
    communication_demo()


if __name__ == "__main__":
    main()
