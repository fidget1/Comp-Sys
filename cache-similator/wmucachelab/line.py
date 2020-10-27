class Line:
    def __init__(self, set_num, line_num, valid, tag, data, block_size):
        self.set_num = set_num
        self.line_num = line_num
        self.valid = valid
        self.tag = tag
        self.block = data
        self.block_size = block_size

    def get_set_num(self):
        return self.set_num

    def get_line_num(self):
        return self.line_num

    def get_valid(self):
        return self.valid

    def get_tag(self):
        return self.tag

    def get_block(self):
        return self.block

    def get_block_size(self):
        return self.block_size

    def set_set_num(self, set_num):
        self.set_num = set_num

    def set_line_num(self, line_num):
        self.line_num = line_num

    def set_valid(self, valid):
        self.valid = valid

    def set_tag(self, tag):
        self.tag = tag

    def set_block(self, data):
        self.block = data

    def set_block_size(self, block_size):
        self.block_size = block_size

