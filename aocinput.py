def import_aoc_list(day):
    with open(f'inputs/day{day}input.txt') as f:
        f = [line.strip() for line in f]
    
    return f

def import_aoc(day):
    with open(f'inputs/day{day}input.txt') as f:
        f = f.read()
    
    return f

def import_aoc_read(day):
    input_file = list(map(int, open(f'inputs/day{day}input.txt', 'r').read().strip().split('\n')))

    return input_file

def import_aoc_readlines(day):
    with open(f'inputs/day{day}input.txt') as f:
        f = f.readlines()
    return f

def aocday(day: int, ilist: bool, read_line: bool):
    if ilist:
        f = [line.strip() for line in open(f'inputs/day{day}input.txt')]
    if read_line:
        f = open(f'inputs/day{day}input.txt').readlines()
    if ilist is False and read_line is False:
        f = open(f'inputs/day{day}input.txt').read()
    return f