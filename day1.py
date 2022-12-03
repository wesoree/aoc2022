with open('day1input.txt', 'r', encoding='UTF-8') as inventory:
    elflist = [line.rstrip() for line in inventory]
    elfsum = []
    top3 = []
    for i in elflist:
        elves = map(int, i.split())
        a = sum(elves)
        elfsum.append(a)
    # part 1
    print(max(elfsum))

    def maxelves(c):
        for num in range(0, c):
            b = max(elfsum)
            top3.append(b)
            elfsum.remove(b)
    maxelves(3)
    # part 2
    print(sum(top3))
