from implicit_free_list import ImplicitFreeList
from implicit_free_list import ImplicitNode
from explicit_free_list import ExplicitFreeList
from explicit_free_list import ExplicitNode


def encode_header_footer_implicit(node):
    if node is None:
        print("Error: node doesn't exist.")
    return node.block_size + node.allocated


def encode_header_footer_explicit(node, allocated):
    if node is None:
        print("Error: node doesn't exist.")
    return node.block_size + allocated


class MemoryAllocator:
    def __init__(self, policy):
        self.heap_type = policy["heap_type"]
        self.algorithm = policy["algorithm"]
        self.heap_size = 4000
        self.max_heap_size = 400000
        self.num_words = int(self.heap_size / 4)
        self.words = [0 for i in range(self.num_words)]
        if self.heap_type == "implicit":
            node = ImplicitNode(address=4,
                                end_address=self.heap_size - 5,
                                allocated=0,
                                block_size=self.heap_size - 8,
                                ptr_num=None)
            self.write_to_mem(node, None)
            self.heap = ImplicitFreeList(self.heap_size, self.algorithm, node)
        else:
            node = ExplicitNode(address=4,
                                end_address=self.heap_size - 5,
                                block_size=self.heap_size - 8,
                                ptr_num=None)
            self.write_to_mem(node, 0)
            self.heap = ExplicitFreeList(self.heap_size, self.algorithm, node)

    def print_mem(self):
        for i in range(self.num_words):
            print("0x{:08x}".format(self.words[i]))
        print()

    def myalloc(self, ptr_size, ptr_num):
        if self.heap_type == "implicit":
            block_size = ((ptr_size + 7) & -8) + 8
            free_block = self.heap.find_free_block(block_size)
            if free_block.block_size == block_size:
                block = self.heap.replace_block(free_block, ptr_num)
                self.write_to_mem(block, None)
                return
            nodes = self.heap.split(free_block, ptr_size, self.heap_size, ptr_num)
            if not nodes:
                self.mysbrk(free_block.address, ptr_size)
                self.heap.set_mem_brk(self.heap_size)
                nodes = self.heap.split(free_block, ptr_size, self.heap_size, ptr_num)
            self.write_to_mem(nodes[0], None)
            self.write_to_mem(nodes[1], None)
        else:
            block_size = ((ptr_size + 7) & -8) + 8
            free_block = self.heap.find_free_block(block_size)
            if free_block.block_size == block_size:
                # block = self.heap.replace_block(free_block, ptr_num)
                self.write_to_mem(free_block, None)
                return
            nodes = self.heap.split(free_block, ptr_size, self.heap_size, ptr_num)
            if not nodes:
                self.mysbrk(free_block.address, ptr_size)
                self.heap.set_mem_brk(self.heap_size)
                nodes = self.heap.split(free_block, ptr_size, self.heap_size, ptr_num)
            self.write_to_mem(nodes[0], 1)
            self.write_to_mem(nodes[1], 0)

    def write_to_mem(self, block, allocated):
        if self.heap_type == "implicit":
            self.words[int(block.address / 4)] = encode_header_footer_implicit(block)
            self.words[int(block.end_address / 4)] = encode_header_footer_implicit(block)
        else:
            self.words[int(block.address / 4)] = encode_header_footer_explicit(block, allocated)
            self.words[int(block.end_address / 4)] = encode_header_footer_explicit(block, allocated)

    def myrealloc(self, prev_ptr_num, new_ptr_num, size):
        if self.heap_type == "implicit":
            self.myfree(prev_ptr_num)
            self.myalloc(size, new_ptr_num)
        else:
            self.myfree(prev_ptr_num)
            self.myalloc(size, new_ptr_num)

    def myfree(self, ptr_num):
        if self.heap_type == "implicit":
            block = self.heap.find_pointer_block(ptr_num)
            if block is not None:
                block.allocated = 0
                block.ptr_num = None
                blocks = self.heap.join_adjacent_blocks(block)
                for i in range(len(blocks)):
                    self.write_to_mem(blocks[i], None)
            else:
                print("Error: pointer not found.")
        else:
            block = self.heap.find_pointer_block(ptr_num)
            if block is not None:
                block.ptr_num = None
                self.heap.insert_free_block(block)
                self.heap.remove_allocated_block(block)
                self.heap.join_adjacent_blocks()
                cur = self.heap.free_head
                for i in range(self.heap.num_free_nodes):
                    if cur is not None:
                        self.write_to_mem(cur, 0)
                        cur = cur.next
                cur = self.heap.allocated_head
                for i in range(self.heap.num_allocated_nodes):
                    if cur is not None:
                        self.write_to_mem(cur, 1)
                        cur = cur.next
            else:
                print("Error: pointer not found.")

    def mysbrk(self, address, size):
        if self.heap_type == "implicit":
            new_mem_brk = address + size + 16
            if new_mem_brk > self.max_heap_size:
                print("Error: Operation exceeds heap size.")
                return
            self.heap_size = new_mem_brk

    def print_to_file(self, file_name):
        with open(file_name, "w") as f:
            for i in range(self.num_words):
                f.write(str("0x{:08x}".format(self.words[i])) + "\n")
