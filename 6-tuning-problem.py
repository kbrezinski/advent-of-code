

def part1():

    lines = open("6-input.txt", "r").read().splitlines()[0]
    for pos in range(14, len(lines)):
        buffer = lines[pos - 14 : pos]
        if len(buffer) == len(set(buffer)):
            print(pos, buffer)  # part 2 uses 14 instead of 4
            return 

part1()

