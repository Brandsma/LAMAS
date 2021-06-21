from communication.agent import Agent
from communication import log
import config


class Sender(Agent):

    def __init__(self, name):
        super().__init__(name)

    def new_message(self):
        if self.output_buffer != None:
            log.warning("Output buffer full, new message blocked.")
        if len(self.send_message_list) == 0:
            log.info("Sender message list empty, no message passed to output buffer.")
        else :            
            self.output_buffer = self.send_message_list[0].event(self.clock)
            self.send_message_list.pop(0)

    def acknowledge_input(self):
        # If there is a message in the input and the output, see if one acknowledges the other and stop sending
        #log.info(self.print_buffers())
        if (self.output_buffer != None and self.input_buffer != None):
            # "I can stop sending this message, it has been acknowledged"
            if (self.input_buffer == self.output_buffer.acknowledge()):
                if (self.input_buffer.acknowledge_level < config.acknowledge_depth):
                    self.output_buffer = self.input_buffer.acknowledge()
                else:
                    self.output_buffer = None
                log.info("Output buffer changed.")
                self.input_buffer = None
            else:
                log.info(
                    "Something went wrong, unexpected acknowledge levels in sender buffers.")

    def step(self, physical_time):
        self.receive()
        if self.other_public_key == None:
            self.recognize_public_key()
        else :
            self.acknowledge_input()
        if self.output_buffer == None:
            self.new_message()
        if self.step_counter % config.message_timeout == 0:
            self.send()

    def import_messages(self, messages):
        self.send_message_list += messages