

class Message:

    def __init__(self, content):
        self.content = content

    def read(self) -> str:
        return self.content