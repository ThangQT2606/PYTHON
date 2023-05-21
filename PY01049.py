from math import*

def nto(n):
    if n < 2:
        return False
    else:
        for i in range(2, isqrt(n)+1):
            if n%i == 0:
                return False
        return True

def check(n):
    demnt = 0
    for i in range(len(n)):
        if nto(int(n[i])):
            demnt += 1
            # print(n[i])
    # print('dem:' ,demnt)
    notnto = len(n) - demnt
    # print('not', notnto)
    if demnt > notnto:
        return True
    else:
        return False
if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        n = input()
        if nto(len(n)) and check(n):
            print("YES")
        else:
            print("NO")
        # print(check(n))