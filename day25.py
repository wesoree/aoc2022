from aocinput import aocday, aocsplit
from time import time 

DAY = 25

t = aocsplit(DAY, False, None)

def s2n(s):
    v = 0
    for c in s:
      v = 5*v + {"0":0,"1":1,"2":2,"-":-1,"=":-2}[c]
    return v

def n2s(n):
    r = ""
    while n != 0:
        n,m = divmod(n,5)
        if m >=3:
            n += 1
        m -= 5
        r += "=-012"[m+2]
    return r[::-1]

print(n2s(sum(map(s2n,t))))
