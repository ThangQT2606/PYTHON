from math import*
def nto(n):
    if n < 2:
        return False
    else:
        for i in range(2, isqrt(n) + 1):
            if n%i == 0:
                return False
        return True

def sum(n):
    res = 0
    while n > 0:
        res += n%10
        n //= 10
    return nto(res)

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
        a, b = map(int, input().split())
        m = ucln(a, b)
        if(sum(m)):
            print("YES")
        else:
            print("NO")