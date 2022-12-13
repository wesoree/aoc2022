sections = [[list(map(int, s.split('-'))) for s in line.split(',')] for line in open("day4input.txt").read().splitlines()]

full_overlap = sum([a >= c and b <= d or c >= a and d <= b for (a, b), (c, d) in sections])
print(full_overlap) #part 1

overlap = sum([a <= c <= b or a <= d <=b or c <= b <= d for (a, b), (c, d) in sections])
print(overlap) #part2