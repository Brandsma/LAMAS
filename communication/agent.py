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
        if self.output_buffer != None:
            if config.encryption_protocol and type(self.output_buffer.get_content()) != type(self.public_key):
                self.send_message(self.encrypt_message(self.output_buffer))
            else :
                self.send_message(self.output_buffer)
        else :
            log.info("Output buffer empty, no new message passed to channel.")

    def receive(self):
        message = self.receive_message()
        if message != None:
            self.set_clock(message.clock)
            self.tick()
            if self.input_buffer != None:
                log.warning("Input buffer full, buffer overwritten.")
            if config.encryption_protocol and type(message.get_content()) != type(self.public_key):
                self.input_buffer = self.decrypt_message(message)
            else :
                self.input_buffer = message
                
    def send_message(self, message):
        self.tick()
        self.outgoing_connection.write(message.event(self.clock))

    def receive_message(self):
        return self.incomming_connection.read()

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
        split_1, split_2 = content[0:len(content)//2], content[len(content)//2:len(content)] # Split message in half
        message_2 = message.copy()
        message.set_content(split_1)
        message_2.set_content(split_2)
        return message, message_2

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
        return " clock: {}|{}|{}|{}|{}|{}".format( 
            self.clock, self.name,
            self.read_buffer(self.input_buffer), self.read_buffer(
            self.output_buffer),
            self.message_list_content(self.send_message_list),
            self.message_list_content(self.receive_message_list)
            )

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

