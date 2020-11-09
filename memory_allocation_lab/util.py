def read_input(file):
    inp = []
    with open(file, "r") as f:
        for line in f:
            arr = line.split(", ")
            arr[len(arr) - 1] = arr[len(arr) - 1].replace("\n", "")
            inp.append(arr)
    return inp
