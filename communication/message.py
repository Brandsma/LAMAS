from communication.process import Process

class Message(Process): # Is a message really a process? I don't know, but its usefull 
                        # for the message to have time. Possibly make it something else

    def __init__(self, content, clock = 0, acknowledge_level = 0):
        super().__init__()
        self.content = content
        self.clock = clock
        self.acknowledge_level = acknowledge_level

    def __eq__(self, other):  
        if isinstance(other, self.__class__):
            return self.content == other.content and self.acknowledge_level == other.acknowledge_level
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def read(self) -> str:
        return self.content

    def event(self, time): #experimental function. might be really stupid or really smart
        # instead of passing the object, pass this object by invoking this function, which increments the time
        self.set_clock(time)
        return self

    def acknowledge(self):
        # An acknowledge is a copy of the object with the acknowledge level increased by one
        # pretty elegant if you ask me
        return Message(self.content, self.clock, self.acknowledge_level + 1)

    def set_clock(self, time):
        if time >= self.clock:
            self.clock = time