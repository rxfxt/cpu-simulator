from cpu import CPU

# Helper functions to clean up and pass instructions from input files to CPU and memory
def initialize_memory_bus(cpu):
    # Parse the data input file and save each line into a list
    with open(data_input_file, 'r') as file:
        data = [line.strip() for line in file]
    # Write each value in the list to the correct address in the memory bus      
    for instruction in data:
        instruction_parsed = instruction.split(",")
        cpu.write_memory_bus(instruction_parsed[0], instruction_parsed[1])

def send_instructions_to_cpu(cpu):
    # Parse the cpu instructions input file and save each line into a list
    with open(instructions_input_file, 'r') as file:
        cpu_instructions = [line.strip() for line in file]
    # Send the instructions to the cpu
    for instruction in cpu_instructions:
        cpu.parse_cpu_instruction(instruction)

# Prompt user to input file name for CPU instructions and data input
instructions_input_file = input("Please enter the name of the CPU instructions input file name (including file extension): ")
data_input_file = input("Please enter the name of the data input file name (including file extension): ")

# Create CPU object
my_cpu = CPU()
print("###############################################################")
print("             Welcome to the Python CPU simulator               ")
print("---------------------------------------------------------------")
# Initialize memory bus using the data file 
print(f"Initializing memory bus from {data_input_file}...")
initialize_memory_bus(my_cpu)
print("Memory bus initialized successfully")
print(f"Memory Bus: {my_cpu.memory_bus.memory_bus}")
print("---------------------------------------------------------------")
# Pass CPU instructions list to CPU
print(f"Reading CPU instructions from {instructions_input_file}...")
send_instructions_to_cpu(my_cpu)
print("CPU instructions read successfully")
print(f"Cache: {my_cpu.cache.cache}")
print(f"Registers: {my_cpu.registers}")
print(f"Number of instructions processed: {my_cpu.cpu_counter}")
print("###############################################################")