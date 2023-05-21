from math import *

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        n = int(input())
        a = list(map(int, input().split()))
        d = dict()
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for val, fre in d.items():
            if fre%2 == 1:
                print(val)
