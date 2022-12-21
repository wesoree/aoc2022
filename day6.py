from collections import deque

with open('inputs/day6input.txt') as file:
    line = file.read()

def solve(length):
    q = deque()
    for i, c in enumerate(line):
        q.append(c)
        if len(q) > length:
            q.popleft()
        if len(set(q)) == length:
            return i + 1
# part 1

print(solve(4)) 

# part 2

print(solve(14))