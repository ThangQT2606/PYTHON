from math import*
def solve(n):
    print('1 * ', end = '')
    for i in range(2, isqrt(n)+1):
        if n%i == 0:
            dem = 0
            while n%i == 0:
                dem += 1
                n //= i
            print(i, dem, sep = '^', end = '')
            if n != 1:
                print(' * ', end = '')
    if n > 1:
        print(n, 1, sep = '^', end = '')

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        n = int(input())
        solve(n)
        print()
        cnt += 1