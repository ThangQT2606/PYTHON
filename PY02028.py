from math import *

def nto(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, isqrt(n)+1):
            if n%i == 0:
                return False
        return True

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = [nto(i) for i in a]
    c = []
    for i in a:
        if nto(i):
            c.append(i)
    c.sort()
    index = 0
    for i in range(n):
        if b[i] == False:
            print(a[i], end = ' ')
        else:
            print(c[index], end = ' ')
            index += 1

