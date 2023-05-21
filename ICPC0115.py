from math import*

def sum(n):
    m, res = n, 0
    while n > 0:
        res += factorial(n%10)
        n //= 10
    if res == m:
        return True
    else:
        return False
if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        n = int(input())
        if sum(n):
            print("Yes")
        else:
            print("No")