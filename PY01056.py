import math

def nto(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i== 0:
            return False
    return True

def chan(n):
    for i in range(0,len(n)):
        if (i % 2 == 0) and int(n[i]) % 2 == 0:
            return True
    return False

def le(n):
    for i in range(0,len(n)):
        if (i % 2 != 0) and int(n[i]) % 2 != 0:
            return True
    return False

def tong(n):
    sum = 0
    for i in n:
        sum += int(i)
    if nto(sum):
        return True
    return False

t = int(input())
while(t > 0):
    t -= 1
    n = input()
    if chan(n) and le(n) and tong(n):
        print("YES")
    else:
        print("NO")

    # print(chan(n))
    # print(le(n))

    