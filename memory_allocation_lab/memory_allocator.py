from implicit_free_list import ImplicitFreeList
from implicit_free_list import ImplicitNode
from explicit_free_list import ExplicitFreeList
from explicit_free_list import ExplicitNode


def encode_header(node):
    if not node:
        print("error - node doesn't exist")
    return node.block_size + node.allocated


class MemoryAllocator:
    def __init__(self, policy):
        self.heap_type = policy["heap_type"]
        self.algorithm = policy["algorithm"]
        self.heap_size = 200
        self.max_heap_size = 400000
        self.num_words = int(self.heap_size / 4)
        self.words = [0 for i in range(self.num_words)]
        if self.heap_type == "implicit":
            node = ImplicitNode(address=4,
                                end_address=self.heap_size - 5,
                                allocated=0,
                                block_size=self.heap_size - 8,
                                ptr_num=None)
            self.write_to_mem(node)
            self.heap = ImplicitFreeList(self.heap_size, self.algorithm, node)
        else:
            node = ExplicitNode(address=4,
                                end_address=self.heap_size - 5,
                                block_size=self.heap_size - 8,
                                ptr_num=None)
            self.write_to_mem(node)
            self.heap = ExplicitFreeList(self.heap_size, self.algorithm, node)

    def print_mem(self):
        for i in range(self.num_words):
            print("0x{:08x}".format(self.words[i]))
        print()

    """
    takes an integer value indicating the number of bytes to allocate for the payload of the block
    returns a "pointer" to the starting address of the payload of the allocated block
        The "pointer" above can take any form you like, depending on the data structure you use to represent your heap
    """
    def myalloc(self, ptr_size, ptr_num):
        if self.heap_type == "implicit":
            block_size = ((ptr_size + 7) & -8) + 8
            free_block = self.heap.find_free_block(block_size)
            if free_block.block_size == block_size:
                block = self.heap.replace_block(free_block, ptr_num)
                self.write_to_mem(block)
                return
            nodes = self.heap.split(free_block, ptr_size, self.heap_size, ptr_num)
            if nodes is None:
                print("error - neither False nor [node1, node2]")
            elif not nodes:
                print("warning - extending memory")
                self.mysbrk(free_block.address, ptr_size)
                self.heap.set_mem_brk(self.heap_size)
                nodes = self.heap.split(free_block, ptr_size, self.heap_size, ptr_num)
                if not nodes:
                    print("error - not able to split after an sbrk")
            self.write_to_mem(nodes[0])
            self.write_to_mem(nodes[1])

    def write_to_mem(self, block):
        if self.heap_type == "implicit":
            self.words[int(block.address / 4)] = encode_header(block)
            self.words[int(block.end_address / 4)] = encode_header(block)
        else:
            return

    """
    takes a pointer to an allocated block and an integer value to resize the block to
    returns a "pointer" to the new block 
    frees the old block
    a call to myrealloc with a size of zero is equivalent to a call to myfree
    """
    def myrealloc(self, prev_ptr_num, new_ptr_num, size):
        if self.heap_type == "implicit":
            self.myfree(prev_ptr_num)
            self.myalloc(size, new_ptr_num)
        else:
            return

    """
    frees the block pointed to by the input parameter "pointer"
    returns nothing
    only works if "pointer" represents a previously allocated or reallocated block that has not yet been freed
        otherwise, does not change the heap
    """
    def myfree(self, ptr_num):
        if self.heap_type == "implicit":
            block = self.heap.find_pointer_block(ptr_num)
            block.allocated = 0
            block.ptr_num = None
            blocks = self.heap.join_adjacent_blocks(block)
            for i in range(len(blocks)):
                self.write_to_mem(blocks[i])
        else:
            return

    """
    grows or shrinks the size of the heap by a number of words specified by the input parameter "size"
    you may call this whenever you need to in the course of a simulation, as you need to grow the heap
    this call will return an error and halt the simulation if your heap would need to grow past the maximum size of 
    100,000 words
    """
    def mysbrk(self, address, size):
        if self.heap_type == "implicit":
            new_mem_brk = address + size + 16
            if new_mem_brk > self.max_heap_size:
                print("error - Operation not permitted: exceeds heap size.")
                return
            self.heap_size = new_mem_brk
        else:
            return
