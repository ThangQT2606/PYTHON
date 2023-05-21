from math import *

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        n = int(input())
        dem = 0
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        for i in range(n):
            if a[i] <= b[i]:
                dem += 1
        if dem == n:
            print('YES')
        else:
            print('NO')
        cnt += 1