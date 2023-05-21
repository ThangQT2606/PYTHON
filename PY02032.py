from math import *

def nto(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, isqrt(n)+1):
            if n%i == 0:
                return False
        return True

if __name__ == '__main__':
    s = input()
    a = []
    if len(s)%2 != 0:
        s = s[:len(s)-1]
    # print(s)
    for i in range(0, len(s), 2):
        a.append(int(s[i:i+2]))
    a = set(a)
    b = list(a)
    b.sort()
    for i in b:
        print(i, end = ' ')
