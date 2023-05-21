from math import *

if __name__ == '__main__':
    # t = int(input())
    # cnt = 1
    # while cnt <= t:
    n = int(input())
    dem = 0
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                dem += 1
                # print(a[i], a[j])
    print(dem)