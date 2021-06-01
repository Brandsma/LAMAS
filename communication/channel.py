from logger import setup_logger
from communication.message import Message
from communication.process import Process

log = setup_logger(__name__)

class Channel(Process):

    def __init__(self):
        super().__init__()
        self.input_buffer = None
        self.chute = []
        self.output_buffer = None

    def write(self, message): # send to the channel (used by sender)
        self.set_clock(message.clock)
        self.tick()
        if self.input_buffer != None:
            log.warning("Input buffer full, send blocked.")
        else :
            self.input_buffer = message.event(self.clock)

    def send(self): # perform sending action
        self.tick()
        if self.input_buffer == None:
            log.warning("Input buffer empty, aborting send.")
        else :
            self.chute.append(self.input_buffer.event(self.clock))
            self.input_buffer = None

    def listen(self): # listen to whats in the buffer, performed by eavesdrop
        self.tick()
        # NOTE important function, what message is received/ eavesdropped?
        if len(self.chute) > 0:
            return self.chute[len(self.chute)-1].event(self.clock)
        else :
            log.info("No message in chute to eavesdrop.")
            return None

    def receive(self):  # perform receive action
        self.tick()
        if self.output_buffer != None:
            log.warning("Output buffer full, receive blocked.")
        elif len(self.chute) == 0:
            log.info("No message in chute to receive.")
        else :
            self.output_buffer = self.chute[-1].event(self.clock)
            self.chute.pop()
            
    def read(self) -> Message: # receive from channel, performed by receiver
        self.tick()
        if self.output_buffer == None:
            log.info("No message in output buffer to read, returning None.")
            return None # Yeah I know, solve later
        else :
            message = self.output_buffer.event(self.clock)
            self.output_buffer = None
            return message

    def step(self, physical_time):
        self.print_status()
        if self.chute != []:
            self.receive()
        if self.input_buffer != None:
            self.send()

    def print_status(self):
        inp = None if self.input_buffer == None else self.input_buffer.read()
        out = None if self.output_buffer == None else self.output_buffer.read()
        chu = [m.read() for m in self.chute]

        print("Channel status: clock {} | inputbuffer {} | chute {} | outputbuffer {}"\
            .format(self.clock, inp, chu, out))