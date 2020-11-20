from memory_allocator import MemoryAllocator
import util


def operate(line, memory):
    operation = line[0]
    if operation == "a":
        if len(line) > 3:
            print("Error: too many parameters.")
            return
        try:
            block_size = int(line[1])
            op_num = int(line[2])
        except ValueError:
            print("Error: invalid parameter.")
            return
        except TypeError:
            print("Error: parameter type mismatch.")
            return
        memory.myalloc(block_size, op_num)
    elif operation == "r":
        if len(line) > 4:
            print("Error: too many parameters.")
            return
        try:
            size = int(line[1])
            prev_block = int(line[2])
            new_block = int(line[3])
        except ValueError:
            print("Error: invalid parameter.")
            return
        except TypeError:
            print("Error: parameter type mismatch.")
            return
        memory.myrealloc(prev_block, new_block, size)
    elif operation == "f":
        if len(line) > 2:
            print("Error: too many parameters.")
            return
        try:
            ptr_num = int(line[1])
        except ValueError:
            print("Error: invalid parameter.")
            return
        except TypeError:
            print("Error: parameter type mismatch.")
            return
        memory.myfree(ptr_num)
    else:
        print("Error: operation not recognized")


args = util.parse_args()
inp = util.read_input(args.file)
mem = MemoryAllocator(policy={"heap_type": args.heap_type, "algorithm": args.algorithm})
for i in range(len(inp)):
    operate(inp[i], mem)
mem.print_to_file("output.txt")
