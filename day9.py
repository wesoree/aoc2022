from collections import defaultdict

filename = 'day9input.txt'

with open(filename) as f:
    lines = [line.rstrip().split(' ') for line in f]


def move_head(direction, c_pos):
    d_map = {'R': [1, 0], 
             'L': [-1, 0],
             'U': [0, -1],
             'D': [0, 1]}
    return tuple([position + increase for position, increase in zip(c_pos, d_map[direction])])


def move_tail(t_pos, h_pos):
    p_difference = [y - x for x, y in zip(t_pos, h_pos)]
    if max([abs(p) for p in p_difference]) <= 1:
        return t_pos
    move_direction = []
    for p in p_difference:
        if p == 0:
            move_direction.append(0)
        else:
            move_direction.append(p//abs(p))
    return tuple([current + increase for current, increase in zip(t_pos, move_direction)])
def solve(num_knots):
    moves = []
    knot_list = [(0, 0) for _ in range(num_knots)]
    tail_visited = defaultdict(int)
    tail_visited[knot_list[-1]] = 1

    for this_line in lines:
        moves.append([this_line[0], int(this_line[1])])
    
    for this_move in moves:
        move_dir, total_steps = this_move
        for _ in range(total_steps):
           knot_list[0] = move_head(move_dir, knot_list[0])
           for i in range(1, num_knots):
                # Move each tail relative to the knot ahead of it in the list
                new_knot_position = move_tail(knot_list[i], knot_list[i-1])
                if new_knot_position != knot_list[i]:
                    knot_list[i] = new_knot_position
                    if i == num_knots - 1:
                        tail_visited[knot_list[i]] += 1
    return len(tail_visited)

print(f'part 1: {solve(2)}')
print(f'part 2: {solve(10)}')