from communication.agent import Agent
from communication import log
import config


class Sender(Agent):

    def __init__(self, name):
        super().__init__(name)

    def new_message(self):
        if self.output_buffer != None:
            log.warning("Output buffer full, new message blocked.")
        if len(self.message_list) == 0:
            log.info("Sender message list empty, no message passed to output buffer.")
        else :            
            self.output_buffer = self.message_list[-1].event(self.clock)
            self.message_list.pop()

    def send(self):
        self.tick()
        if self.output_buffer != None:
            self.connection.write(self.output_buffer.event(self.clock))
        else :
            log.info("Output buffer empty, no new message passed to channel.")

    def receive(self):
        message = self.back_connection.read()
        if message != None:
            if self.input_buffer != None:
                log.warning("Input buffer full, buffer overwritten.")
            self.set_clock(message.clock)
            self.tick()
            self.input_buffer = message

    def step(self, physical_time):
        self.receive()
        self.acknowledge_input()
        if self.output_buffer == None:
            self.new_message()
        if self.step_counter % config.message_timeout == 0:
            self.send()

    def import_messages(self, messages):
        self.message_list += messages