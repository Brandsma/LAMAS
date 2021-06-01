

class Event:

    def __init__(self, event_type, logical_time, physical_time, process_1, process_2 = None):
        self.event_type = event_type
        self.l_time = logical_time
        self.p_time = physical_time
        self.p_1 = process_1
        self.p_2 = process_2