from communication.agent import Agent


class Eavesdropper(Agent):

    def __init__(self, name):
        super().__init__(name)

    def listen(self):
        message = self.connection.listen()
        if message != None:
            self.set_clock(message.clock)
            self.tick()
            self.message_list.append(message)

    def step(self, physical_time):
        self.listen()