from wmucachelab import block


class Line:
    def __init__(self):
        self.valid = False
        self.tag = None
        self.block = None

    def get_valid(self):
        return self.valid

    def get_tag(self):
        return self.tag

    def get_block(self):
        return self.block

    def set_valid(self, valid):
        self.valid = valid

    def set_tag(self, tag):
        self.tag = tag

    def set_block(self, block_size, data):
        self.block = block.Block(block_size, data)

    def print_line(self):
        print("valid: " + str(self.valid) + " | tag: " + str(self.tag) + " | block: " + str(self.block))

