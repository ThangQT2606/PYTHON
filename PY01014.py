import math

a, k, n = map(int, input().split())
h = 0
n = int(n/k)+1

for i in range(1,n):
    x = i * k - a
    if x >0:
        h =1
        print(x,end=' ')
if h ==0:
    print("-1")