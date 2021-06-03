# Configs

# failure types true/false

# stepper order random/ordered

# agent paramters
message_timeout = 4
acknowledge_depth = 3 # Needs to be uneven
if acknowledge_depth % 2 == 0:
    log.error("READ THE COMMENTS, ACKNOWLEDGE DEPTH NEEDS TO BE UNEVEN!")