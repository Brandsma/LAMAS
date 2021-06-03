from communication.channel import Channel
from communication.message import Message
from communication.process import Process
from logger import setup_logger
import logging
import config
log = setup_logger(__name__, level=logging.WARNING)


class Agent(Process):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.connection = None
        self.back_connection = None
        self.message_list = []
        self.output_buffer = None
        self.input_buffer = None

    def connect(self, channel):
        self.connection = channel

    # this seems pretty ugly, but I'll not mind for now, as it solves an otherwise difficult problem
    def connect_back(self, channel):
        self.back_connection = channel

    def acknowledge_input(self):
        # If there is a message in the input and the output, see if one acknowledges the other and stop sending
        log.info(self.print_buffers())
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

    def state(self):
        return " clock: {}|{}|{}|{}|{}".format(self.clock, self.name,
                                               self.read_buffer(self.input_buffer), self.read_buffer(
                                                   self.output_buffer),
                                               [m.read() for m in self.message_list])

    def read_buffer(self, buffer):
        if buffer == None:
            return (None, None)
        else:
            return (buffer.content, buffer.acknowledge_level)

    def print_buffers(self):
        print("agent {} input: {} output: {}".format(self.name,
                                                     self.read_buffer(self.input_buffer), self.read_buffer(self.output_buffer)))

    def print_messages(self):
        messages = [message.read() for message in self.message_list]
        print("Agent {} at time {} has messages {}.".format(
            self.name, self.clock, messages))
