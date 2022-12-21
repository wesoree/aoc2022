import sys
import numpy as np
from io import StringIO
from itertools import product
from operator import mul
from functools import reduce


def is_visible(x: int, y: int, forest: np.ndarray) -> bool:
    neighbors_groups = forest[:x, y], forest[x + 1:, y], forest[x, :y], forest[x, y+1:]
    return any((forest[x, y] > neighbors).all() for neighbors in neighbors_groups)


def get_forest(input_data: str) -> np.ndarray:
    return np.genfromtxt(StringIO(input_data), delimiter=1, dtype=int)


def iter_trees(shape_x, shape_y):
    yield from product(range(1, shape_x-1), range(1, shape_y-1))


def part_1(input_data: str) -> int:
    forest = get_forest(input_data)
    n_visible: int = 2*(forest.shape[0] + forest.shape[1] - 2)
    n_visible += sum(is_visible(tree_x, tree_y, forest) for tree_x, tree_y in iter_trees(*forest.shape))
    return n_visible


def main() -> None:

    itxt = open("day8input.txt", mode='r').read().splitlines()
    tree = {(x, y): t for y, row in enumerate(itxt) for x, t in enumerate(list(row))}
    visi = {(x, y): 0 for y, row in enumerate(itxt) for x, _ in enumerate(list(row))}

    for xt, yt in tree.keys():
        if xt == 0 or yt == 0 or xt == len(list(itxt)) or yt == len(itxt):
            continue

        lr = rl = tb = bt = 0

        for xc in range(xt + 1, len(list(itxt))):  # l->r
            lr += 1

            if tree.get((xc, yt)) >= tree.get((xt, yt)):
                break

        for xc in range(xt - 1, -1, -1):  # r->l
            rl += 1

            if tree.get((xc, yt)) >= tree.get((xt, yt)):
                break

        for yc in range(yt + 1, len(itxt)):  # t->b
            tb += 1

            if tree.get((xt, yc)) >= tree.get((xt, yt)):
                break

        for yc in range(yt - 1, -1, -1):  # b->t
            bt += 1

            if tree.get((xt, yc)) >= tree.get((xt, yt)):
                break

        visi.update({(xt, yt): lr * rl * tb * bt})

    print(sorted(visi.values())[-1])


if __name__ == '__main__':
    with open('inputs/day8input.txt') as input_raw:
        input_data = input_raw.read()
    print(part_1(input_data))
    sys.exit(main())
