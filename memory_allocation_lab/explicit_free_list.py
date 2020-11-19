class ExplicitFreeList:
    def __init__(self, size, algorithm, node):
        self.size = size
        self.algorithm = algorithm
        self.free_head = node
        self.num_free_nodes = 1
        self.allocated_head = None
        self.num_allocated_nodes = 0

    def print_self(self):
        print("Explicit free list:\n\talgorithm: " + str(self.algorithm) + ",\tfree:" + str(self.num_free_nodes) +
              ",\tallocated: " + str(self.num_allocated_nodes) + ",\tsize: " + str(self.size))

    def find_free_block(self, block_size):
        if self.algorithm == "first-fit":
            if self.free_head is None:
                print("error - free head is None for some reason")
                return
            elif self.free_head.next is None:
                return self.free_head
        else:
            return

    def split(self, old_free_block, payload_size, heap_size, ptr_num):
        if not old_free_block:
            print("error - split, free block doesn't exist")
            return False
        block_size = ((payload_size + 7) & -8) + 8
        if old_free_block.address + block_size > heap_size:
            print("warning - split, exceeds heap size")
            return False
        allocated_end_address = old_free_block.address + block_size - 1
        allocated_block = ExplicitNode(address=old_free_block.address,
                                       end_address=allocated_end_address,
                                       block_size=block_size,
                                       ptr_num=ptr_num)
        allocated_block.payload_address = allocated_block.address + 4
        allocated_block.payload_size = payload_size
        new_free_address = old_free_block.address + block_size
        # next address minus newly allocated
        new_free_block_size = (old_free_block.end_address + 1) - (old_free_block.address + block_size)
        new_free_block = ExplicitNode(address=new_free_address,
                                      end_address=old_free_block.end_address,
                                      block_size=new_free_block_size,
                                      ptr_num=None)
        if self.allocated_head is None:
            self.allocated_head = allocated_block
            self.num_allocated_nodes += 1
        else:
            return
        if self.free_head.next is None:
            self.free_head = new_free_block
        else:
            return
        return [allocated_block, new_free_block]

    def replace_block(self):
        return

    def join_adjacent_blocks(self):
        return

    def join_blocks(self):
        return

    def set_mem_brk(self):
        return

    def find_pointer_block(self):
        return

    def print_list(self, which):
        if which == "free":
            cur = self.free_head
            print("num_free_nodes: " + str(self.num_free_nodes))
        else:
            cur = self.allocated_head
            print("num_allocated_nodes: " + str(self.num_allocated_nodes))
        while cur is not None:
            cur.print_node()
            cur = cur.next
        print()


class ExplicitNode:
    def __init__(self, address, end_address, block_size, ptr_num):
        self.address = address
        self.block_size = block_size
        self.end_address = end_address
        self.ptr_num = ptr_num
        self.payload_address = None
        self.payload_size = None
        self.prev = None
        self.next = None

    def print_node(self):
        print("\taddress: " + str(self.address) + ",\tpayload_address: " + str(self.payload_address) +
              "\tpayload_size: " + str(self.payload_size) + ",\tend_address: " + str(self.end_address) +
              ",\tblock_size: " + str(self.block_size) + ",\tptr_num: " + str(self.ptr_num))
        #  + ",\tprev: " + str(self.prev) + ",\tnext: " + str(self.next)
