
# ARM64-Emulator

This project is a simple ARM64 emulator that allows you to simulate and inspect the execution of basic ARM64 assembly instructions. I created it for my Reverse Engineering course, as we had to build our own emulators to run our ARM assembly code. Python was chosen since it was the simplest option for this task. The emulator displays the processor state—including registers, program counter, and flags—and simulates a stack in memory to support `str` and `ldr` operations.

## Features

- **Instruction Simulation:** Emulates basic ARM64 instructions.
- **Processor State Display:** Shows registers, program counter, and flags.
- **Stack Simulation:** Supports `str` (store) and `ldr` (load) operations through a simulated memory stack.
- **Easy Customization:** Edit `main.py` to import or include your ARM64 assembly code.

## Getting Started

### Clone the Repository

Clone this repository using:

```bash
https://github.com/Schnoww/Emulator-ARM64.git
```

Edit the ARM64 Assembly Code

Open the main.py file and modify it to include the ARM64 assembly code you want to simulate.
Run the Emulator

Execute the emulator with:

```bash
python main.py
```


Execue the emulator with:
```bash
python main.py
```




