from math import*

def nto(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def dao(n):
    res = 0
    while n > 0:
        res = res*10 + n%10
        n //= 10
    if(nto(res)):
        return True
    else:
        return False
def tong(n):
    res = 0
    while n > 0:
        res += n%10
        n //= 10
    if(nto(res)):
        return True
    else:
        return False
def cs(n):
    while n > 0:
        m = n%10
        if m != 2 and m != 3 and m != 5 and m != 7:
            return False
        n //= 10
    return True
if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        n = int(input())
        if cs(n) and nto(n) and dao(n) and tong(n):
            print("Yes")
        else:
            print("No")
        cnt += 1