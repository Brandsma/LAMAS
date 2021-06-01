from logger import setup_logger
from communication.agent import Agent

log = setup_logger(__name__)

class Sender(Agent):

    def __init__(self, name):
        super().__init__(name)

    def send(self, message):
        self.tick()
        self.connection.write(self, message)

    def send(self):
        self.tick()
        if len(self.message_list) == 0:
            log.warning("Sender message list empty, no message passed to channel.")
        else :
            self.connection.write(self.message_list[-1])
            self.message_list.pop()

    def import_messages(self, messages):
        self.message_list += messages