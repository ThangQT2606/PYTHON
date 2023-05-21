from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(float, input().split()))
    minn = min(a)
    maxx = max(a)
    for i in a:
        if i == minn:
            a.remove(i)
        if i == maxx:
            a.remove(i)
    print('%.2f' %(sum(a)/len(a)))