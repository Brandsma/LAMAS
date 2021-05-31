from communication.channel import Channel
from communication.message import Message

class Agent:

    def __init__(self, name):
        self.name = name
        self.connection = None
        self.message_list = []
        self.clock = 0
        self.event_log = []

    def connect(self, channel):
        self.connection = channel

    def print_messages(self):
        messages = [message.read() for message in self.message_list]
        print("Agent {} at time {} has messages {}.".format(self.name, self.clock, messages))

    def tick(self):
        self.clock += 1
