from wmucachelab.set import Set
from wmucachelab.address import Address


class Cache:
    def __init__(self, cache_size, num_sets, block_size, lines_per_set, tag_index_bits, set_index_bits,
                 block_index_bits):
        self.cache_size = cache_size
        self.num_sets = num_sets
        self.block_size = block_size
        self.tag_index_bits = tag_index_bits
        self.set_index_bits = set_index_bits
        self.block_index_bits = block_index_bits
        self.lines_per_set = lines_per_set
        self.hits = 0
        self.misses = 0
        self.evictions = 0
        self.sets = []
        for i in range(num_sets):
            self.sets.append(Set(self.lines_per_set, self.block_size, i))

    def get_set(self, index):
        if index > len(self.sets):
            return None
        return self.sets[index]

    def load(self, size, address, text):
        addr = Address(address, self.set_index_bits, self.block_index_bits, size)
        tag_num = addr.get_tag_num()
        set_num = addr.get_set_num()
        block_offset = addr.get_block_num()
        # print("\tSet: " + str(set_num) + "\n\tTag: " + str(tag_num) + "\n\tBlock: " + str(block_offset))
        _set = self.get_set(set_num)
        ret = None
        if _set is not None:
            # _set.print()
            # print("set not none")
            line_num = _set.find_line_num_from_tag(tag_num)
            if line_num is not None:
                # print("line_num not none")
                line = _set.get_line(line_num)
                if line is not None:
                    # print("line not none")
                    valid = line.get_valid()
                    data_in_range = _set.block_valid_size(block_offset, size)
                    # print("DATA IN RANGE: " + str(data_in_range))
                    if line_num is None or not valid or not data_in_range:
                        # print("line_num not none, valid, in range")
                        ret = " miss"
                        self.misses += 1
                    else:
                        ret = " hit"
                        self.hits += 1
                else:
                    print("something else happened")
            else:
                # tag not found
                line = _set.get_line(None)
                valid = line.get_valid()
                ret = " miss"
                self.misses += 1
                if valid:
                    ret += " eviction"
                    self.evictions += 1
                # else:
                    # print("something else happened")
        else:
            print("something else happened")

        return text + ret

    def store(self, size, address, text):
        addr = Address(address, self.set_index_bits, self.block_index_bits, size)
        tag_num = addr.get_tag_num()
        set_num = addr.get_set_num()
        block_offset = addr.get_block_num()
        # print("\tSet: " + str(set_num) + "\n\tTag: " + str(tag_num) + "\n\tBlock: " + str(block_offset))
        _set = self.get_set(set_num)
        # _set.print()
        ret = None
        if _set is not None:
            # print("set not None")
            # _set.print()
            line_num = _set.find_line_num_from_tag(tag_num)
            # print("line number \t\t!!!")
            # tag not found
            if line_num is None:
                # print("line_num is None")
                line = _set.get_line(line_num)
                # print("LINE: " + str(line_num))
                # line_num = line.get_line_num()
                if line is not None:
                    # print("line is not None")
                    valid = line.get_valid()
                    data_in_range = _set.block_valid_size(block_offset, size)
                    # print("data_in_range: " + str(data_in_range))
                    # print("valid: " + str(valid))
                    if data_in_range and not valid:
                        # print("data in range")
                        line.set_valid(True)
                        line.set_tag(tag_num)
                        line.set_block("set")
                        ret = " hit"
                        self.hits += 1
                    else:
                        line.set_tag(tag_num)
                        line.set_block("set")
                        ret = " hit"
                        self.hits += 1
                        # print("something else happened1")
                else:
                    print("something else happened2")
            else:
                # tag not found
                line = _set.get_line(None)
                # line.print()
                valid = line.get_valid()
                # print("VALID: " + str(valid))
                ret = " miss"
                self.misses += 1
                if valid:
                    ret += " eviction"
                    self.evictions += 1
                # else:
                    # print("something else happened")
        else:
            print("something else happened3")
        return text + ret

    def modify(self, size, address, text):
        addr = Address(address, self.set_index_bits, self.block_index_bits, size)
        tag_num = addr.get_tag_num()
        set_num = addr.get_set_num()
        block_offset = addr.get_block_num()
        # print("\tSet: " + str(set_num) + "\n\tTag: " + str(tag_num) + "\n\tBlock: " + str(block_offset))
        _set = self.get_set(set_num)
        ret = None
        if _set is not None:
            # print("set is not None")
            # _set.print()
            line_num = _set.find_line_num_from_tag(tag_num)
            # tag not found
            if line_num is None:
                ret = " miss"
                self.misses += 1
                # print("line_num is None")
                line = _set.get_line(line_num)
                # line_num = line.get_line_num()
                if line is not None:
                    # print("line is not None")
                    valid = line.get_valid
                    data_in_range = _set.block_valid_size(block_offset, size)
                    if data_in_range:
                        line.set_valid(True)
                        line.set_tag(tag_num)
                        line.set_block("set")
                        ret += " hit"
                        self.hits += 1
                    else:
                        print("something else happened")
                else:
                    print("something else happened")
            else:
                # tag not found
                line = _set.get_line(None)
                # line.print()
                valid = line.get_valid()
                # print("VALID: " + str(valid))
                ret = " miss"
                self.misses += 1
                if valid:
                    ret += " eviction hit"
                    self.evictions += 1
                    self.hits += 1
                else:
                    print("something else happened")
        else:
            print("something else happened")
        return text + ret

    def print(self):
        for i in range(self.num_sets):
            self.get_set(i).print()

    def print_vars(self):
        print("cache_size: " + str(self.cache_size))
        print("num_sets: " + str(self.num_sets))
        print("block_size: " + str(self.block_size))
        print("tag_index_bits: " + str(self.tag_index_bits))
        print("set_index_bits: " + str(self.set_index_bits))
        print("block_index_bits: " + str(self.block_index_bits))

