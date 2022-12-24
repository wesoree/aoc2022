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
    if ilist is False and read_line is False or ilist is None and read_line is None:
        f = open(f'inputs/day{day}input.txt').read()
    return f

def aocsplit(day: int, long: bool, split_content):
    if long:
        with open(f'inputs/day{day}input.txt') as f:
            f = f.read().strip().split(split_content)
    if long is False:
        f = open(f'inputs/day{day}input.txt').read().strip().split(split_content)
    return f

def aocsplitday(day: int, ilist: bool, read_line: bool, splitline: bool):
    if ilist:
        f = [line.strip() for line in open(f'inputs/day{day}input.txt')]
    if read_line:
        f = open(f'inputs/day{day}input.txt').readlines()
    if splitline:
        f = open(f'inputs/day{day}input.txt').read().strip().splitlines()
    if ilist is False and read_line is False and splitline is False:
        f = open(f'inputs/day{day}input.txt').read()
    return f