from math import*
   
if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        n, x, m = map(float, input().split())
        dem = 0
        while n <= m:
            lai = n*(x/100)
            n += lai
            dem += 1
        print(dem)