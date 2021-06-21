from communication.process import Process
from communication.agent import Agent
from communication.sender import Sender
from communication.receiver import Receiver
from communication.communicator import Communicator
import config

class Eavesdropper(Process):

    def __init__(self, name):
        super().__init__()
        # Identification
        self.name = name

        # Fake Alice and Fake Bob, spoofed agents pretending to be someone else
        if config.two_way_communication:
            self.spoof_B = Communicator("Fake Bob", False)
            self.spoof_A = Communicator("Fake Alice", True)
        else :
            self.spoof_B = Receiver("Fake Bob") # Pretends to be Bob, the receiver, in communication with ALice
            self.spoof_A = Sender("Fake Alice") # Pretends to be Alice, the sender, in communication with Bob

        # Knowledge
        self.message_list = []
        self.knowledge = []

    def transfer(self): # NOTE Asynchronous now, rewrite when done to sync
        # If Fake Bob learned anything
        if len(self.difference_lists(self.spoof_B.receive_message_list, self.message_list)) > 0: # if there is a difference between the lists
            # Grab intel Fake Bob learned about
            transfer_message = self.spoof_B.receive_message_list[-1]
            
            # Transfer it to Eve's knowledge
            self.message_list.append(transfer_message)

            # Give it to Fake Alice to pass it on to Real Bob
            if type(transfer_message) != type(self.spoof_B.public_key):
                self.spoof_A.send_message_list.append(transfer_message)

    def difference_lists(self, li1, li2):
        return [i for i in li1 + li2 if i not in li1 or i not in li2]

    def public_announcement(self):
        # TODO
        pass

    def connect(self, conn_ea, conn_ae, conn_eb, conn_be,):
        self.spoof_B.connect(conn_ea, conn_ae) # Fake Bob connects as Bob with Alice
        self.spoof_A.connect(conn_eb, conn_be)

    def setup(self):
        self.spoof_B.setup()
        self.spoof_A.setup()

    def print_messages(self):
        self.spoof_B.print_messages()
        self.spoof_A.print_messages()
        messages = [message.read() for message in self.message_list]
        print("Agent {} at time {} has messages {}.".format(
            self.name, self.clock, messages))

    def state(self): # Lets give these fstrings a try eh?
        return f"{self.spoof_B.state()}\n{self.spoof_A.state()}"

    def step(self, physical_time):
        self.spoof_B.step(physical_time)
        self.transfer()
        self.spoof_A.step(physical_time)
        # if self.step_counter % config.eavesdropper_listen_rate == 0:
        #     self.listen()
        self.step_counter += 1