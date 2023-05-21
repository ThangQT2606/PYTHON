from math import *

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        res = 0
        s = input()
        a = []
        dilim = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for x in s:
            if x in dilim:
                a.append(x)
        a.sort()
        for x in s:
            if '0' < x <= '9':
                res += int(x)
        a.append(res)
        for x in a:
            print(x, end = '')
        print()