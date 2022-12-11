with open('day10input.txt', 'r') as file:
    commands = [_.split(' ') for _ in file.read().split('\n')]

x = 1
states = []
for command_number, c in enumerate(commands):
    if len(c) == 1:
        states.append(x)
    if len(c) == 2:
        states += [x, x]
        x += int(c[1])

print("Signal strength: ", sum([(i+1)*val for i, val in enumerate(states)if (i+1) % 40 - 20 == 0]))

crt = [
    "##" if i%40 in list(range(_-1, _+2)) else '  '
    for i, _ in enumerate(states)
]
crt = [crt[i:i+40] for i in range(0, len(crt), 40)]
print("\n".join(["".join(_) for _ in crt]))