with open('dec1input.txt', 'r', encoding='UTF-8') as inventory:
    elflist = [line.rstrip() for line in inventory]
    elfsum = []
    top3 = []
    for i in elflist:
        elves=map(int,i.split())
        a = sum(elves)
        elfsum.append(a)
    print(max(elfsum)) # this prints out the max value of total calories per elf, PART 1 ONLY
    def maxelves(c):        # will find the top numbers depending on the num inside.
        for num in range (0, c):    
            b = max(elfsum)
            top3.append(b)
            elfsum.remove(b)
    maxelves(3)

    print(sum(maxelves)) # part 2 only

    