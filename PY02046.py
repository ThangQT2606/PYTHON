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
    n = int(input())
    a = list(map(int, input().split()))
    index = [0]*1000
    b = []
    for i in a:
        if index[i] == 0:
            b.append(i)
            index[i] = 1
    # print(b)
    dem = 0
    for i in range(len(b)):
        if nto(sum(b[:i+1])) and nto(sum(b[i+1:])):
            dem = 1
            print(i)
            break
    if dem == 0:
        print('NOT FOUND')
    # print(tong)