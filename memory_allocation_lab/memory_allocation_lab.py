from memory_allocator import MemoryAllocator
import util


def operate(line, memory):
    operation = line[0]
    if operation == "a":
        size = int(line[1])
        block = int(line[2])
        memory.myalloc(block, size)
    elif operation == "r":
        size = int(line[1])
        prev_block = int(line[2])
        new_block = int(line[3])
        memory.myrealloc(prev_block, new_block, size)
    elif operation == "f":
        block = int(line[1])
        memory.myfree(block)


inp = util.read_input("input.txt")
mem = MemoryAllocator("ff")
for i in range(len(inp)):
    operate(inp[i], mem)
# mem.heap.print_list()
