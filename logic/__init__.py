from logger import setup_logger
from logic.and_formula import And
from logic.not_formula import Not
from logic.or_formula import Or
from logic.atom_formula import Atom
from logic.implies_formula import Implies
from logic.state import State
from logic.kripkeModel import KripkeModel
from logic.logic_demo import logic_demo
import logging

logic_log = setup_logger(__name__, logging.WARNING)
