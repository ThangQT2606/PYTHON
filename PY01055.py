import math
def check(n):
    for i in range(0,len(n),2):
        if (n[i] != n[-1]) and (n[i] !=n[i+1]) :
            return False
    return True

t = int(input())
while(t > 0):
    t -= 1
    n = input()
    # print(len(n))
    # print(n[0],n[1])
    # for i in range(0,len(n),2):
    #     print(n[i],end="")
    if check(n)== True and len(n) % 2 == 1 and (n[0] != n[1]):
        print("YES")
    else:
        print("NO")
    # print(check(n))
    # print()
    # print(n[-1])