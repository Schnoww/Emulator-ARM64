#importing re because we will be using it for pattern and matches
#it is known as RegEX
import re
from registers import * #ARM64Processor

processor = ARM64Processor()
reg = processor.registers # register rename

class Parser: # this class holds the instructions + parses the instructions
    def __init__(self, filename):
        self.filename = filename

    def parseLine(self, line):
        # regex 4 address, opcode, inst, and operands
        match = re.match(r"^\s*([0-9a-f]+):\t+([0-9a-f]+)\s+(\w+(?:\.le)?)\s*(.*)", line)
        if not match:
            return None
        
        # save the groups
        addr = match.group(1)
        opcode = match.group(2)
        inst = match.group(3)
        opp = match.group(4).split(',') if match.group(4) else []
        
        opp = [operand.strip() for operand in opp] # clear whitespace
        
        return {
            'addr': addr,
            'opcode': opcode,
            'inst': inst,
            'opp': opp,
            'address': 0x0
        }

    def parseFile(self): # parse file function
        instructions = [] # all instructions(addr, opcode, inst, opp) saved into list
        
        with open(self.filename, 'r') as file:
            for line in file:
                parsedLine = self.parseLine(line)
                if parsedLine:
                    instructions.append(parsedLine)
        
        return instructions

    def printInst(self, instructions): # print instructions
        lineNum = 1
        for instr in instructions:
            inst = instr['inst']
            opp = instr['opp']
            instr['address'] += 0x4

            # print each line w/ the required formatting
            print('-'*100)
            print(f"Instruction #{lineNum}")
            print('-'*100)
            print(f"Instruction: {inst}")

            for idx, operand in enumerate(opp, 1):
                print(f"Operand #{idx}: {operand}")
            print()

            self.execInst(inst, opp) # execute instructions

            lineNum += 1
            processor.print_registers() # print registers/stack

    def execInst(self, instruction, operands):
        #this is for the ret instruction so that way when its false it will terminate
        self.running = True

        instructionSet = {
            "sub": self.sub,
            "eor": self.eor,
            "add": self.add,
            "AND": self.AND,
            "mul": self.mul,
            "mov": self.mov,
            "str": self.str,
            "strb": self.strb,
            "ldr": self.ldr,
            "ldrb": self.ldrb,
            "nop": self.nop,
            "b": self.b,
            "b.gt": self.bgt,
            "b.le": self.ble,
            "cmp": self.cmp,
            "ret": self.ret,
        }
        if instruction in instructionSet:
            instructionSet[instruction](operands)
            
    #this is for 32 bits
    # def read_register_32(reg_name):
    #     return processor.registers[reg_name] & 0xFFFFFFFF

    # def write_register_32(reg_name, value):
    #     processor.registers[reg_name] = value & 0xFFFFFFFF
    
#code for the instructions
    def mov(self, opp): #move inst
        # print("Move")
        dest = opp[0]
        match = re.search(r'#(0x[0-9a-fA-F]+)', opp[1])
        x1 = int(match.group(1), 16)
        
        print(x1)
        reg[dest] = x1
        return
        reg['pc'] += 0x4

    def sub(self, opp): # subtraction function
        dest = opp[0]
        x1 = opp[1]
        x2 = int((opp[2].lstrip("#")), 16) if opp[2].startswith("#") else reg[opp[2]] # works 4 registers or immediate vals

        reg[dest] = x2 - reg[x1]
        reg['pc'] += 0x4

    #mateusz
    def eor(self, opp):
        dest = opp[0]
        x1 = opp[1]
        x2 = int(opp[2].lstrip("#"), 16) if opp[2].startswith("#") else reg[opp[2]]
        reg[dest] = reg[x1] ^ 2
        reg['pc'] += 0x4

    def add(self, opp): # addition function
        dest = opp[0]
        x1 = opp[1]
        x2 = int((opp[2].lstrip("#")), 16) if opp[2].startswith("#") else reg[opp[2]] # works 4 registers or immediate vals
        reg[dest] = x2 + reg[x1]
        reg['pc'] += 0x4

    def AND(self, opp): #bitwise AND op1 w/ op2 - store in op0
        dest = opp[0]
        x1 = opp[1]
        x2 = int((opp[2].lstrip("#")), 16) if opp[2].startswith("#") else reg[opp[2]] # works 4 registers or immediate vals
        reg[dest] = reg[x1] & x2
        reg['pc'] += 0x4

    def mul(self, opp): # multiplication function
        dest = opp[0]
        x1 = opp[1]
        x2 = int((opp[2].lstrip("#")), 16) if opp[2].startswith("#") else reg[opp[2]] # works 4 registers or immediate vals
        
        reg[dest] = reg[x1]*x2
        reg['pc'] += 0x4

    #mateusz working on it
    def str(self, opp):
        src = opp[0]
        base = opp[1].strip('[]')
        if len(opp) > 2:
            offset = opp[2].strip(']')
            offset = int((offset.lstrip("#")), 16) if offset.startswith("#") else reg[offset] 
            tAddress = reg[base] + offset
        else:
            tAddress = reg[base]
        stack.storeW(reg[src], tAddress - stack.baseAddr)
        reg['pc'] += 0x4

    def strb(self, opp):
        dest = opp[0]
        base = opp[1].strip('[')
        offset = opp[2].strip(']')
        # print(base, offset)

        if offset.startswith('#'):
            offset = int(offset.lstrip('#'), 16)
        else:
            offset = reg[offset] + 0x3

        # tAddress = reg[base] + offset
        tAddress = reg['sp'] + offset
        byte = reg[dest] & 0xFF

        stack.storeB(byte, tAddress - stack.baseAddr)
        reg['pc'] += 0x4

    #mateusz
    def ldr(self, opp):
        dest = opp[0]
        base = opp[1].strip("[")
        offset = opp[2].lstrip("#").strip("]")

        wSize = 4 if dest.startswith('w') else 8

        offset = int(offset, 16) if len(opp) > 2 and opp[2].startswith("#") else 0
        address = reg[base] + offset

        val = stack.readW(address - stack.baseAddr, wSize)

        if val is not None:
            reg[dest] = val
        else:
            #cool print statement for the error with the address
            print(f"Error Address: {hex(address)}")
        reg['pc'] += 0x4

    def ldrb(self, opp):
        reg['pc'] += 0x4

    #literally means no operation so executing the program counter is all it does
    def nop(self, opp):
        reg['pc'] += 0x4

    # \/\/\/\/\/\/\/ need to strip opp[1] so only hex remains \/\/\/\/\/\/\/\/
    def b(self, opp): # branch function
        match = re.search(r"(\d+)\s+<(\w+)\+0x([0-9a-fA-F]+)>", opp[0])
        x1 = match.group(3)
        x1 =  int(x1, 16)
        print(f"Branching to: {hex(x1)}")
        reg['pc'] += (0x4 * x1)

    def cmp(self, opp):
        x1 = (opp[1].lstrip("#"))
        x2 = int((opp[0].lstrip("#")), 16) if opp[0].startswith("#") else opp[0] # works 4 registers or immediate vals
        reg['pc'] += 0x4
        return x1 == x2
    
    #Mateusz
    def ret(self, opp):
        print("Emulator Terminated")
        self.running - False
        reg['pc'] += 0x4

    #Mateusz
    def ble(self, opp):
        target_address = int(opp[1], 16)
        if reg['N'] == 1 or reg['Z'] == 1:
            reg['pc'] = target_address
            print(f"Branch to {hex(target_address)}")
        else:
            reg['pc'] += (0x4 * opp[1])
    #Mateusz
    def bgt(self, opp):
        target_address = int(opp[1], 16)
        if reg['z'] == 0 and reg['N'] == reg['V']:
            reg['pc'] = target_address
            print(f"Branch to {hex(target_address)}")
        else:
            reg['pc'] += (0x4 * opp[1])
