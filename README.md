# CPU Simulator
 
## Computer Architecture project to simulate a CPU, including memory and cache 

1. What does the program do?

This program simulates a CPU with a MIPS (Microprocessor without Interlocked Pipelined Stages) instruction set architecture (ISA). The instructions for the CPU and memory can be fed to the simulator through a text file

2. What data do you need?

Program needs CPU instructions as well as data input to initialize memory bus. These instructions can be inputed as a .txt file.

3. What aspects of a CPU can you simulate using Python?

The program can simulate a variety of MIPS instructions including ADD, ADDI, SUB, SLT, CACHE, J and HALT

## Usage

```python
python main.py
```

You will be then prompted to enter CPU instructions input file name as well as the data input file name. For this example, we'll use the sample files provided in the project (instruction_input.txt and data_input.txt)

```
Please enter the name of the CPU instructions input file name (including file extension): instruction_input.txt 
Please enter the name of the data input file name (including file extension): data_input.txt
```

The program will then intitalize the memory bus using the data input file by writing the value provided in the binary location provided. Shown below is the memory bus using the provided sample data input file data_input.txt

```
Initializing memory bus from data_input.txt...
Memory bus initialized successfully
Memory Bus: {'00000000': 0, '00000001': '4', '00000010': '5', '00000011': '6', '00000100': '7', '00000101': '2', '00000110': '3', '00000111': '9', '00001000': 0, '00001001': 0, '00001010': 0, '00001011': 0, '00001100': 0, '00001101': 0, '00001110': 0, '00001111': 0, '00010000': 0, '00010001': 0, '00010010': 0, '00010011': 0, '00010100': 0, '00010101': 0, '00010110': 0, '00010111': 0, '00011000': 0, '00011001': 0, '00011010': 0, '00011011': 0, '00011100': 0, '00011101': 0, '00011110': 0, '00011111': 0, '00100000': 0, '00100001': 0, '00100010': 0, '00100011': 0, '00100100': 0, '00100101': 0, '00100110': 0, '00100111': 0, '00101000': 0, '00101001': 0, '00101010': 0, '00101011': 0, '00101100': 0, '00101101': 0, '00101110': 0, '00101111': 0, '00110000': 0, '00110001': 0, '00110010': 0, '00110011': 0, '00110100': 0, '00110101': 0, '00110110': 0, '00110111': 0, '00111000': 0, '00111001': 0, '00111010': 0, '00111011': 0, '00111100': 0, '00111101': 0, '00111110': 0, '00111111': 0}
```

After the memory bus is intialized, the CPU instructions are read and executed on the register values. Each individual instruction will be outputed to the console as well. Shown below is the console output for the CPU instruction using the provided sample data input file instruction_input.txt. 

```
Reading CPU instructions from instruction_input.txt...
Reading instructions: CACHE,1
Reading instructions: ADDI,R2,R2,2
Reading instructions: ADD,R3,R2,R1
Reading instructions: J,8
Reading instructions: HALT,;
CPU instructions read successfully
Cache: deque([',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ',', ','], maxlen=32)
Registers: [0, 0, 2, 2, 0, 0, 0, 0]
Number of instructions processed: 9
```

After the instructions are executed, the Cache, Register and Number of instructions processed are displayed. More details on MIPS instructions can be found [here](https://www.dsi.unive.it/~gasparetto/materials/MIPS_Instruction_Set.pdf).

## Current Limitations and Future Improvements 
- Cache is initilaized when cache_flag is set to True but data is not transfered between registers, cache and memory. In order for cache to be correctly implemented, associativity would need to be set up to associate the cache with memory and registers.
- The Jump instruction only increments the CPU counter and does not jump to the specific instruction.
- Error handling for incorrect file names.
- Only the following MIPS instructions are supported: CACHE, ADD, ADDI, J, SLT, HALT. 