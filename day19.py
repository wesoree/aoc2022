import re
import sys
import numpy as np


MINERALS = {'ore': 0, 'clay': 1, 'obsidian': 2, 'geode': 3}
def to_array(bp):
    arr = np.zeros([4, 4], dtype=np.uint32)
    for bot in bp:
        i = MINERALS[bot['type']]
        for n, mineral in bot['costs']:
            j = MINERALS[mineral]
            arr[i][j] = n
    return arr


def parse_input(path):
    words = open(path).read().split()
    bps = []
    i = 0
    while i < len(words):
        if words[i] == 'Blueprint':
            bps.append([])
            i += 2
        elif words[i] == 'Each':
            bot = {'type': words[i + 1], 'costs': []}
            bps[-1].append(bot)
            i += 4
        elif words[i] == 'and':
            i += 1
        else:
            assert words[i].isdigit(), (i, words[i])
            quantity = int(words[i])
            mineral = words[i + 1].rstrip('.')
            bps[-1][-1]['costs'].append((quantity, mineral))
            i += 2
    return [to_array(bp) for bp in bps]


def prune_states(states, max_costs, time_left):
    states = states.copy()

    # Once we have enough of a reosurce that we can't ever run out, there
    # is no benefit to tracking quantities of the resource above that level,
    # so we cap resource counts to keep state counts down
    for state in states:
        for i in range(3):
            deficit = max_costs[i] - state[i]
            max_useful_quantity = max_costs[i] + deficit * time_left
            if state[i + 4] >= max_useful_quantity:
                state[i + 4] = max_useful_quantity

    for i in range(7, -1, -1):
        idxs = np.argsort(states[:, i], kind='stable')
        states = states[idxs]

    new_states = np.zeros(states.shape, dtype=states.dtype)
    n = 0

    for i in range(len(states)):
        redundant = np.any(np.all(states[i] <= states[i+1:], axis=1))
        if not redundant:
            new_states[n] = states[i]
            n += 1

    return new_states[:n]


def simulate(bp, duration):
    max_costs = [max(bp[i][j] for i in range(4)) for j in range(4)]
    states = np.zeros([1, 8], dtype=np.uint32)
    states[0][0] = 1

    for i in range(duration):
        new_states = np.zeros([0, 8], dtype=np.uint32)
        for state in states:
            bots = state[:4]
            resources = state[4:]
            n = len(new_states)
            new_states = np.resize(new_states, (n + 1, 8))
            new_states[n] = np.append(bots, resources + bots)
            for j, bot_cost in enumerate(bp):
                if j < 3 and bots[j] >= max_costs[j]:
                        continue # No benefit to building more bots of this type
                if np.all(resources >= bot_cost):
                    new_bots = bots.copy()
                    new_bots[j] += 1
                    new_resources = resources + bots - bot_cost
                    n = len(new_states)
                    new_states = np.resize(new_states, (n + 1, 8))
                    new_states[n] = np.append(new_bots, new_resources)
        pre_prune = len(new_states)
        states = prune_states(new_states, max_costs, duration - i - 1)

    return  max(states[:, 7])


def main(input_file):
    bps = parse_input(input_file)

    quality = 0
    for i, bp in enumerate(bps):
        n = simulate(bps[i], 24)
        quality += (i + 1) * n
    print("Part 1:", quality)

    product = 1
    for i, bp in enumerate(bps[:3]):
        n = simulate(bp, 32)
        product *= n
    print("Part 2:", product)


if __name__ == '__main__':
    main('inputs/day19input.txt')