from math import*
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
        sum = 0
        if(n % 2 == 0):
            for i in range(2, n+1, 2):
                sum += 1/i
            print('%.6f' %sum)

        else:
            for i in range(1, n+1, 2):
                sum += 1/i
            print('%.6f' %sum)
