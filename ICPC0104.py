from math import*
t = int(input())
while (t >0):
    t-=1
    s = input()
    k = 'abcdefghijklmnopqrstuvwxyz'
    for i in k:
        s=s.replace(i,' ')
    a = s.split()
    # print(a)
    # print(s)
    for i in range(0,len(a)):
        a[i] = int(a[i])
    print(min(a))