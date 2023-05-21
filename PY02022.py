from math import*

def nto(n):
    if n < 2:
        return False
    else:
        for i in range(2, isqrt(n)+1):
            if n%i == 0:
                return False
        return True
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    dic = {}
    for x in a:
        if nto(x):
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
    for val, fre in dic.items():
        print(val, fre)
    
        