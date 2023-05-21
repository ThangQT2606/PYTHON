from math import *
# def fibo(a, b):
#     f = []
#     f.append(0)
#     f.append(1)
#     f.append(1)
#     for i in range(3, b+1):
#         f.append(f[i-2]+f[i-1])
#     # print(a)
#     for i in range(a, b+1):
#         print(f[i], end = ' ')

def swap(n):
    res = 0
    while n > 0:
        res = res*10 + n%10
        n //= 10
    return res

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        n = int(input())
        dem = 0
        # print(swap(n))
        while n % 7 != 0:
            n = n + swap(n)
            dem += 1
            if n%7 == 0 or dem == 1000:
                break
        if dem < 1000:
            print(n)
        else:
            print(-1)
