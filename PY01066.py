from math import *
# a = [True]*(10**6 + 1)
# def sang():
#     a[0] = a[1] = False
#     for i in range(2, isqrt(10**6)+1):
#         if a[i]:
#             for j in range(i*i, 10**6+1, i):
#                 a[j] = False

# def solve(n):
#     res = 0
#     if a[n]:
#         res += n
#     else:
#         while n%2 == 0:
#             res += 2
#             n //= 2
#         for i in range(3, isqrt(n)+1, 2):
#             while n%i == 0:
#                 res += i
#                 n //= i
#         if n > 1:
#             res += n
#     return res

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        dem = 0
        s1 = input()
        s2 = s1[::-1]
        for i in range(len(s1)):
            if abs(ord(s1[i]) - ord(s1[i - 1])) == abs(ord(s2[i]) - ord(s2[i - 1])):
                dem += 1
        if dem == len(s1):
            print('YES')
        else:
            print('NO')