import math

def tong(n):
    sum =0
    for i in range(len(n)):
        sum += int(n[i])
    if sum % 10 != 0:
        return False
    # print(sum)
    return True

def cach(n):
    for i in range(len(n)-1):
        if (abs(int(n[i])-int(n[i+1])) != 2):
            return False
    return True

t = int(input())
while( t > 0):
    t -= 1
    n = input()
    if tong(n) == True and cach(n) == True:
        print("YES")
    else:
        print("NO")
    # print(tong(n))
    # print(cach(n))
    