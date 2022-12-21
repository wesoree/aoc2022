from collections import defaultdict
from collections import deque
import os
import string
GridList = []
with open("inputs/day12input.txt", "r") as data:
    for t in data:
        Line = t.strip()
        GridList.append(Line)

Height = len(GridList)
Width = len(GridList[0])
GridDict = defaultdict()
for y, l in enumerate(GridList):
    for x, a in enumerate(l):
        if a == "S":
            GridDict[(x,y)] = 0
            StartPoint = (x, y)
        elif a == "E":
            GridDict[(x,y)] = 25
            EndGoal = (x,y)
        else:
            GridDict[(x,y)] = string.ascii_lowercase.index(a)

ImperialCore = set()
ImperialCore.add(StartPoint)
ImperialFrontier = deque()
ImperialFrontier.appendleft((0, StartPoint))
Directions = [(0,1),(0,-1),(1,0),(-1,0)]
while ImperialFrontier:
    CurrentDist, Location = ImperialFrontier.popleft()
    if Location == EndGoal:
        Part1Answer = CurrentDist
        break
    X, Y = Location
    CurrentHeight = GridDict[Location]

    for dx, dy in Directions:
        NX, NY = X+dx, Y+dy
        if NX < 0 or NX >= Width or NY < 0 or NY >= Height:
            continue
        NewLocation = (NX,NY)
        if NewLocation in ImperialCore:
            continue
        NewHeight = GridDict[NewLocation]
        if CurrentHeight + 1 >= NewHeight:
            NewDistance = CurrentDist + 1
            NewEntry = (NewDistance, NewLocation)
            ImperialFrontier.append(NewEntry)
            ImperialCore.add(NewLocation)

######################Part 2

ImperialCore = set()
ImperialCore.add(EndGoal)
ImperialFrontier = deque()
ImperialFrontier.appendleft((0, EndGoal))
while ImperialFrontier:
    CurrentDist, Location = ImperialFrontier.popleft()
    X, Y = Location
    CurrentHeight = GridDict[Location]
    if CurrentHeight == 0:
        Part2Answer = CurrentDist
        break

    for dx, dy in Directions:
        NX, NY = X+dx, Y+dy
        if NX < 0 or NX >= Width or NY < 0 or NY >= Height:
            continue
        NewLocation = (NX,NY)
        if NewLocation in ImperialCore:
            continue
        NewHeight = GridDict[NewLocation]
        if CurrentHeight - 1 <= NewHeight:
            NewDistance = CurrentDist + 1
            NewEntry = (NewDistance, NewLocation)
            ImperialFrontier.append(NewEntry)
            ImperialCore.add(NewLocation)

        
print(f"{Part1Answer = }")
print(f"{Part2Answer = }")