from math import*
def dao(n):
    res = 0
    while n > 0:
        res = res*10 + n%10
        n //= 10
    return res

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
        if(ucln(n, dao(n)) == 1):
            print("YES")
        else:
            print("NO")