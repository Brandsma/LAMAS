from .event import Event

class Process:
    
    def __init__(self):
        self.clock = 0          # Logical system clock for event ordering, Lamport's time algorithm 
        self.step_counter = 0   # internal step counter, used for action rates. 
        self.event_log = []

    def tick(self):
        self.clock += 1

    def set_clock(self, time):
        if time >= self.clock:
            self.clock = time

    def step(self, physical_time):
        # interface function 
        pass

    def log_event(self, event):
        self.event_log.append(event)

    def state(self):
        # interface
        pass

    def setup(self):
        # interface
        pass