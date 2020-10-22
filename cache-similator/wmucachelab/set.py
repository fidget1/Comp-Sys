from wmucachelab import line
from wmucachelab import block


class Set:
    def __init__(self, num_lines, block_size):
        self.num_lines = num_lines
        self.block_size = block_size
        self.lines = []
        for i in range(self.num_lines):
            self.lines.append(line.Line(False, None, block.Block(block_size, None), block_size))

    def set_line(self, line_num, block_size, valid, tag, data):
        if len(self.lines) == 0:
            self.lines.append(line.Line())
        self.lines[line_num].set_valid(valid)
        self.lines[line_num].set_tag(tag)
        self.lines[line_num].set_block(block_size, data)

