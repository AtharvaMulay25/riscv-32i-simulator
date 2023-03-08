import decode
import single_cycle
instruction_memory = {}
pc = "0x0"
next_pc = "0x0"


def fetch():
    inst = instruction_memory[pc]
    decode.instruction = inst
    if(inst=='$'):
        single_cycle.end=1
    next_pc = str(hex(int(pc, 16) + 0x4))
    decode.pc = pc
    decode.next_pc = next_pc

