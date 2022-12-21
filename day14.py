LineList = []
with open("inputs/day14input.txt", "r") as data:
    for t in data:
        Line = t.strip().split(" -> ")
        for n, l in enumerate(Line):
            X, Y = l.split(",")
            X, Y = int(X), int(Y)
            NewTuple = (X,Y)
            Line[n] = NewTuple
        LineList.append(tuple(Line))

RockSet = set()
LowestY = 10
for l in LineList:
    X, Y = l[0]
    RockSet.add((X, Y))
    for k in range(1, len(l)):
        TX, TY = l[k]
        while TX > X:
            X += 1
            RockSet.add((X,Y))
        while TX < X:
            X -= 1
            RockSet.add((X,Y))
        while TY > Y:
            Y += 1
            RockSet.add((X,Y))
            if Y > LowestY:
                LowestY = Y
        while TY < Y:
            Y -= 1
            RockSet.add((X,Y))

SandRestSet = set()
NotVoid = True
Part1Done = False
while NotVoid:
    X, Y = 500,0
    Falling = True
    while Falling:
        if Y > LowestY:
            if not(Part1Done):
                Part1Answer = len(SandRestSet)
                Part1Done = True
            SandRestSet.add((X,Y))
            break
        NX, NY = X, Y+1
        if (NX,NY) not in RockSet and (NX,NY) not in SandRestSet:
            X, Y = NX, NY
            continue
        NX, NY = X-1, Y+1
        if (NX,NY) not in RockSet and (NX,NY) not in SandRestSet:
            X, Y = NX, NY
            continue
        NX, NY = X+1, Y+1
        if (NX,NY) not in RockSet and (NX,NY) not in SandRestSet:
            X, Y = NX, NY
            continue
        SandRestSet.add((X,Y))
        if (X,Y) == (500,0):
            NotVoid = False
            break
        Falling = False
        break

Part2Answer = len(SandRestSet)  

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")