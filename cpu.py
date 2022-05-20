from memory import Memory
from cache import Cache

NUMBER_OF_REGISTERS = 8

# This class implements a cpu
class CPU:
    def __init__(self):
        self.cpu_counter = 0
        self.registers = [0] * NUMBER_OF_REGISTERS
        self.cache_flag = False
        self.cache = Cache()
        self.memory = Memory()

    def increment_cpu_counter(self):
        self.cpu_counter += 1

    def reset_cpu_counter(self):
        self.cpu_counter = 0

    def set_cache_flag(self, value):
        self.cache_flag = value

    def clear_cache(self):
        self.cache.flush_cache()

    def write_memory_bus(self, address, value):
        self.memory.write_memory_bus(address, value)

    def cache_instruction(self, value):
        if int(value) == 0:
            self.set_cache_flag(False)
        elif int(value) == 1:
            self.set_cache_flag(True)
        elif int(value) == 2:
            self.clear_cache(self)

    def add_instruction(self, destination, source, target):
        # convert register string to index i.e. register R2 would correspond to int index 2
        destination = int(destination[1:])
        source = int(source[1:])
        target = int(target[1:])
        self.registers[destination] = self.registers[source] + self.registers[target]

    def add_i_instruction(self, destination, source, immediate):
        # convert register string to index i.e. register R2 would correspond to int index 2
        destination = int(destination[1:])
        source = int(source[1:])
        self.registers[destination] = self.registers[source] + int(immediate)

    def jump_instruction(self, value):
        self.cpu_counter = int(value)

    def parse_cpu_instruction(self, instruction):
        self.increment_cpu_counter()
        instruction_parsed = instruction.split(",")
        print(f"Reading instructions: {instruction}")
        if instruction_parsed[0] == "CACHE":
            self.cache_instruction(instruction_parsed[1])
        elif instruction_parsed[0] == "ADD":
            self.add_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        elif instruction_parsed[0] == "ADDI":
            self.add_i_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        elif instruction_parsed[0] == "J":
            self.jump_instruction(instruction_parsed[1])
