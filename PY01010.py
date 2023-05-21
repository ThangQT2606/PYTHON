from math import*
#C1
def check(n):
    m = n%100
    while n > 100:
        n //= 10
    if n == m:
        return True
    else:
        return False

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        n = int(input())
        if n > 1000:
            if check(n):
                print("YES")
            else:
                print("NO")
#C2
t = int(input())
while(t > 0):
    t -= 1
    n = input()
    if int(n[:2])==int(n[-2:]):
        print("YES")
    else:
        print("NO")
