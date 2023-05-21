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
        for j in range(i + 1, n):
            delta1 += a[i][j]
            delta2 += a[j][i]
    if abs(delta1-delta2) < k:
        print('YES')
        print(abs(delta1-delta2))
    else:
        print('NO')
        print(abs(delta1-delta2))
