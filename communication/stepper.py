
class Stepper:

    def __init__(self):
        self.physical_time = 0
        self.processes = []

    def add_all_processes(self, processes):
        for process in processes:
            self.add_process(process)

    def add_process(self, process):
        self.processes.append(process)

    def remove_process(self, process):
        self.processes.remove(process)

    def start(self, time_limit):
        while self.physical_time < time_limit:
            for process in self.processes:
                process.step(self.physical_time)
                self.physical_time += 1