from math import *

a = [True] * (10**6+1)
def sang():
    a[0], a[1] = False, False
    for i in range(2, isqrt(10**6)+1):
        if a[i] == True:
            for j in range(i*i, 10 ** 6+1,i):
                a[j] = False
t = int(input())
while(t > 0):
     t -= 1
     n = int(input())
     sang()
     dem =0
     for i in range(0,n-6):
        if a[i] and a[i+2] and a[i+6]:
            # print(i,i+2,i+6)
            dem +=1
        elif a[i] and a[i+4] and a[i+6]:
            # print(i,i+4,i+6)
            dem +=1
     print(dem)