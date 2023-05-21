from math import *
a = [True]*(10**6 + 1)
def sang():
    a[0] = a[1] = False
    for i in range(2, isqrt(10**6)+1):
        if a[i]:
            for j in range(i*i, 10**6+1, i):
                a[j] = False

def solve(n):
    res = 0
    if a[n]:
        res += n
    else:
        while n%2 == 0:
            res += 2
            n //= 2
        for i in range(3, isqrt(n)+1, 2):
            while n%i == 0:
                res += i
                n //= i
        if n > 1:
            res += n
    return res

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        s = input()
        n = int(input())
        n = str(n)
        dem = 0
        i = 0
        while i <= len(s) - len(n):
            a = s[i:(len(n)+i)]
            # print(a)
            if a == n:
                i += len(n)
                dem += 1
            else:
                i += 1
        print(dem)