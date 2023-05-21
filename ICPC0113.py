from math import *


def sang(a):
    a[0], a[1] = False, False
    for i in range(2, isqrt(10**6)+1):
        if a[i] == True:
            for j in range(i*i, 10 ** 6+1,i):
                a[j] = False
def dao(n):
    res = 0
    while n > 0:
        res = res * 10 + n %10
        n //= 10
    return res
t = int(input())
while(t > 0):
    t -= 1
    a = [True] * (10** 6 +1)
    sang(a)
    n = int(input())
    for i in range(10,n):
        if a[i] == True:
            rev = dao(i)
            if i != rev and a[rev] == True and rev < n:
                print(i , rev,end=' ')
                a[rev] = False
    print()



