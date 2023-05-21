from math import *

if __name__ == '__main__':
    n = int(input())
    a = []
    delta1, delta2 = 0, 0
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    k = int(input())
    for i in range(n):
        for j in range(n - 1 - i):
            delta1 += a[i][j]
    # print(delta1)
    for i in range(1, n):
        x = i
        while x > 0:
            x -= 1
            delta2 += a[i][n-1-x]
    # print(delta2)
    if abs(delta1-delta2) <= k:
        print('YES')
        print(abs(delta1-delta2))
    else:
        print('NO')
        print(abs(delta1-delta2))