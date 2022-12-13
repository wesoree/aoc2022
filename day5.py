import copy
import re

with open('day5input.txt') as f:
    # parse as { 1: ['A'], 2: ['B', 'C'] }
    cargo = {
        int(c[0]): [*filter(str.isalpha, c)]
        for c in zip(*[*iter(f.readline, '\n')][::-1])  # transpose
        if c[0].isdigit()
    }
    # parse as [ [1, 2, 3], [2, 3, 1] ]
    instructions = [
        [*map(int, re.findall(r'\d+', instr))]
        for instr in f.readlines()
    ]


def solve(cargos, instr, direction):
    for count, fr, to in instr:
        cargos[to].extend(
            [cargos[fr].pop() for _ in range(min(len(cargos[fr]), count))][::direction]
        )

    return ''.join(c[-1] for c in cargos.values() if c)


print('Part 1:', solve(copy.deepcopy(cargo), instructions, 1))
print('Part 2:', solve(copy.deepcopy(cargo), instructions, -1))