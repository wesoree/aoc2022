from collections import deque
from aocinput import import_aoc_read


def part1(input_file):
    pos_list = deque([(val, index) for index, val in enumerate(input_file)])
    for i, num in enumerate(input_file):
        current_index = pos_list.index((num, i))
        pos_list.remove((num, i))
        pos_list.rotate(-num)
        pos_list.insert(current_index, (num, i))
    
    final_list = list(map(lambda x: x[0], pos_list))
    zero_index = final_list.index(0)
    result = sum(final_list[(zero_index+1000*i) % len(input_file)] for i in [1, 2, 3])
    return result


def part2(input_file, decrypt_key = 811589153):
    pos_list = deque([(decrypt_key*val, index) for index, val in enumerate(input_file)])
    for _ in range(10):
        for i, num in enumerate(input_file):
            num = 811589153*num
            current_index = pos_list.index((num, i))
            pos_list.remove((num, i))
            pos_list.rotate(-num)
            pos_list.insert(current_index, (num, i))
    
    final_list = list(map(lambda x: x[0], pos_list))
    zero_index = final_list.index(0)
    result = sum(final_list[(zero_index+1000*i) % len(input_file)] for i in [1, 2, 3])
    return result

def main(input_file):
    print(f'part 1: {part1(input_file)}')
    print(f'part 2: {part2(input_file)}')

if __name__ == '__main__':
    input_file = import_aoc_read(20)
    main(input_file)