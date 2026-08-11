class CPU:
    def __init__(self, cores):
        self.cores = cores

    def process(self):
        print(f"CPU processing with {self.cores} cores")


class RAM:
    def __init__(self, size_gb):
        self.size_gb = size_gb

    def load(self):
        print(f"RAM loading data ({self.size_gb} GB)")


class Storage:
    def __init__(self, capacity_gb):
        self.capacity_gb = capacity_gb

    def read(self):
        print(f"Storage reading from {self.capacity_gb} GB disk")


class Computer:
    def __init__(self, cores, ram_gb, storage_gb):
        self.cpu = CPU(cores)
        self.ram = RAM(ram_gb)
        self.storage = Storage(storage_gb)

    def boot(self):
        print("Booting computer...")
        self.cpu.process()
        self.ram.load()
        self.storage.read()
        print("Computer ready")


pc = Computer(8, 16, 512)
pc.boot()