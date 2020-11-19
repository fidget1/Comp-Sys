from memory_allocator import MemoryAllocator
import util


def operate(line, memory):
    operation = line[0]
    if operation == "a":
        block_size = int(line[1])
        op_num = int(line[2])
        memory.myalloc(block_size, op_num)
    elif operation == "r":
        size = int(line[1])
        prev_block = int(line[2])
        new_block = int(line[3])
        memory.myrealloc(prev_block, new_block, size)
    elif operation == "f":
        ptr_num = int(line[1])
        memory.myfree(ptr_num)


args = util.parse_args()
inp = util.read_input("input.txt")
mem = MemoryAllocator(policy={"heap_type": args.heap_type, "algorithm": args.algorithm})
for i in range(len(inp)):
    print(inp[i])
    operate(inp[i], mem)
    mem.print_mem()
# mem.myalloc(20, 0)
# mem.myalloc(10, 1)
# mem.myalloc(10, 2)
# mem.myalloc(10, 3)
# mem.myalloc(5, 4)
# mem.myfree(0)
# mem.myfree(2)
# mem.myfree(4)
# mem.myalloc(5, 0)
