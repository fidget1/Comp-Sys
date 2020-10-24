from wmucachelab.line import Line


class Set:
    def __init__(self, num_lines, block_size, set_num):
        self.set_num = set_num
        self.num_lines = num_lines
        self.block_size = block_size
        self.lines = []
        for i in range(self.num_lines):
            self.lines.append(Line(set_num, i, False, None, None, block_size, i))

    def find_line_num_from_tag(self, tag):
        for i in range(self.num_lines):
            if self.lines[i].get_tag() == tag:
                return i
        return None

    def block_valid_size(self, block_offset, data_size):
        ret = False
        # print("BLOCK OFFSET: " + str(block_offset))
        # print("DATA SIZE: " + str(data_size))
        # print("BLOCK_SIZE: " + str(self.block_size))
        if block_offset + data_size <= self.block_size:
            ret = True
        return ret

    def get_line(self, line_num):
        if line_num is None:
            line_num = self.get_oldest_line()
            # print("AFTER GET OLDEST LINE ( line_num: " + str(line_num))
            # print("GET LINE\n\n")
            # self.lines[line_num].print()
        elif line_num > len(self.lines):
            return None

        return self.lines[line_num]

    def get_oldest_line(self):
        max_age = -1
        line_index = -1
        for i in range(len(self.lines)):
            if self.lines[i].get_age() > max_age:
                max_age = self.lines[i].get_age()
                line_index = i
        return line_index

    def set_line(self, set_num, line_num, valid, tag, data, age):
        self.lines[line_num].set_set_num(set_num)
        self.lines[line_num].set_line_num(line_num)
        self.lines[line_num].set_valid(valid)
        self.lines[line_num].set_tag(tag)
        self.lines[line_num].set_block(data)
        self.lines[line_num].set_age(age)

    def print(self):
        for i in range(self.num_lines):
            self.lines[i].print()

