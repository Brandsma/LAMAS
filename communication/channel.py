from communication.message import Message
from communication.process import Process
from communication import log
import config

class Channel(Process):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.input_buffer = None
        self.chute = []
        self.output_buffer = None

    def write(self, message):  # send to the channel (used by sender)
        self.set_clock(message.clock)
        self.tick()
        if self.input_buffer != None:
            log.warning("Input buffer full, send blocked.")
        else:
            self.input_buffer = message.event(self.clock)

    def send(self):  # perform sending action
        self.tick()
        if self.input_buffer == None:
            log.warning("Input buffer empty, aborting send.")
        else:
            self.chute.append(self.input_buffer.event(self.clock))
            self.input_buffer = None

    def listen(self):  # listen to whats in the buffer, performed by eavesdrop
        self.tick()
        # NOTE important function, what message is received/ eavesdropped?
        if len(self.chute) > 0:
            return self.chute[len(self.chute)-1].event(self.clock)
        else:
            log.info("No message in chute to eavesdrop.")
            return None

    def receive(self):  # perform receive action -- move message from chute to output buffer
        self.tick()
        if self.output_buffer != None:
            log.warning("Output buffer full, receive blocked.")
        elif len(self.chute) == 0:
            log.info("No message in chute to receive.")
        else:
            self.output_buffer = self.chute[-1].event(self.clock)
            self.chute.pop()  # TODO

    def read(self) -> Message:  # receive from channel, performed by receiver
        self.tick()
        if self.output_buffer == None:
            log.debug("No message in output buffer to read, returning None.")
            return None  # Yeah I know, solve later
        else:
            message = self.output_buffer.event(self.clock)
            self.output_buffer = None
            return message

    def step(self, physical_time):
        if config.print_channel_content:
            self.print_status()
        if self.chute != []:
            self.receive()
        if self.input_buffer != None:
            self.send()

    def state(self):
        return " clock: {}|{}|{}|{}|{}".format(self.clock, self.name,
                                               self.read_buffer(self.input_buffer), self.read_buffer(
                                                   self.output_buffer),
                                               [(m.read(), m.acknowledge_level) for m in self.chute])

    def read_buffer(self, buffer):
        if buffer == None:
            return (None, None)
        else:
            return (buffer.content, buffer.acknowledge_level)

    def print_status(self):
        inp = None if self.input_buffer == None else self.input_buffer.read()
        inp_ack = None if self.input_buffer == None else self.input_buffer.acknowledge_level
        out = None if self.output_buffer == None else self.output_buffer.read()
        out_ack = None if self.output_buffer == None else self.output_buffer.acknowledge_level
        chu = [m.read() for m in self.chute]

        print("Channel {} status: clock {} | inputbuffer {} {}| chute {} | outputbuffer {} {}"
              .format(self.name, self.clock, inp, inp_ack, chu, out, out_ack))
