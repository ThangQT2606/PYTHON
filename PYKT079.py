from math import *

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        # print(a)
        dem = 0
        for i in range(min(a), max(a)):
            if i not in a:
                # print(i, end = ' ')
                dem += 1
        print(dem)

