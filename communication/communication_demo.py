from logger import setup_logger
from .agent import Agent
from .channel import Channel
from .message import Message
from .sender import Sender
from .receiver import Receiver
from .communicator import Communicator
from .eavesdropper import Eavesdropper
from .stepper import Stepper
import config
from communication import log
from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def interact_with_people():
    # Determine situation
    clear_screen()
    print("Welcome to the communication demo for eavesdropping")
    print("This program, along with the website, have been created by:")
    print("- I.E. Steegstra")
    print("- R.M. O'Loughlin")
    print("- A.   Brandsma\n")
    print("There are three possible situations to choose from:")
    print("(Press the relevant number to run the specific situation)")
    print(" 1 - Perfect Communication")
    print(" 2 - Perfect Communication With Eavesdropping")
    print(" 3 - The Interlock Protocol")
    situation = int(input("Situation: "))
    clear_screen()
    if situation != 1 and situation != 2 and situation != 3:
        print(type(situation))
        log.error(f"The situation should be either 1, 2 or 3, not {situation}")
        return (0, False, False)
    
    # Determine communication type
    communication_type = 2
    if situation == 1 or situation == 2:
        print("We can either use one-way or two-way communication for these protocols")
        print(" 1 - One-way Communication")
        print(" 2 - Two-way Communication")
        communication_type = int(input("Communication Type: "))
        clear_screen()
        if communication_type != 1 and communication_type != 2:
            log.error(f"The communication type should be either 1 or 2, not {communication_type}")
            return (0, False, False)
    
    # Determine encryption
    print("We can use encryption or communicate using plain-text")
    print(" 0 - Encryption off")
    print(" 1 - Encryption on")
    encryption_type = int(input("Encryption: "))
    clear_screen()
    if encryption_type != 1 and encryption_type != 0:
        log.error(f"The encryption setting should be either 1 or 0, not {encryption_type}")
        return (0, False, False)
        
    
    return (situation, True if encryption_type == 1 else False, True if communication_type==2 else False)

def set_config(situation, encryption, is_two_way_communication):
    if situation == 1:
        config.encryption_protocol = encryption
        config.include_eavesdropper = False
        config.two_way_communication = is_two_way_communication
        config.interlock_protocol = False

        return True
    elif situation == 2:
        config.encryption_protocol = encryption
        config.include_eavesdropper = True
        config.two_way_communication = is_two_way_communication
        config.interlock_protocol = False
        
        return True
    elif situation == 3:
        config.encryption_protocol = encryption
        config.include_eavesdropper = False
        config.two_way_communication = is_two_way_communication
        config.interlock_protocol = True
        
        return True
    else:
        log.error(f"No situation has been found for {situation}")
        return False

def communication_demo():
    if config.commandline_config_chooser:
        situation, encryption, is_two_way_communication = interact_with_people()
        if situation == 0:
            return
    
        if not set_config(situation, encryption, is_two_way_communication):
            return

    # Required entities
    if config.two_way_communication:
        alice = Communicator("Alice", True)
        bob = Communicator("Bob", False)
    else:
        alice = Sender("Alice")
        bob = Receiver("Bob")

    agents = [alice, bob]
    stepper = Stepper()

    stepper.add_all_processes([alice, bob])

    # Set up connection
    if config.include_eavesdropper:
        eve = Eavesdropper("Eve")
        agents.append(eve)
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

    if config.two_way_communication and True:
        m_d, m_e, m_f = Message("Do you even know?"), Message("Everything is nothing."), Message("Freedom forlorn.")
        messages_b = [m_d, m_e, m_f]
        bob.import_messages(messages_b)

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
