#imports
# from parser import parseINSTR
from registers import ARM64Processor
from job import *

#main
def main():
    #file we are using
    # filePath = "ARM_assembly.txt"
    filePath = "test1.txt"

    #open and read the file
    try:
        with open(filePath, 'r') as file:
            # stack.fill()
            #read file line by line
            parser = Parser(filePath)
            instructions = parser.parseFile()
            parser.printInst(instructions)
    #edge cases
    except FileNotFoundError:
        print(f"Error: The file '{filePath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


    # parser = Parser(filePath)
    # instructions = parser.parseFile()
    # parser.printInst(instructions)
    
    # print("\nInstruction Handling Results:") 
    # for instr in instructions:
    #     result = parseInst(instr)
        
        # print(f"{instr['inst']} {', '.join(instr['opp'])} -> {result}")

        # print(f"Line {line_num}: {line}")
        # print(f"-----------------------------------------------------")
        # print(f"Instruction #{line_num}:")
        # print(f"-------------------------------------------------------")
        # print(f"Instruction: {instruction}\tAddress: {address}")

        # for idx, operand in enumerate(operands, 1):
        #     print(f"Operand #{idx}: {operand}")
        # print()




    # #open and read the file
    # try:
    #     with open(filePath, 'r') as file:
    #         #read file line by line
    #         for line_num, line in enumerate(file, 1):
    #             line = line.strip('\t')
    #             #analyze each line
    #             if line:
    #                 #call function to parse each line
    #                 address, instruction, operands = parseINSTR(line)
                
    #                 print(f"Line {line_num}: {line}")
    #                 print(f"-----------------------------------------------------")
    #                 print(f"Instruction #{line_num}:")
    #                 print(f"-------------------------------------------------------")
    #                 print(f"Instruction: {instruction}\tAddress: {address}")

    #                 for idx, operand in enumerate(operands, 1):
    #                     print(f"Operand #{idx}: {operand}")
    #                 print()
    # except FileNotFoundError:
    #     print(f"Error: The file '{filePath}' was not found.")
    # except Exception as e:
    #     print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
