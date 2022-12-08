import numpy as np
from io import StringIO
from itertools import product
from operator import mul
from functools import reduce

def is_visible(x: int, y: int, forest: np.ndarray) -> bool:
    neighbors_groups = forest[:x, y], forest[x+1:, y], forest[x, :y], forest[x, y+1:]
    return any((forest[x,y] > neighbors).all() for neighbors in neighbors_groups)
def get_forest(input_raw: str) -> np.ndarray:
    return np.genfromtxt(StringIO(input_raw), delimiter=1, dtype=int)
def iter_trees(shape_x, shape_y):
    yield from product(range(1, shape_x-1), range(1, shape_y-1))
def takewhile_inc(max_value, iterable):
    for x in iterable:
        if x < max_value:
            yield x
        else:
            yield x
            break
def scenic_score():
    pass
def part_1(input_raw: str) -> int:
    forest = get_forest(input_raw)
    n_visible : int = 2*(forest.shape[0] + forest.shape[1] - 2)
    n_visible += sum(is_visible(tree_x, tree_y, forest) for tree_x,tree_y in iter_trees(*forest.shape))
    return n_visible
def part_2(input_raw: str) -> int:
    pass
if __name__ == '__main__':
    with open('day8input.txt') as input_raw:
        input_raw = input_raw.read()
    print(part_1(input_raw))
    # print(part_2(input_raw))