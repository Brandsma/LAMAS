from communication.channel import Channel
from communication.message import Message
from communication.process import Process
from communication import log
import config
import rsa

class Agent(Process):

    def __init__(self, name):
        super().__init__()
        # Identification
        self.name = name

        # Knowledge
        self.send_message_list = []
        self.receive_message_list = []
        self.knowledge = []

        # Communication
        self.outgoing_connection = None
        self.incomming_connection = None
        self.output_buffer = None
        self.input_buffer = None
            # Encryption
        self.private_key = None
        self.public_key = None
        self.other_public_key = None
        self.interlock_switch = False   # Used to keep track of which half to send and when to remove a message from the message list. Switches at new message
        # When TRUE --> access first part of the broken message to send When TRUE --> 
        self.other_interlock_switch = False # Used to keep track of which half is sent to us so we know when to stitch. Switches at record message
        self.second_half = None
        # When TRUE --> We have the first half stored in ciphertext, now we can concat the second part and decrypt. When FALSE --> We receive the first part, don't decrypt

# Communication
    def connect(self, outgoing, incomming): # Open-closed principle
        self.connect_outgoing(outgoing)
        self.connect_incomming(incomming)

    # Agent writes messages to the outgoing channel
    def connect_outgoing(self, channel):
        self.outgoing_connection = channel

    # Agent listens to messages from the incomming channel
    def connect_incomming(self, channel):
        self.incomming_connection = channel

    def send(self): # NOTE possible dependency problem -- depends on lower level function. Fixed by fixing the forward/backward connection to be sender and receiver channels
        # If there is something to send
        if self.output_buffer != None:
            # And we need to encrypt it
            if config.encryption_protocol and type(self.output_buffer.get_content()) != type(self.public_key):
                print(f"{self.name} encrypting message {self.output_buffer.read()}")
                message = self.encrypt_message(self.output_buffer)
            # Or we send it raw
            else :
                message = self.output_buffer
            # If we interlock, split the message and update the switch
            if config.interlock_protocol and type(self.output_buffer.get_content()) != type(self.public_key) and self.interlock_switch:
                message, self.second_half = self.split_message(message)
            # Send either the first or second part, depending on the switch
            elif config.interlock_protocol and type(self.output_buffer.get_content()) != type(self.public_key) and not self.interlock_switch:
                message = self.second_half
            # Send the message
            print(f"{self.name} sending message {message.read()}")
            self.send_message(message)
        else :
            log.info("Output buffer empty, no new message passed to channel.")

    def receive(self):
        message = self.receive_message()
        # If we received something
        if message != None:
            self.set_clock(message.clock)
            self.tick()
            if self.input_buffer != None:
                log.warning("Input buffer full, buffer overwritten.")
            # If the interlock protocol is on, we need to stitch the message
            if config.interlock_protocol and type(message.get_content()) != type(self.public_key) and self.other_interlock_switch:
                part_1 = self.receive_message_list[-1]
                if part_1 != message:               # TODO refractor this -- this gives incorrect behaviour as an even-character palindrome not work anymore. Solves duplication from early rounds
                    self.receive_message_list.pop() # TODO refractor this
                    message = self.stitch_message(part_1, message)
            if config.encryption_protocol and type(message.get_content()) != type(self.public_key) and config.interlock_protocol and self.other_interlock_switch:
                self.input_buffer = self.decrypt_message(message)
            elif (not config.interlock_protocol) and config.encryption_protocol and type(message.get_content()) != type(self.public_key):
                self.input_buffer = self.decrypt_message(message)
            else :
                self.input_buffer = message
                
    def send_message(self, message):
        self.tick()
        self.outgoing_connection.write(message.event(self.clock))

    def receive_message(self):
        return self.incomming_connection.read()

# Interlocking protocol
    # TODO Refractor send & receive to look nicer

# Encryption
    def generate_keys(self):
        (self.public_key, self.private_key) = rsa.newkeys(512)

    def set_other_public_key(self, public_key):
        self.other_public_key = public_key

    def encrypt_message(self, message):
        plaintext = message.get_content().encode('utf8')            # RSA only operates on bytes
        ciphertext = rsa.encrypt(plaintext, self.other_public_key)  # Encrypt the message using the others public key        
        encrypted_message = message.copy()                           # Set the content of the message to the ciphertext
        encrypted_message.set_content(ciphertext)
        return encrypted_message

    def decrypt_message(self, message): # inverse of the encrypt_message function
        ciphertext = message.get_content()
        plaintext = rsa.decrypt(ciphertext, self.private_key)
        decrypted_message = message.copy()
        decrypted_message.set_content(plaintext.decode('utf8'))
        return decrypted_message

    def split_message(self, message):
        content = message.get_content()
        print(f"{self.name} {content = }")
        split_1, split_2 = content[0:len(content)//2], content[len(content)//2:len(content)] # Split message in half
        message_1 = message.copy()
        message_2 = message.copy()
        message_1.set_content(split_1)
        message_2.set_content(split_2)
        return message_1, message_2

    def stitch_message(self, message_1, message_2):
        split_1, split_2 = message_1.get_content(), message_2.get_content()
        message = message_2.copy()
        message.set_content(split_1 + split_2)
        print(f"{self.name} stitching {split_1} with {split_2} for {message.read()}")
        return message

    def recognize_public_key(self):
        if self.other_public_key == None and self.input_buffer != None and \
            type(self.input_buffer.get_content()) == type(self.public_key) and \
            self.input_buffer.get_content() != self.public_key:
            #print(f"{self.name = } Set other public key {self.input_buffer.get_content()}")
            self.set_other_public_key(self.input_buffer.get_content())

    def setup(self):
        if config.encryption_protocol:
            self.generate_keys()
            # First message out is a public key
            if config.two_way_communication:
                self.send_message_list.insert(0, Message(self.public_key))
            else :  # If communication is one-way, receiver never sends their key, so it is placed in the buffer immediately
                self.output_buffer = Message(self.public_key)
            #print(f"{self.name = } {self.public_key}")

# Reporters
    def state(self):
        return  f" {self.clock = }|{self.name =}"\
                f"|input_buffer = {self.read_buffer(self.input_buffer)}|output_buffer = {self.read_buffer(self.output_buffer)}"\
                f"|send_message_list = {self.message_list_content(self.send_message_list)}"\
                f"|receive_message_list = {self.message_list_content(self.receive_message_list)}"

    def read_buffer(self, buffer):
        if buffer == None:
            return (None, None)
        else:
            return (buffer.content, buffer.acknowledge_level)

    def print_buffers(self):
        print("agent {} input: {} output: {}".format(
            self.name, self.read_buffer(self.input_buffer), self.read_buffer(self.output_buffer)))

    def print_messages(self):
        send_messages = self.message_list_content(self.send_message_list)
        receive_messages = self.message_list_content(self.receive_message_list)
        print(f"Agent {self.name} at time {self.clock} has messages \n{send_messages = }\n{receive_messages = }")

    def message_list_content(self, message_list):
        return [message.read() for message in message_list]

