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
    b = [0]*(100)
    for i in a:
        if b[i] == 0:
            print(i, end = ' ')
            b[i] = 1
