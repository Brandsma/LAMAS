from communication.agent import Agent
import config

class Eavesdropper(Agent):

    def __init__(self, name):
        super().__init__(name)

    def listen(self):
        message = self.connection.listen()
        if message != None:
            self.set_clock(message.clock)
            self.tick()
            self.message_list.append(message)

    def public_announcement(self):
        # TODO
        pass

    def step(self, physical_time):
        if self.step_counter % config.eavesdropper_listen_rate == 0:
            self.listen()
        self.step_counter += 1