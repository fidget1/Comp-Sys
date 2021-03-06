class Address:
    def __init__(self, address, set_index_bits, block_index_bits, size):
        self.address = address
        self.size = size
        self.tag_bits = self.size - (set_index_bits + block_index_bits)
        self.set_bits = set_index_bits
        self.block_bits = block_index_bits
        self.tag_num = address >> (set_index_bits + block_index_bits)
        set_mask = "0b"
        for bit in range(set_index_bits):
            set_mask += "1"
        self.set_num = (address >> block_index_bits) & int(set_mask, 2)
        block_mask = "0b"
        for bit in range(block_index_bits):
            block_mask += "1"
        self.block_num = address & int(block_mask, 2)

    def get_address(self):
        return self.address

    def get_tag_num(self):
        return self.tag_num

    def get_set_num(self):
        return self.set_num

    def get_block_num(self):
        return self.block_num

