
def part1():

    priority_sum = 0
    with open('3-input.txt') as file:  
        for line in file.readlines(): 

            len_items = len(line) // 2
            first, second = set(line[:len_items]), set(line[len_items:-1])

            common = first.intersection(second).pop()
            assert len(common) == 1, "Uhoh"

            if common.isupper():
                priority_sum += ord(common) - 38
            else:
                priority_sum += ord(common) - 96

    return priority_sum


def part2():

    priority_sum = 0
    lines = open("3-input.txt", "r").read().splitlines()

    for pos in range(0, len(lines), 3):
        three_groups = lines[pos : pos + 3]
        group_sets = [set(i) for i in three_groups]

        common = group_sets[0].intersection(*group_sets)

        assert len(common) == 1, "Uhoh" 
        common = list(common)[0]

        if common.isupper():
            priority_sum += ord(common) - 38
        else:
            priority_sum += ord(common) - 96

    return priority_sum

print(part2())

