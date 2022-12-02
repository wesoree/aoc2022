with open('dec1input.txt', 'r', encoding='UTF-8') as inventory:
    elflist = [line.rstrip() for line in inventory]
    elfsum = []
    top3 = []
    for i in elflist:
        elves=map(int,i.split())
        a = sum(elves)
        elfsum.append(a)    
    def maxelves():
        b = max(elfsum)
        top3.append(b)
        elfsum.remove(b)
    maxelves()
    maxelves()
    maxelves()
    c = sum(top3)

    print(c)

    