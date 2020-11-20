class ExplicitFreeList:
    def __init__(self, size, algorithm, node):
        self.size = size
        self.algorithm = algorithm
        self.free_head = node
        self.num_free_nodes = 1
        self.allocated_head = None
        self.num_allocated_nodes = 0

    def find_free_block(self, block_size):
        if self.algorithm == "first-fit":
            if self.free_head.block_size >= block_size:
                return self.free_head
            else:
                cur = self.free_head
                while cur.next is not None:
                    cur = cur.next
                    if cur.block_size >= block_size:
                        return cur
        else:
            if self.free_head.next is None:
                return self.free_head
            else:
                cur = self.free_head
                best_fit = None
                min_difference = 100000000
                while cur is not None:
                    if cur.block_size >= block_size:
                        cur_difference = cur.block_size - block_size
                        if cur_difference == 0:
                            return cur
                        if cur_difference < min_difference:
                            min_difference = cur_difference
                            best_fit = cur
                    cur = cur.next
                return best_fit

    def split(self, old_free_block, payload_size, heap_size, ptr_num):
        if not old_free_block:
            return False
        block_size = ((payload_size + 7) & -8) + 8
        if old_free_block.address + block_size > heap_size:
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
            cur = self.allocated_head
            while cur.next is not None:
                cur = cur.next
            cur.next = allocated_block
            allocated_block.prev = cur
            while cur.prev is not None:
                cur = cur.prev
            self.allocated_head = cur
            self.num_allocated_nodes += 1
        if self.free_head.next is None:
            self.free_head = new_free_block
        else:
            cur = self.free_head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_free_block
            new_free_block.prev = cur
            while cur.prev is not None:
                cur = cur.prev
            self.free_head = cur
        return [allocated_block, new_free_block]

    def remove_allocated_block(self, block):
        cur = self.allocated_head
        while cur is not None:
            if cur.address == block.address:
                if cur.prev is not None:
                    cur.prev.next = cur.next
                if cur.next is not None:
                    cur.next.prev = cur.prev
                self.num_allocated_nodes -= 1

            if cur.next is not None:
                cur = cur.next
            else:
                break
        while cur.prev is not None:
            cur = cur.prev
        self.allocated_head = cur

    def insert_free_block(self, block):
        cur = self.free_head
        new_block = ExplicitNode(address=block.address, end_address=block.end_address, block_size=block.block_size,
                                 ptr_num=None)
        while cur.next is not None:
            if new_block.block_size <= cur.block_size:
                if cur.prev is not None and cur.prev.block_size >= new_block.block_size:
                    cur.prev.next = new_block
                    new_block.prev = cur.prev
                    cur.prev = new_block
                    new_block.next = cur
                    self.num_free_nodes += 1
                elif cur.block_size >= block.block_size:
                    cur.prev = new_block
                    new_block.next = cur
                    self.num_free_nodes += 1
            if cur.next is not None:
                cur = cur.next
        while cur.prev is not None:
            cur = cur.prev
        self.free_head = cur

    def replace_block(self):
        return

    def join_adjacent_blocks(self):
        cur = self.free_head
        new_block = None
        while cur is not None:
            if cur.next is not None and cur.end_address + 1 == cur.next.address:
                block_size = cur.block_size + cur.next.block_size
                new_block = ExplicitNode(address=cur.address, end_address=cur.next.end_address, block_size=block_size,
                                         ptr_num=None)
                if cur.prev is not None:
                    cur.prev.next = new_block
                new_block.prev = cur.prev
                new_block.next = cur.next.next
                if cur.next.next is not None:
                    cur.next.next.prev = new_block
                self.num_free_nodes -= 1
            if cur.next is not None:
                cur = cur.next
            else:
                break
        cur = new_block
        if cur is not None:
            while cur.prev is not None:
                if cur.prev is not None:
                    cur = cur.prev
                else:
                    break
        if cur is not None:
            self.free_head = cur

    def set_mem_brk(self, heap_size):
        cur = self.free_head
        while cur.next is not None:
            cur = cur.next
        cur.end_address = heap_size

    def find_pointer_block(self, ptr_num):
        cur = self.allocated_head
        while cur is not None:
            if cur.ptr_num == ptr_num:
                return cur
            cur = cur.next

    def print_lists(self):
        allocated_cur = self.allocated_head
        print("num_allocated_nodes: " + str(self.num_allocated_nodes))
        while allocated_cur is not None:
            allocated_cur.print_node()
            allocated_cur = allocated_cur.next
        free_cur = self.free_head
        print("num_free_nodes: " + str(self.num_free_nodes))
        while free_cur is not None:
            free_cur.print_node()
            free_cur = free_cur.next
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
