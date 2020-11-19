class ImplicitFreeList:
    def __init__(self, size, algorithm, node):
        self.head = node
        self.algorithm = algorithm
        self.num_nodes = 1
        self.size = size

    def print_self(self):
        print("Implicit free list:\n\talgorithm: " + str(self.algorithm) + ",\tfree:" + str(self.num_nodes) +
              ",\tsize: " + str(self.size))

    def find_free_block(self, block_size):
        if self.algorithm == "first-fit":
            if self.head is None:
                print("error - head is None for some reason")
            if self.head.next is None and self.head.allocated == 0:
                # print("Only head block exists. Block is free. Requested block size is smaller than block size.")
                return self.head
            else:
                cur = self.head
                while cur.next is not None:
                    cur = cur.next
                    if cur.allocated == 0 and cur.block_size >= block_size:
                        return cur
                print("error")
        else:
            if self.head is None:
                print("error - head is None for some reason")
            if self.head.next is None and self.head.allocated == 0:
                return self.head
            else:
                cur = self.head
                best_fit = None
                min_difference = 100000000
                while cur is not None:
                    if cur.allocated == 0 and cur.block_size >= block_size:
                        cur_difference = cur.block_size - block_size
                        if cur_difference == 0:
                            return cur
                        if cur_difference < min_difference:
                            min_difference = cur_difference
                            best_fit = cur
                    cur = cur.next
                return best_fit

    def replace_block(self, free_block, ptr_num):
        free_block.ptr_num = ptr_num
        free_block.allocated = 1
        cur = free_block
        while cur is not None:
            if cur.prev is None:
                self.head = cur
            cur = cur.prev

        return free_block

    def split(self, old_free_block, payload_size, heap_size, ptr_num):
        if not old_free_block:
            print("error - split, free block doesn't exist")
            return False
        if old_free_block.allocated == 1:
            print("error - split, block not free")
            return False
        block_size = ((payload_size + 7) & -8) + 8
        if old_free_block.address + block_size > heap_size:
            # print("warning - split, exceeds heap size")
            return False
        allocated_end_address = old_free_block.address + block_size - 1
        allocated_block = ImplicitNode(address=old_free_block.address,
                                       end_address=allocated_end_address,
                                       allocated=1,
                                       block_size=block_size,
                                       ptr_num=ptr_num)
        allocated_block.payload_address = allocated_block.address + 4
        allocated_block.payload_size = payload_size
        new_free_address = old_free_block.address + block_size
        # next address minus newly allocated
        new_free_block_size = (old_free_block.end_address + 1) - (old_free_block.address + block_size)
        new_free_block = ImplicitNode(address=new_free_address,
                                      end_address=old_free_block.end_address,
                                      allocated=0,
                                      block_size=new_free_block_size,
                                      ptr_num=None)
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
                    new_free_block.next = cur.next
                    self.num_nodes += 1
        return [allocated_block, new_free_block]

    def join_adjacent_blocks(self, block):
        ret_blocks = []
        if block is None:
            print("error - block is None")
            return
        if block.allocated == 1:
            print("error - block is not free")
            return
        if block.prev is not None:
            if block.prev.allocated == 0:
                new_block = self.join_blocks(first=block.prev, second=block)
                ret_blocks.append(new_block)
                if new_block.next is not None:
                    if new_block.next.allocated == 0:
                        new_block = self.join_blocks(first=new_block, second=new_block.next)
                        ret_blocks[0] = new_block
                        self.print_list()
                        return ret_blocks
            elif block.next is not None:
                if block.next.allocated == 0:
                    new_block = self.join_blocks(first=block, second=block.next)
                    ret_blocks.append(new_block)
                    return ret_blocks
                else:
                    block.allocated = 0
                    ret_blocks.append(block)
                    return ret_blocks
        elif block.next is not None:
            if block.next.allocated == 0:
                new_block = self.join_blocks(first=block, second=block.next)
                ret_blocks.append(new_block)
            else:
                block.allocated = 0
                ret_blocks.append(block)

        if not ret_blocks:
            ret_blocks.append(block)

        return ret_blocks

    def join_blocks(self, first, second):
        address = first.address
        end_address = second.end_address
        prev_node = first.prev
        next_node = second.next
        block_size = first.block_size + second.block_size
        new_block = ImplicitNode(address=address,
                                 end_address=end_address,
                                 allocated=0,
                                 block_size=block_size,
                                 ptr_num=None)
        new_block.prev = prev_node
        new_block.next = next_node
        if new_block.next:
            new_block.next.prev = new_block
        if new_block.prev:
            new_block.prev.next = new_block
        new_block.payload_size = None
        new_block.payload_address = None
        cur = new_block
        while cur.prev is not None:
            cur = cur.prev
        self.head = cur
        self.num_nodes -= 1
        return new_block

    def set_mem_brk(self, heap_size):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.end_address = heap_size

    def find_pointer_block(self, ptr_num):
        cur = self.head
        while cur is not None:
            if cur.ptr_num == ptr_num:
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
    def __init__(self, address, end_address, allocated, block_size, ptr_num):
        self.address = address
        self.block_size = block_size
        self.end_address = end_address
        self.allocated = allocated
        self.ptr_num = ptr_num
        self.payload_address = None
        self.payload_size = None
        self.prev = None
        self.next = None

    def print_node(self):
        print("\taddress: " + str(self.address) + ",\tpayload_address: " + str(self.payload_address) +
              "\tpayload_size: " + str(self.payload_size) + ",\tend_address: " + str(self.end_address) +
              ",\tblock_size: " + str(self.block_size) + ",\tallocated: " + str(self.allocated) +
              ",\tptr_num: " + str(self.ptr_num))
        #  + ",\tprev: " + str(self.prev) + ",\tnext: " + str(self.next)
