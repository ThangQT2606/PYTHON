from math import *
def thuan_nghich(n):
    res, m = 0, n
    while n > 0:
        res = res*10 + n%10
        n //= 10
    if res == m:
        return True
    else:
        return False

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    ln, ok = -1e9, 0
    for i in range(n):
        for j in range(m):
            if a[i][j] > 10 and thuan_nghich(a[i][j]) and a[i][j] > ln:
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
