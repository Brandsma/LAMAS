from communication.agent import Agent

class Receiver(Agent):

    def __init__(self, name):
        super().__init__(name)

    def receive(self):
        self.tick()
        message = self.connection.read()
        self.message_list.append(message)
