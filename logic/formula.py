from abc import ABC, abstractmethod

from logic.kripkeModel import KripkeModel
from logic.state import State


class Formula(ABC):
    @abstractmethod
    def evaluate(self, model: KripkeModel, s: State) -> bool:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    def __repr__(self):
        return str(self)
