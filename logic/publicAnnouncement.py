from logic.formula import Formula
from logic import log


class PublicAnnouncement(Formula):
    def __init__(self, announcement: Formula, f2: Formula):
        self.announcement = announcement
        self.f2 = f2

    def __str__(self):
        return "[ " + str(self.announcement) + " ] " + str(self.f2)

    def evaluate(self, model, state) -> bool:
        # TODO: Check if this is correct
        if(not self.announcement.evaluate(model, state)):
            return False

        for s in model.states:
            # Remove all states from the Kripke Model that are not relevant anymore
            if(not self.announcement.evaluate(model, s)):
                model.remove_state(s)

        return self.f2.evaluate(model, state)
