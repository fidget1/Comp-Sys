import argparse


def read_line(_line, line_type, text):
    arr = _line.split(",")
    text = text[1:]
    # print("arr[0]: " + str(arr[0]))
    address = int(str("0x" + arr[0]), 16)
    size = arr[1].replace("\n", "")
    return {"address": address, "size": size, "line_type": line_type, "text_line": text.replace("\n", "")}


def read_input(t):
    with open(t, "r") as trace_file:
        input_data = []
        for ln in trace_file:
            if ln[0] == " ":
                if ln[1] == "L":
                    input_data.append(read_line(ln[3:], "load", ln))
                elif ln[1] == "S":
                    input_data.append(read_line(ln[3:], "store", ln))
                elif ln[1] == "M":
                    input_data.append(read_line(ln[3:], "modify", ln))
    trace_file.close()
    return input_data


def print_input(data):
    for item in data:
        print(item)


def parse_arguments():
    parser = argparse.ArgumentParser(description="CPU cache simulator")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    parser.add_argument("-s", "--set-index-bits", type=int, help="index bits")
    parser.add_argument("-E", "--cache-lines", type=int, help="cache lines")
    parser.add_argument("-b", "--block-index-bits", type=int, help="block index bits")
    parser.add_argument("-t", "--trace", type=str, help="file to load")
    args = parser.parse_args()
    return args


def print_arguments(arguments):
    print("-v=" + str(arguments.verbose))
    print("-s=" + str(arguments.index_bits))
    print("-E=" + str(arguments.cache_lines))
    print("-b=" + str(arguments.block_index_bits))
    print("-t=" + arguments.trace + "\n")

