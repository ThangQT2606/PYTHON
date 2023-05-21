from math import *

if __name__ == '__main__':
    s = input()
    cs8 = ''
    while len(s)%3 != 0:
        s = '0'+s
    # print(s)
    for i in range(0, len(s), 3):
        a = s[i:3+i]
        res = 0
        # print(a)
        for j in range(len(a)):
            res += (int(a[j]))* 2**(2-j)
        cs8 += str(res)
    print(cs8)
