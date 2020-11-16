class ImplicitFreeList:
    def __init__(self, size, algorithm):
        self.head = ImplicitNode(address=0x4, end_address=3999, free=1, block_size=size, ptr_num=None)
        self.algorithm = algorithm
        self.num_nodes = 1
        self.size = size

    def print_self(self):
        print("Implicit free list:\n\talgorithm: " + str(self.algorithm) + ",\tfree:" + str(self.num_nodes) +
              ",\tsize: " + str(self.size))

    def find_free_block(self, block_size):
        if self.head is None:
            print("error")
        if self.head.next is None and self.head.free == 1 and block_size <= self.head.block_size:
            return self.head
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
                if cur.free == 1:
                    return cur
            print("error")

        return

    def split(self, free_block, payload_size, heap_size, ptr_num):
        if free_block.free == 0:
            print("error")
            return
        print(payload_size)
        block_size = ((payload_size + 7) & -8) + 8
        print(block_size)
        if free_block.address + block_size > heap_size:
            print("error")
            return
        allocated_end_address = free_block.address + block_size - 1
        print("allocated_end_address: ", str(allocated_end_address))
        free_block_end_address = free_block.end_address
        allocated_block = ImplicitNode(address=free_block.address, end_address=allocated_end_address, free=0,
                                       block_size=block_size, ptr_num=ptr_num)
        new_free_block = ImplicitNode(address=free_block.address + block_size, end_address=free_block_end_address,
                                      free=1, block_size=free_block.block_size - block_size, ptr_num=None)
        if self.head.next is None:
            self.head = allocated_block
            self.head.next = new_free_block
            self.head.next.prev = self.head
            self.num_nodes += 1
        else:
            cur = self.head
            while cur is not None:
                cur = cur.next
                if cur is not None and cur.address == allocated_block.address:
                    cur.prev.next = allocated_block
                    allocated_block.prev = cur.prev
                    allocated_block.next = new_free_block
                    new_free_block.prev = allocated_block
                    self.num_nodes += 1

    def find_pointer_block(self, ptr_num):
        print("ptr_num: ", str(ptr_num))
        cur = self.head
        while cur is not None:
            if cur.ptr_num == ptr_num:
                print("returning cur")
                cur.print_node()
                return cur
            cur = cur.next
        return

    def print_list(self):
        cur = self.head
        print("num_nodes: " + str(self.num_nodes))
        while cur is not None:
            cur.print_node()
            cur = cur.next


class ImplicitNode:
    def __init__(self, address, end_address, free, block_size, ptr_num):
        self.address = address
        self.block_size = block_size
        self.payload_size = None
        self.end_address = end_address
        self.free = free
        self.ptr_num = ptr_num
        self.prev = None
        self.next = None

    def print_node(self):
        print("\taddress: " + str(self.address) + ",\tend_address: " + str(self.end_address) +
              ",\tblock_size: " + str(self.block_size) + ",\tfree: " + str(self.free) +
              ",\tptr_num: " + str(self.ptr_num) + ",\tnext: " + str(self.next))
