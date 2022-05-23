from memory import Memory
from cache import Cache

NUMBER_OF_REGISTERS = 8

# CPU class to implement data processing using MIPS instructions. The following variables are instantiated:
#    CPU Counter - int representing the number of the instruction being parsed
#    Registers - list to represent internal registers used by the CPU
#    Cache Flag - boolean representing whether or not the cache is to be used
#    Cache - instance of Cache object instantiated for CPU
#    Memory Bus - instance of Memory Bus object instantiated for CPU
class CPU:
    def __init__(self):
        self.cpu_counter = 0
        self.registers = [0] * NUMBER_OF_REGISTERS
        self.cache_flag = False
        self.cache = Cache()
        self.memory_bus = Memory()

    def increment_cpu_counter(self):
        self.cpu_counter += 1

    def reset_cpu_counter(self):
        self.cpu_counter = 0

    def set_cache_flag(self, value):
        self.cache_flag = value

    def clear_cache(self):
        self.cache.flush_cache()

    def write_memory_bus(self, address, value):
        self.memory_bus.write_memory_bus(address, value)
    
    # Helper methods for implementation of a few MIPS instructions (CACHE, ADD, ADDI, SUB, SLT, J)
    # Method to implement CACHE instruction - Value = 0 (Cache off), Value = 1 (Cache on), Value = 2 (Flush cache)
    def cache_instruction(self, value):
        if int(value) == 0:
            self.set_cache_flag(False)
        elif int(value) == 1:
            self.set_cache_flag(True)
        elif int(value) == 2:
            self.clear_cache(self)
    
    # Method to implement ADD instruction (Rd <- Rs + Rt)
    def add_instruction(self, destination, source, target):
        # Convert register string to index i.e. register R2 would correspond to int index 2
        destination = int(destination[1:])
        source = int(source[1:])
        target = int(target[1:])
        self.registers[destination] = self.registers[source] + self.registers[target]

    # Method to implement ADDI instruction (Rt <- Rs + immd)
    def add_i_instruction(self, destination, source, immediate):
        # convert register string to index i.e. register R2 would correspond to int index 2
        destination = int(destination[1:])
        source = int(source[1:])
        self.registers[destination] = self.registers[source] + int(immediate)

    # Method to implement SUB instruction (Rd <- Rs - Rt)
    def sub_instruction(self, destination, source, target):
        # Convert register string to index i.e. register R2 would correspond to int index 2
        destination = int(destination[1:])
        source = int(source[1:])
        target = int(target[1:])
        self.registers[destination] = self.registers[source] - self.registers[target]
    
    # Method to implement SLT instruction (If (Rs < Rt) then Rd <- 1 else Rd <- 0)
    def slt_instruction(self, destination, source, target):
        destination = int(destination[1:])
        source = int(source[1:])
        target = int(target[1:])
        if self.registers[source] < self.registers[target]:
            self.registers[destination] = 1
        else:
            self.registers[destination] = 0

    # Method to implement J instruction (PC <- target * 4)
    def jump_instruction(self, value):
        self.cpu_counter = int(value)

    # Main parser method used to interpret MIPS instructions from input file.
    # Check value of operator and call appropriate helper method 
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
        elif instruction_parsed[0] == "SUB":
            self.sub_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        elif instruction_parsed[0] == "SLT":
            self.slt_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        elif instruction_parsed[0] == "J":
            self.jump_instruction(instruction_parsed[1])