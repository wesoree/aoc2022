from math import lcm
from aocinput import aocsplitday
DAY = 24
import functools
data = aocsplitday(DAY, False, False, True)
depth = len(data)-2
width = len(data[0])-2
start = (1,0)
end = (width, depth+1)
walls = set([(x,y) for x in (0,width+1) for y in range(depth+2)] + [(1,-1),(width, depth+2)]
           +[(x,y) for y in (0,depth+1) for x in range(width+2) if ((x,y) != start and (x,y) != end)])
b_key = {'<': (-1,0), '>': (1,0), '^': (0,-1), 'v': (0,1)}
blizzard = [(x,y,b_key[tile]) for y,row in enumerate(data) for x,tile in enumerate(row) if tile in '^v<>']

@functools.cache
def move_blizzard(time):
    squares = walls.copy()
    for x,y,(dx,dy) in blizzard:
        squares.add((1 + (x-1+dx*time)%width, 1 + (y-1+dy*time)%depth))
    return squares

def successors(square, forbidden):
    s = []
    x,y = square
    for dx,dy in [(0,1), (1,0), (-1,0), (0,-1), (0,0)]:
        if (nx:=x+dx,ny:=y+dy) not in forbidden: 
            s.append((nx,ny))
    return s

def bfs(start, end, start_time):
    explored = set()
    frontier = [(start_time,start)]
    while frontier:
        time, square = frontier.pop(0)
        time += 1
        for next in successors(square, move_blizzard(time%(width*depth))):
            if (time, next) not in explored:
                if next == end:
                    return time
                explored.add((time, next))
                frontier.append((time, next))

print(p1 := bfs(start, end, 0), bfs(start, end, bfs(end, start, p1)))