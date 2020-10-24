class Line:
    def __init__(self, set_num, line_num, valid, tag, data, block_size, age):
        self.set_num = set_num
        self.line_num = line_num
        self.valid = valid
        self.tag = tag
        self.block = data
        self.block_size = block_size
        self.age = age

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

    def get_age(self):
        return self.age

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

    def set_age(self, age):
        self.age = age

    def print(self):
        print("Set: " + str(self.set_num) + " | Line: " + str(self.line_num) + " | Valid: " + str(self.valid) +
              " | Tag: " + str(self.tag) + " | Block: " + str(self.block) + " | Age: " + str(self.age))

