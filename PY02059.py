from math import *
def nto(n):
    if n < 2:
        return False
    elif n == 2:
        return False
    else:
        for i in range(2, isqrt(n)+1):
            if n%i == 0:
                return False
        return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    ln, ok = -1e9, 0
    for i in range(n):
        for j in range(m):
            if nto(a[i][j]) and a[i][j] > ln:
                ln = a[i][j]
                ok = 1
    if ok == 1:
        print(ln)
    dem = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == ln:
                dem += 1
                print('Vi tri [', i,']','[',j,']', sep = '')
    if dem == 0:
        print('NOT FOUND')
