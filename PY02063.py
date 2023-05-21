from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    c = a[0] * a[1]
    # print(a[len(a)-1])
    # print(a[len(a)-2])
    # 5 10 -2 3 5 2
    d = a[len(a)-1] * a[len(a)-2]
    k = a[0] * a[1] * a[len(a)-1]
    f = a[len(a)-1] * a[len(a)-2] * a[len(a)-3] 
    print(max(c,d,k,f))