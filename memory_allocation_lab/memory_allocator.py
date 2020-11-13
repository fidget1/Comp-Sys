from linked_list import LinkedList
from linked_list import Node


class MemoryAllocator:
    def __init__(self, policy):
        self.policy = policy
        self.heap_size = 1000
        self.heap = LinkedList()

    """
    takes an integer value indicating the number of bytes to allocate for the payload of the block
    returns a "pointer" to the starting address of the payload of the allocated block
        The "pointer" above can take any form you like, depending on the data structure you use to represent your heap
    """
    def myalloc(self, block_size, op_num):
        free_block = self.heap.find_free_block(block_size, op_num)
        free_block.print()

    """
    takes a pointer to an allocated block and an integer value to resize the block to
    returns a "pointer" to the new block 
    frees the old block
    a call to myrealloc with a size of zero is equivalent to a call to myfree
    """
    def myrealloc(self, prev_block, new_block, size):
        return

    """
    frees the block pointed to by the input parameter "pointer"
    returns nothing
    only works if "pointer" represents a previously allocated or reallocated block that has not yet been freed
        otherwise, does not change the heap
    """
    def myfree(self, block):
        self.heap.print()

    """
    grows or shrinks the size of the heap by a number of words specified by the input parameter "size"
    you may call this whenever you need to in the course of a simulation, as you need to grow the heap
    this call will return an error and halt the simulation if your heap would need to grow past the maximum size of 
    100,000 words
    """
    def mysbrk(self, size):
        if self.heap_size + size > 100000:
            print("Exceeded heap size.")
            return -1
