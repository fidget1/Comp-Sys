from wmucachelab.line import Line


class Set:
    def __init__(self, num_lines, block_size, set_num):
        self.set_num = set_num
        self.num_lines = num_lines
        self.block_size = block_size
        self.max_age = num_lines - 1
        self.lines = []
        for i in range(self.num_lines):
            self.lines.append(Line(set_num, i, False, None, None, self.block_size))

    def insert_line(self, set_num, tag_num):
        for i in range(self.num_lines):
            valid = self.lines[i].get_valid()
            tag = self.lines[i].get_tag()
            if valid and tag == tag_num:
                ret = " hit"
                hits = 1

                return {"ret": ret, "hits": hits, "misses": 0, "evictions": 0}
        for i in range(self.num_lines):
            valid = self.lines[i].get_valid()
            if not valid:
                ret = " miss"
                misses = 1
                self.set_line(i, True, tag_num, "set", self.block_size)
                return {"ret": ret, "hits": 0, "misses": misses, "evictions": 0}
        ret = " miss eviction"
        misses = 1
        evictions = 1
        self.lines.pop(0)
        self.lines.append(Line(set_num, self.num_lines - 1, True, tag_num, "set", self.block_size))
        return {"ret": ret, "hits": 0, "misses": misses, "evictions": evictions}

    def set_line(self, line_num, valid, tag, data, block_size):
        self.lines[line_num].set_set_num(self.set_num)
        self.lines[line_num].set_line_num(line_num)
        self.lines[line_num].set_valid(valid)
        self.lines[line_num].set_tag(tag)
        self.lines[line_num].set_block(data)
        self.lines[line_num].set_block_size(block_size)

