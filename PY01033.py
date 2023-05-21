from math import *
a = [True]*(10**6 + 1)
def sang():
    a[0] = a[1] = False
    for i in range(2, isqrt(10**6)+1):
        if a[i]:
            for j in range(i*i, 10**6+1, i):
                a[j] = False

def uc(a, b):
    if b == 0:
        return a
    else:
        return uc(b, a%b)

if __name__ == '__main__':
    # t = int(input())
    # cnt = 1
    # sang()
    # while cnt <= t:
    #     cnt += 1
    l, r = map(int, input().split())
    for i in range(l, r-1):
        for j in range(i+1, r):
            if uc(i, j) == 1:
                for k in range(j + 1, r+1):
                    if uc(j, k) == 1 and uc(i, k) == 1:
                        print('(', end = '')
                        print(i, j, k, sep = ', ', end = ')')
                        print()


