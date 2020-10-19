from wmucachelab import set


class Cache:
    def __init__(self, cache_size, num_sets, block_size, lines_per_set, tag_index_bits, set_index_bits, block_index_bits):
        self.cache_size = cache_size
        self.num_sets = num_sets
        self.block_size = block_size
        self.tag_index_bits = tag_index_bits
        self.set_index_bits = set_index_bits
        self.block_index_bits = block_index_bits
        self.lines_per_set = lines_per_set
        self.sets = []

    def get_sets(self):
        return self.sets

    def set_set(self):
        if len(self.sets) >= self.num_sets:
            print("New set exceeds lines per set.")
            return
        self.sets.append(set.Set(self.lines_per_set, self.block_size))

    def print_vars(self):
        print("cache_size: " + str(self.cache_size))
        print("num_sets: " + str(self.num_sets))
        print("block_size: " + str(self.block_size))
        print("tag_index_bits: " + str(self.tag_index_bits))
        print("set_index_bits: " + str(self.set_index_bits))
        print("block_index_bits: " + str(self.block_index_bits))

    def print_cache(self):
        set_number = 1
        for i in self.sets:
            line_number = 1
            if len(i.lines) > 0:
                for j in i.lines:
                    print("Set: " + str(set_number) +
                          " | Line: " + str(line_number) +
                          " | Valid: " + str(j.valid) +
                          " | Tag: " + str(j.tag) +
                          " | Block: " + str(j.block.get_data()))
                    line_number += 1
            set_number += 1

