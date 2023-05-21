from math import*
def solve(n):
    res , m = 0, n
    dem = 0
    while n > 0:
        res = res * 10 + n%10
        dem += 1
        n //= 10
    if res != m:
        return False
    if res == m and dem%2 == 0:
        return True
def cs(n):
    while n > 0:
        m = n%10
        if m != 0 and m != 2 and m != 4 and m != 6 and m != 8:
            return False
        n //= 10
    return True
if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        n = int(input())
        if n > 21:
            for i in range(22, n):
                if cs(i) and solve(i):
                    print(i, end = ' ')
        print()