class ExplicitFreeList:
    def __init__(self):
        self.head = None
        self.num_nodes = 0

    def find_free_block(self, block_size):
        if self.num_nodes == 0:
            self.head = ExplicitNode(0, 1000)
            self.num_nodes += 1
            return self.head

    def remove_first(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        tmp = self.head
        self.head = self.head.next
        self.head.prev = None
        self.num_nodes -= 1
        return tmp

    def remove_specific(self, node):
        if self.head is None:
            return
        cur = self.head
        if cur.address == node.address and cur.block_size == node.block_size:
            if cur.next is None:
                self.head = None
                self.num_nodes -= 1
                return cur
            else:
                cur.next.prev = None
                self.head = cur.next
                self.num_nodes -= 1
                return cur
        while True:
            if cur.address == node.address and cur.block_size == node.block_size:
                if cur.next is None:
                    cur.prev.next = None
                    self.num_nodes -= 1
                    return cur
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    self.num_nodes -= 1
                    return cur
            if cur.next is not None:
                cur = cur.next

    def remove_last(self):
        if self.head is None:
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        tmp = cur
        cur.prev.next = None
        self.num_nodes -= 1
        return tmp

    def prepend(self, address, block_size):
        node = ExplicitNode(address=address, block_size=block_size)
        node.prev = None
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        self.num_nodes += 1
        return node

    def insert_after(self, address, block_size, prev):
        if not self.node_in_heap(prev):
            print("Error - node not in heap.")
            return
        node = ExplicitNode(address=address, block_size=block_size)
        node.next = prev.next
        prev.next = node
        node.prev = prev
        if node.next is not None:
            node.next.prev = node
        cur = node
        while cur.prev is not None:
            cur = cur.prev
        self.head = cur
        self.num_nodes += 1
        return node

    def node_in_heap(self, node):
        cur = self.head
        for i in range(0, self.num_nodes):
            if cur.address == node.address and cur.block_size == node.block_size:
                return True
            if cur.next is not None:
                cur = cur.next
        return False

    def append(self, address, block_size):
        node = ExplicitNode(address=address, block_size=block_size)
        if self.head is None:
            node.prev = None
            self.head = node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        node.prev = cur
        self.num_nodes += 1
        return node

    def print(self):
        cur = self.head
        print("num_nodes: " + str(self.num_nodes))
        for i in range(0, self.num_nodes):
            cur.print()
            cur = cur.next

    def split(self, free_block, block_size, heap_size, op_num):
        pass

    def print_list(self):
        cur = self.head
        print("num_nodes: " + str(self.num_nodes))
        while cur is not None:
            cur.print_node()
            cur = cur.next


class ExplicitNode:
    def __init__(self, address, block_size, op_num):
        self.address = address
        self.block_size = block_size
        self.end = self.address + self.block_size - 1
        self.op_num = op_num
        self.free = True
        self.next = None
        self.prev = None

    def print(self):
        print(str(self.address) + ",\t" + str(self.block_size) + ",\t" + str(self.end) + ",\t" + str(self.free))
