from math import *

if __name__ == '__main__':
    s = input()
    k = int(input())
    a = []
    if len(s)%2 != 0:
        s = s[:len(s)-1]
    # print(s)
    for i in range(0, len(s), 2):
        a.append(int(s[i:i+2]))
    a.sort()
    # print(a)
    dem = 0
    d = dict()
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for val, fre in d.items():
        if fre >= k:
            dem += 1
            print(val, fre)
    if dem == 0:
        print('NOT FOUND')