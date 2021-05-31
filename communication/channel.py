from logger import setup_logger
from communication.message import Message

log = setup_logger(__name__)

class Channel:

    def __init__(self):
        self.input_buffer = None
        self.chute = []
        self.output_buffer = None
        self.clock = 0

    def write(self, message): # send to the channel (used by sender)
        self.tick()
        if self.input_buffer != None:
            log.warning("Input buffer full, send blocked.")
        else :
            self.input_buffer = message

    def send(self): # perform sending action
        self.tick()
        if self.input_buffer == None:
            log.warning("Input buffer empty, aborting send.")
        else :
            self.chute.append(self.input_buffer)
            self.input_buffer = None

    def listen(self): # listen to whats in the buffer, performed by eavesdrop
        self.tick()
        # NOTE important function, what message is received/ eavesdropped?
        if len(self.chute) > 0:
            return self.chute[len(self.chute)-1]
        else :
            log.warning("No message in chute to eavesdrop.")
            return None

    def receive(self):  # perform receive action
        self.tick()
        if self.output_buffer != None:
            log.warning("Output buffer full, receive blocked.")
        elif len(self.chute) == 0:
            log.warning("No message in chute to receive.")
        else :
            self.output_buffer = self.chute[-1]
            self.chute.pop()
            
    def read(self) -> Message: # receive from channel, performed by receiver
        self.tick()
        if self.output_buffer == None:
            log.warning("No message in output buffer to read, returning None.")
            return None # Yeah I know, solve later
        else :
            message = self.output_buffer
            self.output_buffer = None
            return message

    def tick(self):
        self.clock += 1