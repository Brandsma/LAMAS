from logger import setup_logger
from .agent import Agent
from .channel import Channel
from .message import Message
from .sender import Sender
from .receiver import Receiver
from .eavesdropper import Eavesdropper
from .stepper import Stepper
import config
from communication import log

def communication_demo():
    log.info("Communication demo")

    # Required entities
    alice = Sender("Alice")
    bob = Receiver("Bob")
    eve = Eavesdropper("Eve")
    agents = [alice, bob, eve]
    stepper = Stepper()

    stepper.add_all_processes([alice, bob])

    # Set up connection
    if config.include_eavesdropper:
        # Create channels
        conn_alice_eve = Channel("Alice -> Fake Bob")
        conn_eve_alice = Channel("Fake Bob -> Alice")
        conn_bob_eve = Channel("Bob -> Fake Alice")
        conn_eve_bob = Channel("Fake Alice -> Bob")
        # Connect channels to correct ports
        alice.connect(conn_alice_eve, conn_eve_alice)
        bob.connect(conn_bob_eve, conn_eve_bob)
        eve.connect(conn_eve_alice, conn_alice_eve, conn_eve_bob, conn_bob_eve)
        # Add to the stepper
        stepper.add_all_processes([eve, conn_alice_eve, conn_eve_alice, conn_eve_bob, conn_bob_eve])
    else :        
        conn_ab = Channel("Alice -> Bob")  # forward-channel
        conn_ba = Channel("Bob -> Alice")  # backward-channel
        alice.connect(conn_ab, conn_ba)
        bob.connect(conn_ba, conn_ab)
        stepper.add_all_processes([conn_ab, conn_ba])

    #eve.connect_incomming(fc)
    #eve.connect_outgoing(bc)

    # Create dummy messages
    m_a, m_b, m_c = Message("Are my apples still okay?"), Message("Bravery is a fools honour."), Message("Can you please just not?")
    messages = [m_a, m_b, m_c]

    # Add to sender
    alice.import_messages(messages)

    # Message passing
    print_all(agents)
    stepper.start(config.stepper_time_limit)
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
    if config.print_log_to_terminal:
        for item in stepper.state_log:
            print(item)
            
    if config.save_log_to_file:
        log_to_file(stepper.state_log)


def log_to_file(state_log):
    f = open(config.log_trace_filename, "w")
    f.write("time | clock | agent | input | output | message list\n")
    for state in state_log:
        f.write(state + "\n")
    f.close()


def print_all(agents):
    for agent in agents:
        agent.print_messages()
