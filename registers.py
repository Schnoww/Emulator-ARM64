#using class because it makes it easier
from stack import Stack

stack = Stack()

class ARM64Processor:
    def __init__(self):
        #64-bit registers 

        #x0 to x30
        self.registers = {f'x{i}': 0x0000000000000000 for i in range(31)} 
        ##SP
        self.registers['sp'] = 0x0000000000000000 
        #PC
        self.registers['pc'] = 0x0000000000000000 
        #zero register
        self.registers['xzr'] = 0x0000000000000000  

        #processor states (negative and zero)
        self.processor_state = {
            'N': 0,  
            'Z': 0   
        }
        # stack.printStack()

    def print_registers(self):

        # print stack
        stack.printStack()

        #print registers
        print("-"*100)
        print("Registers:")
        print("-"*100)
        
        #formating, 3 registers per line
        for i in range(0, 31, 3): 
            line = " ".join(f"{key}: 0x{value:016X}  \t" for key, value in list(self.registers.items())[i:i+3])
            print(line)
        
        #printing
        # print(f"SP: 0x{self.registers['sp']:016X}  \t pc: 0x{self.registers['pc']:016X}")
        print(f"\nProcessor State N bit: {self.processor_state['N']}")
        print(f"Processor State Z bit: {self.processor_state['Z']}")
        # print("-------------------------------------------")
