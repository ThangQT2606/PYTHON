from math import*
from functools import cmp_to_key
def cmp(a, b):
    tich1, tich2 = tong(a), tong(b)
    if tich1 != tich2:
        return tich1 - tich2
    else:
        return a-b
def tong(n):
    res = 1
    while n > 0:
        res += n%10
        n //= 10
    return res


if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        n = int(input())
        a = list(map(int, input().split()))
        a.sort(key = cmp_to_key(cmp))
        for i in a:
            print(i, end = ' ')
        print()
        cnt += 1