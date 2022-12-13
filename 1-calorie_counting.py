

## get the most calories

rein_list = []
calorie_list = []
with open('1-input.txt') as file:

    for line in file.readlines():
        if line == '\n':
            calorie_list.append(rein_list)
            rein_list = []
        else:
            rein_list.append(int(line.split("\n")[0]))

print(sum(sorted([sum(i) for i in calorie_list])[-3:]))