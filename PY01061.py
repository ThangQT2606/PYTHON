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
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        n = input()
        if len(n) > 3:
            a = int(n[0:3])
            b = int(n[-3::])
            if nto(a) and nto(b):
                print("YES")
            else:
                print("NO")