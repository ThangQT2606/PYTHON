import math

p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while( True):
    x = input()
    if(x == '0'):
        break
    a , b =x.split()
    a = int(a)
    s=""
    for i in b:
        c = p.index(i)
        s += p[(c+a) % 28]
    print(s[::-1])