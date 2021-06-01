from .event import Event

class Process:
    
    def __init__(self):
        self.clock = 0
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