

def part1():

    cargo = [['Z', 'T', 'F', 'R', 'W', "J", 'G'],
            ['G', 'W', 'M'],
            ['J', 'N', 'H', 'G'],
            ['J', 'R', 'C', 'N', 'W'],
            ['W', 'F', 'S', 'B', 'G', 'Q', 'V', 'M'],
            ['S', 'R', 'T', 'D', 'V', 'W', 'C'],
            ['H', 'B', 'N', 'C', 'D', 'Z', 'G', 'V'],
            ['S', 'J', 'N', 'M', 'G', 'C'],
            ['G', 'P', 'N', 'W', 'C', 'J', 'D', 'L']]

    lines = open("5-input.txt", "r").read().splitlines()[10:]
    for line in lines:
        _, count, _, src, _, dst = line.split()
        src, count, dst = int(src)-1, int(count), int(dst)-1
        items_moved = cargo[src][-count:]
        del cargo[src][-count:]
        cargo[dst].extend(items_moved[::1])  # part two is just the non-reversed indexing
        print(f"Finished moving {count} from {src+1} to {dst+1}")

    for stack in cargo: print(stack[-1])
    return cargo

part1()

