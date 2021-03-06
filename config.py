import logging
loglevel = logging.ERROR

commandline_config_chooser = True

# Configs
stepper_time_limit = 300
log_trace_filename = "log_trace_new.txt"
save_log_to_file = False
print_log_to_terminal = False
print_channel_content = False
encryption_protocol = True
include_eavesdropper = False
two_way_communication = True
interlock_protocol = True

# Channel parameters
channel_time_delay = 0

# Eavesdropper parameters
eavesdropper_listen_rate = 1 # every n ticks checks for something

# Sender/receiver paramters
message_timeout = 1
acknowledge_depth = 0 if interlock_protocol else int(two_way_communication) + 1 # 2 # Needs to be uneven for one-way communication, even for two-way communication
if acknowledge_depth % 2 == two_way_communication:
    print("Acknowledge depth needs to be uneven for one-way communication and even for two-way communication.")
if interlock_protocol and acknowledge_depth != 0:
    print("Interlock protocol does not work with acknowledges. Set acknowledge depth to 0.")
    # Does not work because you can't decrypt half the ciphertext to see if it is the correct message to acknowledge
if interlock_protocol and not two_way_communication:
    print("Interlock protocol only works with two-way communication.")
    quit()

# failure types true/false
# <Processes> Process halts and remains halted. Other processes may not be able to detect this state
# --> A process stops the stepper function (until recovery)
crash = False
crash_failure_rate = 0.01
# <Channel> A message inserted in an outgoing buffer never arrives at the other ends incomming buffer.
# --> message lost in transfer from and to chute in channel
omission = False
omission_failure_rate = 0.1 # 1 is every time, 0 is never
# <Process> A process completes a send, but the message is not put in the channels input buffer.
# --> message lost in sender write function
send_omission = False
send_omission_failure_rate = 0.1
# <Process> A message is put in the channel's outgoing message buffer, but does not arrive in the processes incomming buffer.
# --> message lost in receiver read function
receive_omission = False
receive_omission_failure_rate = 0.1

