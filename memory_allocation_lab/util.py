import argparse


def read_input(file):
    inp = []
    with open(file, "r") as f:
        for line in f:
            arr = line.split(", ")
            arr[len(arr) - 1] = arr[len(arr) - 1].replace("\n", "")
            inp.append(arr)
    return inp


def parse_args():
    parser = argparse.ArgumentParser(description="Accept heap type and algorithm.")
    parser.add_argument('-H',
                        '--heap-type',
                        type=str,
                        help='Heap type. Specifies an \"implicit\" or \"explicit\" list.')
    parser.add_argument('-A',
                        '--algorithm',
                        type=str,
                        help='Algorithm. Specifies an \"first-fit\" or \"best-fit\".')
    args = parser.parse_args()
    return args
