def partone(throw, response):
    pts = 0
    if throw == 'A': 
        if response == 'X': 
            pts += 4
        elif response == 'Y':
            pts += 8
        elif response == 'Z':
            pts += 3
    elif throw == 'B': 
        if response == 'X': 
            pts += 1
        elif response == 'Y':
            pts += 5
        elif response == 'Z':
            pts += 9
    elif throw == 'C': 
        if response == 'X': 
            pts += 7
        elif response == 'Y':
            pts += 2
        elif response == 'Z':
            pts += 6
    return pts
def parttwo(throw, response):
    pts = 0
    if throw == 'A': 
        if response == 'X': #lose
            pts += 3
        elif response == 'Y': #draw
            pts += 4
        elif response == 'Z': #win
            pts += 8
    elif throw == 'B': 
        if response == 'X': 
            pts += 1
        elif response == 'Y':
            pts += 5
        elif response == 'Z':
            pts += 9
    elif throw == 'C': 
        if response == 'X': 
            pts += 2
        elif response == 'Y':
            pts += 6
        elif response == 'Z':
            pts += 7
    return pts

p1score = 0
p2score = 0

with open('day2input.txt') as data:
    data = [line.strip() for line in data.readlines()]

    for round in data:
        p1score += partone(round[0], round[2])
        p2score += parttwo(round[0], round[2])
 
print(p1score)
print(p2score)
    
        
        