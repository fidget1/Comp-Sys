from wmucachelab.set import Set
from wmucachelab.address import Address


def print_op(set_index_bits, tag_index_bits, block_index_bits, set_num, tag_num, block_offset, size):
    print("\tSet Index Bits: " + str(set_index_bits) + "\n\tTag Index Bits: " + str(tag_index_bits) +
          "\n\tBlock Index Bits: " + str(block_index_bits) + "\n\tSet: " + str(set_num) + "\n\tTag: " + str(tag_num) +
          "\n\tBlock: " + str(block_offset) + "\n\tData size: " + str(size))


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
        # print_op(self.set_index_bits, self.tag_index_bits, self.block_index_bits, set_num, tag_num, block_offset, size)
        _set = self.get_set(set_num)
        # _set.print()
        line_num = _set.find_line_num_from_tag(tag_num)
        if line_num is None:
            # print("tag not found")
            line = _set.get_oldest_line()
            valid = line.get_valid()
            data_in_range = _set.block_valid_size(block_offset, size)
            # print("valid: " + str(valid) + " | data_in_range: " + str(data_in_range))
            if not valid or not data_in_range:
                ret = " miss"
                self.misses += 1
            elif valid and data_in_range:
                ret = " miss eviction"
                self.misses += 1
                self.evictions += 1
            else:
                ret = " unknown"
                print("load: something else happened")
        else:
            # print("tag found")
            line = _set.get_line(line_num)
            valid = line.get_valid()
            data_in_range = _set.block_valid_size(block_offset, size)
            if not valid or not data_in_range:
                ret = " miss"
                self.misses += 1
            elif valid and data_in_range:
                ret = " hit"
                self.hits += 1
            else:
                ret = " unknown"
                print("load: something else happened")
        return text + ret

    def modify(self, size, address, text):
        addr = Address(address, self.set_index_bits, self.block_index_bits, size)
        tag_num = addr.get_tag_num()
        set_num = addr.get_set_num()
        block_offset = addr.get_block_num()
        # print_op(self.set_index_bits, self.tag_index_bits, self.block_index_bits, set_num, tag_num, block_offset, size)
        _set = self.get_set(set_num)
        # _set.print()
        line_num = _set.find_line_num_from_tag(tag_num)
        if line_num is None:
            # print("tag not found")
            ret = " miss"
            self.misses += 1
            line = _set.get_oldest_line()
            valid = line.get_valid()
            data_in_range = _set.block_valid_size(block_offset, size)
            if data_in_range and not valid:
                line.set_valid(True)
                line.set_tag(tag_num)
                line.set_block("set")
                ret += " hit"
                self.hits += 1
            else:
                print("valid: " + str(valid) + " | data_in_range: " + str(data_in_range))
                print("modify: something else happened1")
        else:
            # print("tag found")
            line = _set.get_line(line_num)
            # line.print()
            valid = line.get_valid()
            ret = " miss"
            self.misses += 1
            if valid:
                ret += " eviction hit"
                self.evictions += 1
                self.hits += 1
            else:
                ret += " hit"
                self.hits += 1
                print("modify: something else happened2")
        return text + ret

    def store(self, size, address, text):
        self.print_cache()
        addr = Address(address, self.set_index_bits, self.block_index_bits, size)
        tag_num = addr.get_tag_num()
        set_num = addr.get_set_num()
        block_offset = addr.get_block_num()
        print_op(self.set_index_bits, self.tag_index_bits, self.block_index_bits, set_num, tag_num, block_offset, size)
        _set = self.get_set(set_num)
        _set.print()
        line_num = _set.find_line_num_from_tag(tag_num)
        if line_num is None:
            # print("tag not found")
            line = _set.get_oldest_line()
            valid = line.get_valid()
            data_in_range = _set.block_valid_size(block_offset, size)
            if not valid or not data_in_range:
                print("not valid or data not in range")
                line.set_valid(True)
                line.set_tag(tag_num)
                line.set_block("set")
                ret = " hit"
                self.hits += 1
            elif valid and data_in_range:
                print("tag not found, valid, data in range")
                line.set_valid(True)
                line.set_tag(tag_num)
                line.set_block("set")
                ret = " hit"
                self.hits += 1
            else:
                ret = " unknown"
                print("store: something else happened")
        else:
            # print("tag found")
            line = _set.get_line(line_num)
            valid = line.get_valid()
            ret = " miss"
            self.misses += 1
            if valid:
                ret += " eviction"
                self.evictions += 1
            else:
                ret = " unknown"
                print("store: something else happened")
        return text + ret

    def print_cache(self):
        for i in range(self.num_sets):
            self.get_set(i).print()

    def print_vars(self):
        print("cache_size: " + str(self.cache_size))
        print("num_sets: " + str(self.num_sets))
        print("block_size: " + str(self.block_size))
        print("tag_index_bits: " + str(self.tag_index_bits))
        print("set_index_bits: " + str(self.set_index_bits))
        print("block_index_bits: " + str(self.block_index_bits))
