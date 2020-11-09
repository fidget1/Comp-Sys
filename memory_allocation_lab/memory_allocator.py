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
    def myalloc(self, block, size):
        new_node = Node()
        new_node.block_size = size
        new_node.block_id = block
        self.heap.append(new_node)

        return new_node

    """
    takes a pointer to an allocated block and an integer value to resize the block to
    returns a "pointer" to the new block 
    frees the old block
    a call to myrealloc with a size of zero is equivalent to a call to myfree
    """
    def myrealloc(self, prev_block, new_block, size):
        self.myfree(prev_block)
        new_node = self.myalloc(new_block, size)

        return new_node

    """
    frees the block pointed to by the input parameter "pointer"
    returns nothing
    only works if "pointer" represents a previously allocated or reallocated block that has not yet been freed
        otherwise, does not change the heap
    """
    def myfree(self, block):
        print("my free")
        cur = self.heap.head
        print("block: " + str(block))
        i = 0
        while i <= block:
            print("i: " + str(i))
            if i < block:
                print("for loop: " + str(cur.block_size))
                cur = cur.next
                i += 1
            else:
                print("block found: block_size - " + str(cur.block_size) + " | block_id - " + str(cur.block_id))
                i += 1
        print("exited for loop: " + str(block))

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

        return self.policy


class LinkedList:
    def __init__(self):
        self.head = None
        self.num_nodes = 0

    def append(self, node):
        if self.head is None:
            self.head = node
            self.num_nodes += 1
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            self.num_nodes += 1

    def print_list(self):
        cur = self.head
        print("num_nodes: " + str(self.num_nodes))
        for i in range(0, self.num_nodes):
            print(cur.data)
            cur = cur.next


class Node:
    def __init__(self):
        self.block_size = None
        self.block_id = None
        self.next = None
