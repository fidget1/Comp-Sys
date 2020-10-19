from wmucachelab import line


class Set:
    def __init__(self, num_lines, block_size):
        self.num_lines = num_lines
        self.block_size = block_size
        self.lines = []

    def set_line(self, line_num, block_size, valid, tag, data):
        if len(self.lines) == 0:
            self.lines.append(line.Line())
        self.lines[line_num].set_valid(valid)
        self.lines[line_num].set_tag(tag)
        self.lines[line_num].set_block(block_size, data)

