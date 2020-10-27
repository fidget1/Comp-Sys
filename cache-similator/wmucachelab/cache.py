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

    # Because without memory, load and store are identical, I'm reusing store twice.
    def modify(self, size, address, text):
        load_ret = self.store(size, address, text)["ret"]
        store_ret = self.store(size, address, text)["ret"]

        return {
            "text": text,
            "ret": load_ret + store_ret
        }

    # Load is identical to store
    def store(self, size, address, text):
        addr = Address(address, self.set_index_bits, self.block_index_bits, size)
        tag_num = addr.get_tag_num()
        set_num = addr.get_set_num()
        _set = self.get_set(set_num)
        data = _set.insert_line(set_num, tag_num)
        ret = data["ret"]
        self.hits += data["hits"]
        self.misses += data["misses"]
        self.evictions += data["evictions"]

        return {
            "text": text,
            "ret": ret
        }

