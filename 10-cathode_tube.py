
lines = open("10-input.txt", "r").read().splitlines()

sig = 1
sig_str = []

for line in lines:
    if line != "noop":
        *_, value = line.split()
        sig_str.append(sig) # first pass
        sig += int(value)
    sig_str.append(sig)     # second pass / noop

target_cycles = [20, 60, 100, 140, 180, 220]
print(sum(cycle * sig_str[cycle] for cycle in target_cycles))