from logger import setup_logger
from communication.agent import Agent
import config

log = setup_logger(__name__)

class Sender(Agent):

    def __init__(self, name):
        super().__init__(name)

    def new_message(self):
        if self.output_buffer != None:
            log.warning("Output buffer full, new message blocked.")            
        self.output_buffer = self.message_list[-1].event(self.clock)
        self.message_list.pop()

    def send(self):
        self.tick()
        if len(self.message_list) == 0:
            log.info("Sender message list empty, no message passed to channel.")
        else :
            self.connection.write(self.output_buffer.event(self.clock))

    def receive(self):
        message = self.back_connection.read()
        if message != None:
            if self.input_buffer != None:
                log.warning("Input buffer full, new message blocked")
            else :
                self.set_clock(message.clock)
                self.tick()
                self.input_buffer = message

    def step(self, physical_time):
        self.receive()
        self.acknowledge_input()
        if self.output_buffer == None:
            self.new_message()
        if physical_time % config.message_timeout == 0:
            self.send()

    def import_messages(self, messages):
        self.message_list += messages