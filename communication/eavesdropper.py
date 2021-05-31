from communication.agent import Agent


class Eavesdropper(Agent):

    def __init__(self, name):
        super().__init__(name)

    def listen(self):
        self.tick()
        message = self.connection.listen()
        self.message_list.append(message)
