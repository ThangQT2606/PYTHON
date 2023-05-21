from math import *

def sang(a):
    a[0], a[1] = False, False
    for i in range(2, isqrt(10**6)+1):
        if a[i]:
            for j in range(i*i, 10**6+1, i):
                a[j] = False

if __name__ == '__main__':
    a = [True] * (10 ** 6 + 1)
    sang(a)
    n, x = map(int, input().split())
    m = n
    pri = []
    for i in range(0, 10**6+1):
        if a[i] and m > 0:
            m -= 1
            pri.append(i)
    # print(pri)
    print(x, end = ' ')
    for i in range(n):
        v = x + pri[i]
        print(v, end = ' ')
        x += pri[i]