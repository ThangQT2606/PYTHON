import math

def nto(n):
    if n < 2 :
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True

t = int(input())
while(t > 0):
    t -= 1
    co , khong = 0,0
    n = input()
    for i in n:
        if nto(int(i)):
            co +=1
        else:
            khong +=1
    if nto(len(n)) and (co > khong):
        print("YES")
    else:
        print("NO")


