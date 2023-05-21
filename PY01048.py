from math import*

def solve(n):
    a = []
    for i in range(1, isqrt(n)+1):
        if n%i == 0:
            a.append(i)
            if n//i != i:
                a.append(n//i)
    dem = 0
    for i in a:
        if i != 1:
            s = i*(i-1)//2
            if (n-s)%i == 0:
                dem += 1
    print(dem)
if __name__ == '__main__':
    t = int(input())
    cnt = 0
    while cnt < t:
        cnt += 1
        n = int(input())
        solve(n)