class Block:
    def __init__(self, block_size, data):
        self.block_size = block_size
        self.data = data

    def get_data(self):
        return self.data

    def print_block(self):
        print("block: " + str(self.data))