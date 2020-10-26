from wmucachelab.line import Line


class Set:
    def __init__(self, num_lines, block_size, set_num):
        self.set_num = set_num
        self.num_lines = num_lines
        self.block_size = block_size
        self.max_age = num_lines - 1
        self.lines = []
        for i in range(self.num_lines):
            self.lines.append(Line(set_num, i, False, None, None, block_size, i))

    def get_set_num(self):
        return self.set_num

    def get_line(self, i):
        return self.lines[i]

    def find_invalid_line(self):
        for i in range(self.num_lines):
            valid = self.lines[i].get_valid()
            if not valid:
                return i
        return -1

    def print_ages(self):
        for i in range(self.num_lines):
            print(self.lines[i].age)

    def find_line_num_from_tag(self, tag):
        for i in range(self.num_lines):
            if self.lines[i].get_tag() == tag:
                return i
        return None

    def get_oldest_line(self):
        _max_age = 0
        max_age_index = -1
        for i in range(len(self.lines)):
            if _max_age < self.lines[i].age:
                _max_age = self.lines[i].age
                max_age_index = _max_age
        return self.lines[max_age_index]

    def set_line(self, line_num, valid, tag, data, age):
        self.lines[line_num].set_set_num(self.set_num)
        self.lines[line_num].set_line_num(line_num)
        self.lines[line_num].set_valid(valid)
        self.lines[line_num].set_tag(tag)
        self.lines[line_num].set_block(data)
        self.lines[line_num].set_age(age)

    def print(self):
        for i in range(self.num_lines):
            self.lines[i].print()

