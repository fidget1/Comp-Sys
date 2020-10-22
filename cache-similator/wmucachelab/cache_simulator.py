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
    cache_size = num_sets * lines_per_set * block_size
    addr_size = 64
    tag_index_bits = addr_size - (block_index_bits + set_index_bits)

    new_cache = cache.Cache(cache_size, num_sets, block_size, lines_per_set, tag_index_bits, set_index_bits,
                            block_index_bits)
    return new_cache


args = get_arguments()
initialized_cache = initialize_cache(args)
data = get_data(args.trace)
util.print_input(data)
op_num = 7
operation = data[op_num]
print("op num: " + str(op_num))
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
initialized_cache.print_cache()
