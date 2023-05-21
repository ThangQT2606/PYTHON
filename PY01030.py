from math import*
def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a%b)

if __name__ == '__main__':
    dem = 0
    n, k = map(int, input().split())
    trc, sau = 10**(k-1), 10**k
    if n > 10:
        for i in range(trc, sau):
            if(ucln(n, i) == 1):
                dem += 1
                print(i, end = ' ')
                if dem%10 == 0:
                    print()
    print()
