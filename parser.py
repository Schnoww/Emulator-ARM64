# #importing re because we will be using it for pattern and matches
# #it is known as RegEX
# import re
# from registers import ARM64Processor 

# processor = ARM64Processor()


# #parse function for ADD instructions
# def parseADD(operandsSTR):
#     return operandsSTR.split(',')

# #parse function for LDR instructions
# def parseLDR(operandsSTR):
#     #using RegEX for the pattern and matching
#     #pattern
#     pattern = r'(\w+), \[(\w+), (.+)\]'
#     #match, using RegEX
#     match = re.match(pattern, operandsSTR)
#     if match:
#         return [match.group(1), f"[{match.group(2)}, {match.group(3)}]"]
#     return operandsSTR.split(',')

# # Function for mnemonic
# def parseINSTR(line):
#     #split method for each instruction
#     instruction, operandsSTR = line.split('\t', 1)

#     # processor = ARM64Processor()
#     # processor.print_registers()

#     #all instructions for now and can add more later
#     if instruction == "ADD":
#         operands = parseADD(operandsSTR)
#         # processor.registers['PC'] += 0x4 
#     elif instruction == "LDR":
#         operands = parseLDR(operandsSTR)  # Corrected assignment operator
#         # processor.registers['PC'] += 0x4
#     else:
#         operands = operandsSTR.split(',')
#         # processor.registers['PC'] += 0x4

#     processor.print_registers()

#     #return the split
#     return address, instruction, operands


