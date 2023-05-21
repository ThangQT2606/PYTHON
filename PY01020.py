from math import*

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while(cnt <= t):
        n = int(input())
        if n % 100 == 86:
            print("YES")
        else:
            print("NO")
        cnt += 1