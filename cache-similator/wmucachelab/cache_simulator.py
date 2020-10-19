from wmucachelab import util
from wmucachelab import cache
from wmucachelab import address


def get_arguments():
    arguments = util.parse_arguments()
    return arguments


def get_data(t):
    input_data = util.read_input(t)
    return input_data


def initialize_cache(arguments):
    # util.print_arguments(args)
    set_index_bits = arguments.set_index_bits
    block_index_bits = arguments.block_index_bits
    num_sets = 2 ** arguments.set_index_bits
    lines_per_set = arguments.cache_lines
    block_size = 2 ** block_index_bits
    cache_size = block_size * lines_per_set * num_sets
    address_size = 64
    # 1 bit for valid
    tag_index_bits = address_size - (block_index_bits + set_index_bits) - 1

    new_cache = cache.Cache(cache_size, num_sets, block_size, lines_per_set, tag_index_bits, set_index_bits,
                            block_index_bits)
    for i in range(num_sets):
        new_cache.set_set()
        this_set = new_cache.get_sets()[i]
        for j in range(args.cache_lines):
            this_set.set_line(j, block_size, False, 0, 0)
    return new_cache


args = get_arguments()
initialized_cache = initialize_cache(args)
data = get_data(args.trace)
util.print_input(data)
operation = data[7]
print("address: " + str(operation["address"]))
print("address in binary: " + str(bin(operation["address"])))
address_size = 64
addr = address.Address(operation["address"], initialized_cache.set_index_bits, initialized_cache.block_index_bits,
                       address_size)
print("tag bits: " + str(addr.tag_bits))
print("tag: " + str(addr.tag_num))
print("set bits: " + str(addr.set_bits))
print("set: " + str(addr.set_num))
print("block bits: " + str(addr.block_bits))
print("block: " + str(addr.block_num))
cache_block_size = 2 ** args.block_index_bits
initialized_cache.get_sets()[0].set_line(0, cache_block_size, True, addr.tag_num, addr.block_num)
initialized_cache.print_cache()
