from math import *

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        dem = 0
        for i in range(n):
            if a[i] <= b[i]:
                dem += 1
        if dem == n:
            print('YES')
        else:
            print('NO')