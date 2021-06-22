from communication.sender import Sender
from communication.receiver import Receiver
from communication import log
import config


# Communicator can do both sending and receiving
class Communicator(Sender, Receiver):

    def __init__(self, name, initiator):
        super().__init__(name)
        self.initiator = initiator

    def acknowledge_input(self):
        # If I'm not sending anything, acknowledge input
        if self.output_buffer == None: 
            if self.input_buffer.acknowledge_level < config.acknowledge_depth:
                self.output_buffer = self.input_buffer.acknowledge()

        # If I'm sending something...
        elif self.input_buffer == self.output_buffer.acknowledge():             # And input is an acknowledge of that
            if self.input_buffer.acknowledge_level < config.acknowledge_depth:  # And acknowledge depth is not reached
                self.output_buffer = self.input_buffer.acknowledge()            # Send a new acknowledge
            else :                                                              # If acknowledge depth has been reached
                self.output_buffer = None                                       # Clear output buffer
            self.input_buffer = None

        # If I'm the last to acknowledge a message, and I receive a new message
        elif self.input_buffer.acknowledge_level == 0 and self.output_buffer.acknowledge_level == config.acknowledge_depth:
            self.output_buffer = self.input_buffer.acknowledge()                # Acknowledge the new message

    def step(self, physical_time):
        self.receive()
        if self.other_public_key == None and config.encryption_protocol:
            self.recognize_public_key()
        if self.input_buffer != None:
            self.record_message()
            self.acknowledge_input()
        if self.output_buffer == None and (len(self.receive_message_list) > 0 or self.initiator): # New message only if I'm not sending anything, and I've received something or I am the initiator
            self.new_message()
        if self.step_counter % config.message_timeout == 0:
            self.send()