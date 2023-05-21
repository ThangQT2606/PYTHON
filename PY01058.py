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
        b = int(n[-4::])
        # print(b)
        if nto(b):
            print('YES')
        else:
            print("NO")