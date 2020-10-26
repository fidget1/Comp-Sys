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
        # self.print_cache()
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
            # print("valid: " + str(valid) + " | data_in_range: " + str(data_in_range))
            if not valid:
                ret = " miss"
                self.misses += 1
                line.set_valid(True)
                line.set_tag(tag_num)
                line.set_block("set")
                line.set_age(0)
            else:
                ret = " miss eviction"
                self.misses += 1
                self.evictions += 1
                line.set_valid(True)
                line.set_tag(tag_num)
                line.set_block("set")
                line.set_age(0)
        else:
            # print("tag found")
            line = _set.get_line(line_num)
            valid = line.get_valid()
            if not valid:
                ret = " miss"
                self.misses += 1
                line.set_valid(True)
                line.set_tag(tag_num)
                line.set_block("set")
                line.set_age(0)
            else:
                ret = " hit"
                self.hits += 1
                line.set_valid(True)
                line.set_tag(tag_num)
                line.set_block("set")
                line.set_age(0)
        return {
            "text": text,
            "ret": ret
        }

    def modify(self, size, address, text):
        load_ret = self.load(size, address, text)["ret"]
        store_ret = self.store(size, address, text)["ret"]

        return {
            "text": text,
            "ret": load_ret + store_ret
        }

    def store(self, size, address, text):
        self.print_cache()
        addr = Address(address, self.set_index_bits, self.block_index_bits, size)
        tag_num = addr.get_tag_num()
        set_num = addr.get_set_num()
        block_offset = addr.get_block_num()
        # print_op(self.set_index_bits, self.tag_index_bits, self.block_index_bits, set_num, tag_num, block_offset, size)
        _set = self.get_set(set_num)
        # _set.print()
        line_num = _set.find_line_num_from_tag(tag_num)
        # print("store: line_num: " + str(line_num))
        if line_num is None:
            # print("tag not found")
            line = _set.get_oldest_line()
            valid = line.get_valid()
            if not valid:
                # print("not valid or data not in range")
                # print("valid: " + str(valid))
                line.set_valid(True)
                line.set_tag(tag_num)
                line.set_block("set")
                line.set_age(0)
                ret = " miss"
                self.misses += 1
            else:
                # print("tag not found, valid, data in range")
                # print("valid: " + str(valid) + "| in range: " + str(data_in_range))
                line.set_valid(True)
                line.set_tag(tag_num)
                line.set_block("set")
                line.set_age(0)
                ret = " miss eviction"
                self.misses += 1
                self.evictions += 1
        else:
            # print("tag found")
            line = _set.get_line(line_num)
            valid = line.get_valid()
            if valid:
                ret = " hit"
                self.hits += 1
                # _set.set_line()
                line.set_valid(True)
                line.set_tag(tag_num)
                line.set_block("set")
                line.set_age(0)
            else:
                ret = " unknown"
                print("store: something else happened")
        return {
            "text": text,
            "ret": ret
        }

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
