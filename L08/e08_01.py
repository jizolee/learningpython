def chop(t):
    del(t[0])
    del(t[-1])
    print(t)
    t.sort()

def middle(t):
    t1=t[1:-1]
    return t1

letter=['a','b','c','d']
chop(letter)
middle(letter)