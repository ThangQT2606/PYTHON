from math import *

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    k = int(input())
    print(s1[0:k-1] + s2 + s1[k-1:])
