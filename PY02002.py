from math import *
def fibo(a, b):
    f = []
    f.append(0)
    f.append(1)
    f.append(1)
    for i in range(3, b+1):
        f.append(f[i-2]+f[i-1])
    # print(a)
    for i in range(a, b+1):
        print(f[i], end = ' ')

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        a, b = map(int, input().split())
        fibo(a, b)
        print()
        cnt += 1