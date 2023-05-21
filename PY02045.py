from math import *
if __name__ == '__main__':
    s = input()
    while len(s) > 1:
        n = len(s)//2
        a = int(s[:n]) + int(s[n:])
        print(a)
        s = str(a)