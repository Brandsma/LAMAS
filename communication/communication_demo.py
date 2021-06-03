from logger import setup_logger
from .agent import Agent
from .channel import Channel
from .message import Message
from .sender import Sender
from .receiver import Receiver
from .eavesdropper import Eavesdropper
from .stepper import Stepper

log = setup_logger(__name__)


def communication_demo():
    log.info("Communication demo")
    
    # Required entities
    alice = Sender("Alice")
    bob = Receiver("Bob")
    eve = Eavesdropper("Eve")
    agents = [alice, bob, eve]
    fc = Channel("forward") # forward-channel
    bc = Channel("backward") # backward-channel

    stepper = Stepper()
    stepper.add_all_processes([alice, eve, bob, fc, bc])

    # Set up connection
    alice.connect(fc)
    bob.connect(fc)
    eve.connect(fc)
    alice.connect_back(bc)
    bob.connect_back(bc)
    eve.connect_back(bc)

    # Create dummy messages
    m_a, m_b, m_c = Message("A"), Message("B"), Message("C")
    messages = [m_a, m_b, m_c]

    m = Message("hallo")
    m_a = m.acknowledge()
    if m.acknowledge() == m_a:
        print("THIS SHOULD WORK")

    # Add to sender
    alice.import_messages(messages)

    # Message passing
    print_all(agents)
    stepper.start(100)
    #     # alice sends message to the channel
    # alice.send() # generic function, sends last message from the list. 
    #     # message is now in the input buffer
    # fc.send() # move message from input_buffer to chute
    #     # input buffer is now free for a new message, message in the chute
    # eve.listen() # eavesdropper receives a* message from the chute
    # fc.receive() # move message from chute to output_buffer
    #     # message is now in the output buffer, ready to be read by bob, and no longer 
    # bob.receive()
    print_all(agents)
    for item in stepper.state_log:
        print(item)
    log_to_file(stepper.state_log)


def log_to_file(state_log):
    f = open("log_trace.txt", "w")
    for state in state_log:
        f.write(state + "\n")
    f.close()

def print_all(agents):
    for agent in agents:
        agent.print_messages()