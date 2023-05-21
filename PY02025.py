from math import *

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    A = set(a)
    B = set(b)
    C = A.intersection(B)
    C = list(C)
    C.sort()
    for i in C:
        print(i, end = ' ')
    print()
    D = A.difference(B)
    D = list(D)
    D.sort()
    for i in D:
        print(i, end = ' ')
    print()
    E = B.difference(A)
    F = list(E)
    F.sort()
    for i in F:
        print(i, end = ' ')
    print()