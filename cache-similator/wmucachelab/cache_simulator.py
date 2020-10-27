from wmucachelab import util
from wmucachelab.cache import Cache


def get_arguments():
    arguments = util.parse_arguments()
    return arguments


def get_data(t):
    input_data = util.read_input(t)
    return input_data


def initialize_cache(arguments):
    set_index_bits = arguments.set_index_bits
    block_index_bits = arguments.block_index_bits
    num_sets = 2 ** arguments.set_index_bits
    lines_per_set = arguments.cache_lines
    block_size = 2 ** block_index_bits
    cache_size = num_sets * lines_per_set * block_size
    addr_size = 64
    tag_index_bits = addr_size - (block_index_bits + set_index_bits)

    new_cache = Cache(cache_size, num_sets, block_size, lines_per_set, tag_index_bits, set_index_bits, block_index_bits)
    return new_cache


def operate(operation_line, _cache, verbose):
    _address = operation_line["address"]
    size = int(operation_line["size"])
    op = operation_line["line_type"]
    text = operation_line["text_line"].replace("\n", "")
    if _address is None:
        ret = text
        print(ret)
    else:
        # Since load and store are identical, they've been consolidated
        if op == "load":
            store_ret = _cache.store(size, _address, text)
            if verbose:
                print(store_ret["text"] + store_ret["ret"])
        elif op == "modify":
            mod_ret = _cache.modify(size, _address, text)
            if verbose:
                print(mod_ret["text"] + mod_ret["ret"])
        elif op == "store":
            store_ret = _cache.store(size, _address, text)
            if verbose:
                print(store_ret["text"] + store_ret["ret"])
    return _cache


args = get_arguments()
initialized_cache = initialize_cache(args)
data = get_data(args.trace)
for item in data:
    initialized_cache = operate(item, initialized_cache, args.verbose)
print("hits:" + str(initialized_cache.hits) + " misses:" + str(initialized_cache.misses) + " evictions:" +
      str(initialized_cache.evictions))
