
def part1():
    overlap = 0
    lines = open("4-input.txt", "r").read().splitlines()
    for line in lines:
        first, second = line.split(",")
        first, second  = first.split('-'), second.split('-')
        concat = [[int(ch) for ch in first], [int(ch) for ch in second]]
        sorted_concat = sorted(concat)
        if sorted_concat[0][1] >= sorted_concat[1][1]:
            overlap += 1
            continue
        if sorted_concat[0][0] == sorted_concat[1][0]:
            if sorted_concat[0][1] <= sorted_concat[1][1]:
                overlap += 1
    return overlap

def part2():
    '''
    
    '''
    overlap = 0
    lines = open("4-input.txt", "r").read().splitlines()
    for line in lines:
        first, second = line.split(",")
        first, second  = first.split('-'), second.split('-')
        concat = [[int(ch) for ch in first], [int(ch) for ch in second]]
        sorted_concat = sorted(concat)
        if sorted_concat[0][1] < sorted_concat[1][0]:         
            print(sorted_concat)
            continue
        overlap += 1
    return overlap

print(part2())

