from math import *

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    ln, ok, nn = -1e9, 0, 1e9
    for i in range(n):
        for j in range(m):
            if a[i][j] > ln:
                ln = a[i][j]
            if a[i][j] < nn:
                nn = a[i][j]
    # print(ln , nn)
    delta = ln - nn
    for i in range(n):
        for j in range(m):
            if a[i][j] == delta:
                ok = 1
    if ok == 1:
        print(delta)
    dem = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == delta:
                dem += 1
                print('Vi tri [', i,']','[',j,']', sep = '')
    if dem == 0:
        print('NOT FOUND')