from communication.agent import Agent
from communication import log
import config


class Receiver(Agent):

    def __init__(self, name):
        super().__init__(name)

# Communication
    def acknowledge_input(self):
        self.output_buffer = self.input_buffer.acknowledge()

# Message handling
    def record_message(self):
        #hacky duplicate detection first TODO make real
        message = self.input_buffer
        if message == None:
            return
        if message not in self.receive_message_list and message.acknowledge_level == 0:
            self.receive_message_list.append(message)
            if config.interlock_protocol and type(message.read()) != type(self.public_key):
                self.other_interlock_switch = not self.other_interlock_switch

    def step(self, physical_time):
        self.receive()
        if self.other_public_key == None:
            self.recognize_public_key()
        if self.input_buffer != None:
            self.record_message()
            self.acknowledge_input() # NOTE: If things break, look here first
        if self.step_counter % config.message_timeout == 0:
            self.send()

