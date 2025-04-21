import random

class Stack:
    def __init__(self, size=256):
        self.size = size
        self.stack = [0x00]*size #init w/ 0x00 val
        self.baseAddr = 0x0 #base address of stack - will be saved in SP

    def printStack(self):
        print('-'*100+'\nStack:')
        print("-"*100)

        for i in range(0, self.size, 16):
            row = self.stack[i:i + 16]
            addr = f"000000{self.baseAddr + i:00x}" #create addr per row
            hex = ' '.join(f"{byte:02x}" for byte in row) #hexidecimal portion
            asci = "".join(chr(byte) if 32 <= byte <= 126 else '.' for byte in row) #ascii portion
            print(f"{addr} {hex:<47} |{asci}")

    def readW(self, address, wSize=4):
        if address<0 or address+wSize > self.size:
            raise IndexError(f"Address: {address} is out of bounds!")
        
        val=0
        for i in range(wSize):
            val |= self.stack[address+i] << (8*i)
        return val
    
    def storeB(self, val, offset):
        if 0 <= offset < self.size:
            self.stack[offset] = val & 0xFF
        else:
            print(f"ERROR: Offset {offset} is out of bounds!")

    def storeW(self, val, address):
        if address<0 or address+4 > self.size:
            raise IndexError(f"Address {address} is out of bounds!")
        
        for i in range(4):
            self.stack[address+i] = (val >> (8*i)) & 0xFF

    # random fill
    def fill(self):
        self.stack = [random.randint(0x00, 0xFF) for _ in range(self.size)]