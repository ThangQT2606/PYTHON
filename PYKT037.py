from math import *

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        n, b = map(int, input().split())
        a = []
        while n > 0:
            x = n%b
            if x >= 10:
                a.append(chr(x+55))
            else:
                a.append(x)
            n //= b
        for i in range(len(a)-1, -1, -1):
            print(a[i], end = '')
        print()
