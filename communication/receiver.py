from logger import setup_logger
from communication.agent import Agent
import config
log = setup_logger(__name__)

class Receiver(Agent):

    def __init__(self, name):
        super().__init__(name)

    def send(self):
        if self.output_buffer != None:
            self.back_connection.write(self.output_buffer.event(self.clock))

    def receive(self):
        message = self.connection.read()
        if message != None:
            if self.input_buffer != None:
                log.warning("Input buffer full, buffer overwritten.")            
            self.set_clock(message.clock)
            self.tick()
            self.input_buffer = message
            self.output_buffer = self.input_buffer.acknowledge()
            #hacky duplicate detection first TODO make real
            if message not in self.message_list and message.acknowledge_level == 0:
                self.message_list.append(message)

    def step(self, physical_time):
        self.receive()
        self.acknowledge_input()
        if physical_time % config.message_timeout == 0:
            self.send()

