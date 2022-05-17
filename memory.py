MEMORY_BUS_SIZE = 128

# This class implements a memory bus
class Memory:
    def __init__(self):
        self.memory_bus = {}
        self.initialize_memory_bus()

    # Method to initialize memory bus with size based on MEMORY_BUS_SIZE variable
    # Memory bus is setup as a dict with binary address being key, and value being value 
    def initialize_memory_bus(self):
        for i in range(MEMORY_BUS_SIZE):
            self.memory_bus[f'{i:08b}'] = 0
    
    # Method to search for address in memory bus and return value if available 
    def search_memory_bus(self, address):
        if self.memory_bus.get(address) != None:
            return self.memory_bus.get(address)
        return None 
    
    # Method to write in memory bus only if address is within the bus size 
    def write_memory_bus(self, address, value):
        if self.memory_bus.get(address) != None:
            self.memory_bus[address] = value
