from math import*
def nto(n):
    if n < 2:
        return False
    else:
        for i in range(2, isqrt(n)+1):
            if n%i == 0:
                return False
        return True

def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a%b)    
if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        n = int(input())
        k = 0
        for i in range(n):
            if(ucln(i, n) == 1):
                k += 1
        if nto(k):
            print("YES")
        else:
            print("NO")