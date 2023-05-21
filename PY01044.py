import math

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    t1 = list(s1.split())
    t2 = list(s2.split())
    a = set()
    for x in t1:
        s = x.lower()
        a.add(s)
    b = set()
    for x in t2:
        s = x.lower()
        b.add(s)
    c = list(a.union(b))
    d = list(a.intersection(b))
    c.sort()
    d.sort()
    for x in c:
        print(x, end = ' ')
    print()
    for x in d:
        print(x, end = ' ')
    print()

